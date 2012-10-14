#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/time.h>
#include "helper.h"
	
/** Return the index of the record with lowest word frequency in an array. **/
int lowestIndex(struct rec *rarray, int rsize){
	int lowest = 0;
	int i;
	for (i=1; i<rsize; i++){
		if (rarray[lowest].freq == -1) {
			lowest = i;
		}
		if ((rarray[i].freq != -1) && (rarray[i].freq < rarray[lowest].freq)){
				lowest = i;
		}	
	}
	return lowest;
}
/** Child processes will read records from their own chunk of data into an array and write
	records one at a time into the pipe connecting to a parent process. 
	i is used as an index, 
	remainder is an int that determines addition distribution for each child
	dist determines how many records each child will sort
	bytesRead is used to determine how many bytes of a file previous processes have read
	filen is the file containing records to read from**/
int dowork(int i, int fdint, int remainder, int dist, int bytesRead, char* filen){
	FILE *infp;
	if ((infp = fopen(filen, "r")) == NULL){
    	fprintf(stderr, "Could not open %s\n", filen);
        exit(1);
	}
	int recsize = sizeof(struct rec);
	// 
	if (remainder > i){
		// this will distribute the remainders evenly to each process by adding one more
			dist = dist + 1;}
	int k;
	struct rec *rarray = malloc(recsize* dist);	   
	struct rec r; 
	/** The next block is used to determine how many bytes have been read so far by other 
		processes.
		case1: i = 0 so no bytes read before it
		case2: there are still remainders to be distributed, handled by if clause
		case3: if this is a process that did not get a remainder but is following a process 
				that did, else if clause
		case 4: if this is not a remainder process at all and does not procede one, else clause
	**/
	if (i > 0){
    		 if (remainder > i){
              bytesRead = i*(dist*recsize); }
		 	else if (remainder == i){
				bytesRead = i*((dist+1)*recsize);
			}
          else{
              bytesRead = remainder*((dist+1)*recsize) + (i-remainder)*(dist*recsize);
          }
     }
	
	// seek the correct byte amount and read dist records into an array to sort
	if (fseek(infp, bytesRead, SEEK_SET) == -1){
		perror("fseek");
		exit(1);
	}
	for(k=0; k<dist; k++) {
		if (fread(&r, recsize, 1, infp) == 1){
			rarray[k] = r;
		}
	}

	if (dist != 0) {
		qsort(rarray, dist, recsize, compare_freq);
		// comp to determine when a child stops writing into the pipe
		// stops writing when dist amount of records have been written
		int comp = 0;
		while (comp < dist){
			if (write(fdint, &rarray[comp], recsize) == -1){
				perror("write");
				exit(1);			
			}
			comp++;
			}
	}
	free(rarray);
	close(fdint);
	exit(0);
}

int main(int argc, char *argv[]) {
	int procs;
	char *infile = NULL, *outfile = NULL;
	char ch;
	FILE *outfp;
	int recsize = sizeof(struct rec);
	
	// error check for usage
	if (argc != 7) {
		fprintf(stderr, "Usage: psort -n <number of processes>"
				"-f <input file name> -o <output filename>\n");
		exit(1);
	}

	// read in arguments 
	while((ch = getopt(argc, argv, "n:f:o:")) != -1){
		switch (ch){
		case 'n':
			procs = atoi(optarg);
			break;
		case 'f':
			infile = optarg;
			break;
		case 'o':
			outfile = optarg;
			break;
		default : fprintf(stderr, "Usage: psort -n <number of processes>"
					   "-f <input file name> -o <output filename>\n");
		}
	}
	if (procs < 1) {
		fprintf(stderr, "Usage: psort -n number of processes has to be at least 1\n");
		exit(1);
	}
	if ((outfp = fopen(outfile, "w")) == NULL){
		fprintf(stderr, "Could not open %s\n", outfile);
        exit(1);
     }	
	// find total number of records in infile
	int fileSize = get_file_size(infile);
	int numRecords = fileSize / recsize;
	// find number of records left after distributing evenly
	int remainder = numRecords % procs; 
	//find even number of records to distribute to each process
	int dist = (numRecords - remainder) / procs;
	struct rec merged[procs];	
	// handle a case where the number of records is less than processes 
	if (numRecords < procs){
		procs = numRecords;
	}
	int i,bytesRead = 0;
	pid_t fpid = 1;	
	int fd[procs][2];
	
	/**************************************************
						Timer start
	**************************************************/
	struct timeval starttime, endtime;
	double timediff;
	if( (gettimeofday(&starttime, NULL)) == -1) {
		perror("gettimeofday");
		exit(1);
	}

	for (i=0; i<procs; i++){
		pipe(fd[i]);
		if ((fpid  = fork()) < 0){
			perror("fork");
			exit(1);
		} 
		if (fpid != 0){
			close(fd[i][1]);
			if (read(fd[i][0], &merged[i], recsize) == -1){
				perror("read");
				exit(1);				
			}
			// parent will start performing its merge and sort only after its children
			// have all written to pipe
			if (i == procs-1){
					int comp = 0;
					int low = 0;
					while ((comp < numRecords)){
						low = lowestIndex(merged, procs);
						 if ((fwrite(&merged[low], recsize, 1, outfp)) != 1){
            				fprintf(stderr, "Could not write to %s\n", outfile);
        				}
						if (read(fd[low][0], &merged[low], recsize) == 0){
							merged[low].freq = -1;
							close(fd[low][0]);		
						}
						comp++;
					}
			}
		}
		if (fpid == 0){
			close(fd[i][0]);
			dowork(i, fd[i][1], remainder, dist, bytesRead, infile);
		}
	}
	
	if( (gettimeofday(&endtime, NULL)) == -1) {
		perror("gettimeofday");
		exit(1);
		}
	/******************************************
				Timer end
	******************************************/
	timediff = (endtime.tv_sec - starttime.tv_sec) +
					(endtime.tv_usec - starttime.tv_usec) / 1000000.0;
	fprintf(stdout, "%.4f\n", timediff);	
	return 0;
}
