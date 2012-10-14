#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <stdlib.h>
#include <ctype.h>
#include "freq_list.h"

/* Remove all punctuation from beginning of word. */

char *strip_left_punct(char *word) {
	int i = 0;
	while (!(isalnum(word[i])))
	{
		i++;
	}
	word = word + i;
	return word;
}
/* Remove all punctuation from end of word. */

char *strip_right_punct(char *word) {
	int i = strlen(word)-1;
	// get where the last alpha character is
	while (i > 0)
	{
		if (isalnum(word[i])){
			break;}
		i--;
	}
	word[i+1] ='\0';
	return word;
}

/* Strip all punctuation from the beginning and end of a word. */

char *strip_punct(char *word){
	// if word contains no letters or digits
	char *alphas = "abcdefghijklmnopqrstuvwxyz1234567890";
	if (strpbrk(word, alphas) == NULL){
		return "";}
	word = strip_left_punct(word);
	word = strip_right_punct(word);
	return word;
}
/* Conver any uppercase letters to lower case in word/ */

char *lowercase(char *word){
	int i;
	char thisChar;
	for (i = 0; word[i] != '\0'; i++)
	{	
		thisChar= word[i];
		word[i] = tolower(thisChar);
	}
	return word;
}

/* Return a pointer to a modified version of word. The modified version of word will convert 
*  any uppercase characters to lowercase, and also strip any punctuation characters
*  from beginning and end of word.
*/

char *clean_word(char *word){
	char *cpy = malloc(strlen(word)+1);
	strncpy(cpy, word, strlen(word)+1);
	cpy = lowercase(cpy);
	cpy = strip_punct(cpy);
	return cpy;
}

int main(int argc, char **argv)
{
    Node *head = NULL;
    char **filenames = init_filenames();
    char ch;
    char *indexfile = "index";
    char *namefile = "filenames";

    while((ch = getopt(argc, argv, "i:n:")) != -1) {
        switch (ch) {
        case 'i':
            indexfile = optarg;
            break;
        case 'n':
            namefile = optarg;
            break;
        default:
            fprintf(stderr, "Usage: indexfile [-i FILE] [-n FILE ] FILE...\n");
            exit(1);
        }
    }
      
    while(optind < argc) {
		FILE *fname;
		if((fname = fopen(argv[optind], "r")) == NULL) {
			perror("Name file");
			exit(1);
		}

		char line[MAXLINE];
		char splitBy[] = " \t\n";
		char *token;
		char *cleaned_token;

		while ((fgets(line, MAXLINE, fname)) != NULL){
			token = strtok(line, splitBy);
			while (token != NULL) {
				cleaned_token = clean_word(token);
				//only add_word if not empty string
				if (strcmp(cleaned_token, "") != 0)	
				{
					head = add_word(head, filenames, cleaned_token, argv[optind]);
				}
				token = strtok(NULL, splitBy);}
		}

	optind++;
	}
	write_list(namefile, indexfile, head, filenames);
	display_list(head, filenames);
	return 0;
}
