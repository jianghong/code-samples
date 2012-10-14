#include <stdio.h>
#include <string.h>
#include <strings.h>
#include <unistd.h>
#include <stdlib.h>      
#include <sys/types.h>
#include <sys/stat.h>
#include <sys/socket.h>
#include <netinet/in.h>    
#include <time.h>
#include <netdb.h>
#include <dirent.h>
#include <utime.h>
#include "wrapsock.h"
#include "filedata.h"


#ifndef PORT
#define PORT 34908
#endif

/* Create and return a sync_message given a filename, last modified time of the 
	file and size of the file. */
struct sync_message make_sync_message(char* filename, long int mtime, int size){
	struct sync_message sm;
	strncpy(sm.filename, filename, strlen(filename)+1);
	sm.mtime = mtime;
	sm.size = size;
	return sm;
}

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

/* Overwrite a local file with another file being sent through socstream. 
	fsize is the size of the new file being sent. */
void overwrite_local(FILE *fp, int fsize, int socstream){
	int size = CHUNKSIZE;
	char buf[size];
	int cursize = 0;

	while (cursize < fsize){		
		if (fsize - cursize < CHUNKSIZE){
			size = fsize - cursize;		
		}
		Readn(socstream, buf, size);
		cursize += size;
		fwrite(buf, sizeof(char), size, fp);
	}
	fclose(fp);
}

/* Overwrite a remote file through socstream with a local file.
	fsize is the size of the local file. */
void overwrite_remote(char *filename, int fsize, int socstream){
	FILE *fp;
	int bytes_read = 0;
	int size = CHUNKSIZE;
	char buf[size];

	if((fp = fopen(filename, "r")) == NULL){
		perror("fopen");
		exit(1);	
	}
	while (bytes_read < fsize){
		if ( (fsize - bytes_read) < CHUNKSIZE){
			size = fsize - bytes_read;
		}
		fread(buf, sizeof(char), size, fp);
		Writen(socstream, buf, size);
		bytes_read += size;
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

/* Check if the server has new files which the local directory does not have. 
	Download until there are no more new files. */
void check_newfiles(int socstream, char *dir) {
	struct sync_message sm, sm_response;
	FILE *fp;
	char *path;
	
	/* Creates empty sync message with correct byte order */
	sm = make_sync_message("", 0, 0);
	sm.mtime = htonl(sm.mtime);
	sm.size = htonl(sm.size);
	Writen(socstream, (struct sync_message*)&sm, sizeof(struct sync_message));
	Readn(socstream, (struct sync_message*)&sm_response, sizeof(struct sync_message));	
	sm_response.mtime = ntohl(sm_response.mtime);
	sm_response.size = ntohl(sm_response.size);
	path =  cat_path(dir, sm_response.filename);

	/* Continue downloading until server sends back an empty sync message */
	while (sm_response.mtime > 0){
		if ( (fp = fopen(path, "w")) == NULL){
				perror("fopen");
				exit(1);
		} 
		printf("Getting new file from server: %s\n", sm_response.filename);
		overwrite_local(fp, sm_response.size, socstream);
		match_mtime(path, sm_response.mtime);
		Readn(socstream, (struct sync_message*)&sm_response, sizeof(struct sync_message));	
		sm_response.mtime = ntohl(sm_response.mtime);
		sm_response.size = ntohl(sm_response.size);
	}
	
}

int main (int argc, char* argv[]){
	struct hostent *hp;
	struct sockaddr_in peer;
	int soc;
	char* path;
	DIR *dp;
	FILE *fp;
	struct stat local;
	struct dirent *entry;
	struct login_message lm;
	struct sync_message sm, sm_remote;
	
	
	/* Handle usage error */
	if (argc != 4) {
		fprintf(stderr, "Usage: %s <hostname> <userid> <dir>\n", argv[0]);
		exit(1);
	}
	
	/* check host */
	hp = gethostbyname(argv[1]);
	if (hp == NULL) {
		fprintf(stderr, "%s: %s unknown host\n", argv[0], argv[1]);
		exit(1);
	}

	/* Set up to initialize socket */
	peer.sin_family = PF_INET;
	peer.sin_port = htons(PORT);
	printf("PORT = %d\n", PORT);
	peer.sin_addr = *((struct in_addr *)hp->h_addr);


	/* open directory specified */
	dp = opendir(argv[3]);
	if (dp == NULL){
		perror("opendir");
		exit(1);
	}

	/* create socket */
	soc = Socket(PF_INET, SOCK_STREAM, 0);
	
	if (Connect(soc, (struct sockaddr *)&peer, sizeof(peer)) == -1) {
		Close(soc);
		exit(1);	
	}

	/* send login_message */
	strncpy(lm.userid, argv[2], strlen(argv[2])+1);
	strncpy(lm.dir, argv[3], strlen(argv[3])+1);	
	
	/* Write login_message to socket */
	Writen(soc, (struct login_message*)&lm, sizeof(struct login_message));
	
	/* Sync operation process every 5 seconds */
	while(1){


		/* open directory specified */
		dp = opendir(argv[3]);
		if (dp == NULL){
			perror("opendir");
			exit(1);
		}
		/* Iterate through files and send sync message with file info */
		 while ((entry = readdir(dp)) != NULL){	
			path = cat_path(argv[3], entry->d_name);
			if (stat(path, &local) == -1){
				perror("stat");
				exit(1);
			}
			/* check if file is a regular file i.e. not a dir */
			if (S_ISREG(local.st_mode)){
				sm = make_sync_message(entry->d_name, local.st_mtime, local.st_size);
				/* change to network byte order */
				sm.mtime = htonl(sm.mtime);
				sm.size = htonl(sm.size);

				Writen(soc, (struct sync_message*)&sm, sizeof(struct sync_message));
				Readn(soc, (struct sync_message*)&sm_remote, sizeof(struct sync_message));

				/* change from network to host byte order */
				sm_remote.mtime = ntohl(sm_remote.mtime);
				sm_remote.size = ntohl(sm_remote.size);
				sm.mtime = ntohl(sm.mtime);
				sm.size = ntohl(sm.size);
				/* if server has a more recent copy of the file, then overwrite local file */
				if (sm_remote.mtime > sm.mtime){
					printf("overwriting local file...\n");
					path = cat_path(argv[3], sm_remote.filename);
					if((fp = fopen(path, "w")) == NULL) {
						perror("fopen");
						exit(1);
					}
					overwrite_local(fp, sm_remote.size, soc);
					match_mtime(path, sm_remote.mtime);
				}
				/* otherwise overwrite remote file*/				
				else if (sm_remote.mtime < sm.mtime){
					printf("overwriting remote file...\n");	
					overwrite_remote(path, sm.size, soc);
				}
			}
		}
		
		/* check if server has any new files */
		
		check_newfiles(soc, argv[3]);
		/* resync after 5 seconds */
		printf("resyncing in 5...\n");
		sleep(5);
	}
	return 0;	
}
