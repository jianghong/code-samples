#include <stdio.h>
#include <string.h>
#include <strings.h>
#include <unistd.h>
#include <stdlib.h>        /* for getenv */
#include <sys/types.h>
#include <sys/stat.h>
#include <sys/socket.h>
#include <netinet/in.h>    /* Internet domain header */
#include <time.h>
#include <dirent.h>
#include <utime.h>
#include "wrapsock.h"
#include "filedata.h"

#define PORT 34908

/* Concatenate file to dir with a '/' in between to form a full path to file.
   This is used for stat. */
char *cat_path(char* dir, char* file){
	char* result;
	char* toCat;
	
	toCat = malloc(strlen(dir)+1);
	toCat = strcpy(toCat, dir);
	result = malloc(strlen(dir) + strlen(file)+2);
	result = strncat(toCat, "/", 1);
	result = strncat(result, file, strlen(file));
	
	return result;
}

/* Create and return a sync_message given a filename, last modified time of the 
	file and size of the file. */
struct sync_message make_sync_message(char* filename, long int mtime, int size){
	struct sync_message sm;
	strncpy(sm.filename, filename, strlen(filename)+1);
	sm.mtime = mtime;
	sm.size = size;
	return sm;
}

/* Overwrite a local file pointed to by fp with another file being sent through socstream. 
	fsize is the size of the new file being sent. */
int overwrite_local(FILE *fp, int fsize, int socstream, char *dir, int bytes_read){
	int size = CHUNKSIZE;
	if ((fsize - bytes_read) < CHUNKSIZE){
		size = (fsize - bytes_read);
	}
	char buf[size];
	int a;

	Readn(socstream, buf, size);

	if ((a = fwrite(buf, sizeof(char), size, fp)) < 0){
		perror("fwrite");
		exit(1);
	}

	return a;
}

/* Overwrite a remote file through socstream with a local file.
	fsize is the size of the local file. */
void overwrite_remote(char *filename, int fsize, int socstream){
	FILE *fp;
	int size = CHUNKSIZE;		
	int bytes_sent = 0;
	char buf[size];

	if((fp = fopen(filename, "r")) == NULL){
		perror("fopen");
		exit(1);	
	}
	while (bytes_sent < fsize){
		if ( (fsize - bytes_sent) < CHUNKSIZE){
			size = fsize - bytes_sent;
		}
		fread(buf, sizeof(char), size, fp);
		Writen(socstream, buf, size);
		bytes_sent += size;	
	}
	fclose(fp);
}

/* Change the modified time of file pointed to by fp to mtime */
void match_mtime(char *path, int mtime){
	struct stat sbuf;
	struct utimbuf new_times;	

	if (stat(path, &sbuf) != 0){
		perror("stat");
		exit(1);
	}

	new_times.actime = sbuf.st_atime;
	new_times.modtime = mtime;
	
	if (utime(path, &new_times) < 0){
		perror("utime");
		exit(1);
	}

	if (stat(path, &sbuf) != 0){
		perror("stat");
		exit(1);
	}
	return;
}

int main(){
	int soc, i, connfd, clientfd;
	int maxfd, maxi, nready;
	int on = 1, status;
	char *path;
	fd_set allset, rset, wset;
	struct sockaddr_in self;
	struct sockaddr_in peer;
	unsigned int peer_len = sizeof(peer);
	FILE *fp;

	self.sin_family = PF_INET;
	self.sin_port = htons(PORT);
	printf("Listening on %d\n", PORT);
	self.sin_addr.s_addr = INADDR_ANY;
	bzero(&(self.sin_zero), 8);
	
	peer.sin_family = PF_INET;

	/* set up listening socket soc */
	soc = Socket(PF_INET, SOCK_STREAM, 0);
	
	/* Make sure can reuse port */
	status = setsockopt(soc, SOL_SOCKET, SO_REUSEADDR, 
								(const char *)&on, sizeof(on));
	if (status == -1){
		perror("setsockopt");
	}

	/* init dirs and clients */
	init();

	Bind(soc, (struct sockaddr *)&self, sizeof(self));
	Listen(soc, 1);

	/* Set up for select to handle multiple clients */
	maxfd = soc;
	maxi = -1;
	FD_ZERO(&allset);
	FD_SET(soc, &allset);	
	
	for (; ;){
		struct login_message lmbuf;
		struct sync_message smbuf;
		struct sync_message response;
		DIR *dp;
		struct dirent *entry;
		struct stat sbuf, local;
		rset = allset;
		wset = allset;
		nready = Select(maxfd+1, &rset, &wset, NULL, NULL);
	
	 	/* Handle new connections */
		if (FD_ISSET(soc, &rset)){
			connfd = Accept(soc, (struct sockaddr *)&peer, &peer_len);
			for (i = 0; i < MAXCLIENTS ; i++){
				if (clients[i].sock < 0){
					clients[i].sock = connfd; 
					printf("Accepted a new client!\n");
					break;
				}
			}
			if (i == MAXCLIENTS){
				printf("too many clients\n");
				close(connfd);
			}
			else{
				FD_SET(connfd, &allset);
				if (connfd > maxfd){
					maxfd = connfd;
				}
				if (i > maxi){
					maxi = i;		
				}
			}
			if (--nready <= 0){
				continue;
			}	
		}

		/* Handle data exchange */ 
		for (i = 0; i <= maxi; i++){

			if ( (clientfd = clients[i].sock) < 0){
				continue;		
			}
			if (FD_ISSET(clientfd, &rset)){
			/* Handle LOGIN case */
				if (clients[i].STATE == LOGIN){
					Readn(clientfd, (struct login_message*)&lmbuf, sizeof(struct login_message));
					add_client(lmbuf, clientfd);
					printf("Logging in...%s\n", clients[i].userid);
					/* check if directory exists on server*/
					path = cat_path("server_files", clients[i].dirname);
					if ((dp = opendir(path)) == NULL){
						/* create the directory on the server side */
						if ( (mkdir(path, 0777)) < 0){
							perror("mkdir");
						}
						printf("created new directory %s\n", clients[i].dirname);
					}
			
				}
			/* Handle SYNC case */
			else if (clients[i].STATE == SYNC){
				path = cat_path("server_files", clients[i].dirname);
				Readn(clientfd, (struct sync_message*)&smbuf, sizeof(struct sync_message));
				smbuf.mtime = ntohl(smbuf.mtime);
				smbuf.size = ntohl(smbuf.size);

				/* if sync_message is empty */
				if (smbuf.mtime == 0){
					 printf("Getting empty sync..probably done syncing everything\n");
					if ((dp = opendir(path)) == NULL){
							perror("opendir");
					}
					 while ((entry = readdir(dp)) != NULL){
						path = cat_path(path, entry->d_name);
						if (stat(path, &local) == -1){
							perror("stat");
							exit(1);
						}
						/* check if file is a regular file i.e. not a dir */
						if (S_ISREG(local.st_mode)){
							int check = check_file(clients[i].files, entry->d_name, local.st_mtime);
							if (check == 1){	
								/* if a file does not exist in clients files then send it */
								response = make_sync_message(entry->d_name, local.st_mtime, local.st_size);
								response.mtime = htonl(response.mtime);
								response.size = htonl(response.size);
								Writen(clientfd, (struct sync_message*)&response, sizeof(struct 													sync_message));
								overwrite_remote(path, local.st_size, clientfd);	
							}
						}
						path = cat_path("server_files", clients[i].dirname);
					}

					/* after sending any missing files, send an empty sync message */
					response = make_sync_message("", 0, 0);
					response.mtime = htonl(response.mtime);
					response.size = htonl(response.size);
					Writen(clientfd, (struct sync_message*)&response, sizeof(struct sync_message));
				}
					
				/* non empty sync message */
				else {
					path = cat_path("server_files", clients[i].dirname);
					int check = check_file(clients[i].files, smbuf.filename, smbuf.mtime);
					path = cat_path(path, smbuf.filename);
					if (check == 0){
						/* file is already on server side */
						/* find the existing file to compare mtime with */
						if (stat(path, &sbuf) == -1){
							perror("stat");
							exit(1);
						}
						response = make_sync_message(smbuf.filename, sbuf.st_mtime, sbuf.st_size);
						response.mtime = htonl(response.mtime);
						response.size = htonl(response.size);
						Writen(clientfd, (struct sync_message*)&response, sizeof(struct sync_message));

						/* if file on server is more recent */
						if (sbuf.st_mtime > smbuf.mtime){
							printf("Writing file %s to client...\n", smbuf.filename);
							overwrite_remote(path, sbuf.st_size, clientfd);		
							clients[i].STATE = SYNC;						
						}
					
				   }
					/* else file not on server side, or server side outdated */
					else if (check == 1){
						clients[i].STATE = GETFILE;
						strncpy(clients[i].currFilename, smbuf.filename, MAXNAME);	
						clients[i].expected_size = smbuf.size;
						clients[i].received_so_far = 0;			
						clients[i].mtime = smbuf.mtime;
						response = make_sync_message("", 0, 0);
						response.mtime = htonl(response.mtime);
						response.size = htonl(response.size);
						Writen(clientfd, (struct sync_message*)&response, sizeof(struct sync_message));
						path = cat_path("server_files", clients[i].dirname);
						path = cat_path(path, clients[i].currFilename);
						printf("getting file...%s\n", clients[i].currFilename);
						if((fp = fopen(path, "w")) == NULL) {
							perror("fopen");
							exit(1);
					  	}
					}
					else{
						fprintf(stderr, "no more space for files!\n");
			   }
			}	
		}	
		/** Handle GETFILE case **/
	 	else if (clients[i].STATE == GETFILE){

			clients[i].received_so_far += 
							overwrite_local(fp, clients[i].expected_size, clientfd, 													clients[i].dirname, clients[i].received_so_far);
			if (clients[i].received_so_far >= clients[i].expected_size){
				clients[i].STATE = SYNC;
				fclose(fp);	
				path = cat_path("server_files", clients[i].dirname);
				path = cat_path(path, clients[i].currFilename);		
				match_mtime(path, clients[i].mtime);
			}
		}

	}
}
}
	return 0;
}
