import os.path, math

def clean_up(s):
    ''' Return a version of string str in which all letters have been
    converted to lowercase and punctuation characters have been stripped 
    from both ends. Inner punctuation is left untouched. '''
    
    punctuation = '''!"',;:.-?)([]<>*#\n\t\r'''
    result = s.lower().strip(punctuation)
    return result

def list_to_split(text):
    '''Return a list of strings obtained from text and split by a 
    white space. text is a non-empty list of strings each ending in \n.
    At least one line in text contains a word.'''
    
    # Create an empty string to combine strings in text
    long_string = ''
    
    # Iterate through strings in text and add to long_string to split
    for words in text:
        long_string += words
    split_string = long_string.split()
    return split_string
        
def remove_blanks(text):
    '''Remove any empty and blankstrings in text. text is a list 
    of strings'''
    
    i = 0
    # Iterate through text to remove empty and blank strings
    while i <= len(text):
        for word in text:
            if word.strip() == '':
                text.remove(word)
                # If word is removed, i reverts to 0 in order to start again
                i = 0 
            else:
                i += 1
    return text

def number_of_words(text):
    '''Return the number of words in text. text is a list of words'''
    
    count = 0
    # clean_up word in text to make sure it is not just punctuation
    for word in text:
        word = clean_up(word)
        if word.strip() != '':
            count += 1
    return count


def average_word_length(text):
    ''' Return the average length of all words in text. Do not
    include surrounding punctuation in words. 
    text is a non-empty list of strings each ending in \n.
    At least one line in text contains a word.'''

    
    total_letters = 0
    total_length = 0
    # Convert text to a list of strings that are words
    words_list = list_to_split(text)
    
    for word in words_list:
        word = clean_up(word)
        # Count word as a word only if it's nonblank and nonpunctuation
        if word.strip() != '':
            total_letters += len(word)
            total_length += 1
    average_length = total_letters / float(total_length)
    return average_length
    

def type_token_ratio(text):
    ''' Return the type token ratio (TTR) for this text.
    TTR is the number of different words divided by the total number of words.
    text is a non-empty list of strings each ending in \n.
    At least one line in text contains a word. '''

    index = []
    # Convert text to a list of strings that are words
    split_text = list_to_split(text)
    total_length = number_of_words(split_text)
    # Append new words to index to form a list of different words
    for words in split_text:
        words = clean_up(words)
        if words not in index:
            index.append(words)
    remove_blanks(index)
    TT_count = len(index)
    type_token_ratio = TT_count / float(total_length)
    return type_token_ratio
    
                
def hapax_legomana_ratio(text):
    ''' Return the hapax_legomana ratio for this text.
    This ratio is the number of words that occur exactly once divided
    by the total number of words.
    text is a list of strings each ending in \n.
    At least one line in text contains a word.'''
 
    one_occurance = []
    two_occurance = []
    HL_count = 0
    split_text = list_to_split(text)
    total_length = number_of_words(split_text)
    # Append every different word to one_occurance
    # Append every word in one_occurance that occurs again to two_occurance
    for word in split_text:
        word = clean_up(word)
        if word not in one_occurance:
            one_occurance.append(word)
        else:
            if word not in two_occurance:
                two_occurance.append(word)
    remove_blanks(one_occurance)
    remove_blanks(two_occurance)
    # Determine if words in one_occurance happen in two_occurance, if not
    # the word happens exactly once
    for word in one_occurance:
        if word not in two_occurance:
            HL_count += 1
    hapax_legomana_ratio = HL_count / float(total_length)
    return hapax_legomana_ratio


def split_on_separators(original, separators):
    ''' Return a list of non-empty, non-blank strings from the original string
    determined by splitting the string on any of the separators.
    separators is a string of single-character separators.'''  
    
    result = [original]
    # Iterate through characters in original to replace all separators
    # with the first separator
    for item in result:
        for char in item:
            if char in separators:
                item = item.replace(char, separators[0])
    # Split the new string by the first separator
    result = item.split(separators[0])
    remove_blanks(result)
    return result
                
    
def find_sentence(text):
    '''Return a list of sentences obtained from text.
    text is guaranteed to have at least one sentence.
    Terminating punctuation defined as !?.
    A sentence is defined as a non-empty string of non-terminating
    punctuation surrounded by terminating punctuation
    or beginning or end of file. '''
    
    string = ''
    for item in text:
        string += item
    sentence_split = split_on_separators(string, '.!?')
    remove_blanks(sentence_split)
    return sentence_split                
    
def average_sentence_length(text):
    ''' Return the average number of words per sentence in text.
    text is guaranteed to have at least one sentence.
    Terminating punctuation defined as !?.
    A sentence is defined as a non-empty string of non-terminating
    punctuation surrounded by terminating punctuation
    or beginning or end of file. '''
    
    # Divide total number of words by total number of sentences
    total_length = number_of_words(list_to_split(text))
    sentences = find_sentence(text)
    average_sentence_length = float(total_length) / len(sentences)
    return average_sentence_length
    

def avg_sentence_complexity(text):
    '''Return the average number of phrases per sentence.
    Terminating punctuation defined as !?.
    A sentence is defined as a non-empty string of non-terminating
    punctuation surrounded by terminating punctuation
    or beginning or end of file.
    Phrases are substrings of a sentences separated by
    one or more of the following delimiters ,;: '''
    
    number_of_phrases = 0
    sentences = find_sentence(text)
    number_of_sentences = len(sentences)
    # Split sentences on ,;: to form a list of phrases and sum the len()
    for sentence in sentences:
        number_of_phrases += len(split_on_separators(sentence, ',;:'))
    average_num_of_phrases = number_of_phrases / float(number_of_sentences)
    return average_num_of_phrases
    
    
def get_valid_filename(prompt):
    '''Use prompt (a string) to ask the user to type the name of a file. If
    the file does not exist, keep asking until they give a valid filename.
    Return the name of that file.'''

    filename = raw_input(prompt)
    # Prompt user again if filename does not exist 
    while os.path.exists(filename) == False:
        print "That file does not exist."
        filename = raw_input(prompt)
    return filename
    
def read_directory_name(prompt):
    '''Use prompt (a string) to ask the user to type the name of a directory. If
    the directory does not exist, keep asking until they give a valid directory.
    '''
    
    dirname = raw_input(prompt)
    # Prompt user again if directory does not exist
    while os.path.isdir(dirname) == False:
        print "That directory does not exist."
        dirname = raw_input(prompt)
    return dirname
    
    
def compare_signatures(sig1, sig2, weight):
    '''Return a non-negative real number indicating the similarity of two 
    linguistic signatures. The smaller the number the more similar the 
    signatures. Zero indicates identical signatures.
    sig1 and sig2 are 6 element lists with the following elements
    0  : author name (a string)
    1  : average word length (float)
    2  : TTR (float)
    3  : Hapax Legomana Ratio (float)
    4  : average sentence length (float)
    5  : average sentence complexity (float)
    weight is a list of multiplicative weights to apply to each
    linguistic feature. weight[0] is ignored.
    '''
    
    similarity_value = 0
    # Ignore first element in sig1, sig2, weight and calculate similarity
    for i in range(1, 6):
        similarity_value += abs(sig1[i] - sig2[i]) * weight[i]
    return similarity_value
    
    

def read_signature(filename):
    '''Read a linguistic signature from filename and return it as 
    list of features. '''
    
    file = open(filename, 'r')
    # the first feature is a string so it doesn't need casting to float
    result = [file.readline()]
    # all remaining features are real numbers
    for line in file:
        result.append(float(line.strip()))
    return result
        

if __name__ == '__main__':
    
    prompt = 'enter the name of the file with unknown author:'
    mystery_filename = get_valid_filename(prompt)

    # readlines gives us a list of strings one for each line of the file
    text = open(mystery_filename, 'r').readlines()
    
    # calculate the signature for the mystery file
    mystery_signature = [mystery_filename]
    mystery_signature.append(average_word_length(text))
    mystery_signature.append(type_token_ratio(text))
    mystery_signature.append(hapax_legomana_ratio(text))
    mystery_signature.append(average_sentence_length(text))
    mystery_signature.append(avg_sentence_complexity(text))
    
    weights = [0, 11, 33, 50, 0.4, 4]
    
    prompt = 'enter the path to the directory of signature files: '
    dir = read_directory_name(prompt)
    # every file in this directory must be a linguistic signature
    files = os.listdir(dir)

    # we will assume that there is at least one signature in that directory
    this_file = files[0]
    signature = read_signature('%s/%s'%(dir,this_file))
    best_score = compare_signatures(mystery_signature, signature, weights)
    best_author = signature[0]
    for this_file in files[1:]:
        signature = read_signature('%s/%s'%(dir, this_file))
        score = compare_signatures(mystery_signature, signature, weights)
        if score < best_score:
            best_score = score
            best_author = signature[0]
    print "best author match: %s with score %s"%(best_author, best_score)    
    
