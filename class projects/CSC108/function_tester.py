import os.path, math


def clean_up(s):
    ''' Return a version of string str in which all letters have been
    converted to lowercase and punctuation characters have been stripped 
    from both ends. Inner punctuation is left untouched. '''
    
    punctuation = '''!"',;:.-?)([]<>*#\n\t\r'''
    result = s.lower().strip(punctuation)
    return result


def list_to_split(text):
    '''xx'''
    
    long_string = ''
    
    for words in text:
        long_string += words
    split_string = long_string.split()
    return split_string
        
def remove_blanks(text):
    ''' xx '''
    
    i = 0
    while i <= len(text):
        for word in text:
            if word.strip() == '':
                text.remove(word)
                i = 0 
            else:
                i += 1
    return text



def number_of_words(text):
    '''x'''
    
    length = 0
    for word in text:
        word = clean_up(word)
        if word.strip() != '':
            length += 1
    return length

def average_word_length(text):
    ''' Return the average length of all words in text. Do not
    include surrounding punctuation in words. 
    text is a non-empty list of strings each ending in \n.
    At least one line in text contains a word.'''

    total_letters = 0
    total_length = 0
    words_list = list_to_split(text)
    for word in words_list:
        word = clean_up(word)
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
    split_text = list_to_split(text)
    total_length = number_of_words(split_text)
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
    
    for word in split_text:
        word = clean_up(word)
        if word not in one_occurance:
            one_occurance.append(word)
        else:
            if word not in two_occurance:
                two_occurance.append(word)
    remove_blanks(one_occurance)
    remove_blanks(two_occurance)
    
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
    
    for item in result:
        for char in item:
            if char in separators:
                item = item.replace(char, separators[0])
    result = item.split(separators[0])
    remove_blanks(result)
    return result

def find_sentence(text):
    '''x'''
    
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
    
    for sentence in sentences:
        number_of_phrases += len(split_on_separators(sentence, ',;:'))
    
    average_num_of_phrases = number_of_phrases / float(number_of_sentences)
    
    return average_num_of_phrases

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
    
    difference_value = 0
    for i in range(1, 6):
        difference_value += abs(sig1[i] - sig2[i]) * weight[i]
    
    return  difference_value
    

if __name__ == '__main__':
    text = ["The time has come, the Walrus said\n", "To talk of many things: of shoes - and ships - and sealing wax,\n", "Of cabbages; and kings.\n" "And why the sea is boiling hot;\n"  "and whether pigs have wings.\n"] 
    text2 = [" Hi there, hi my name is\n", "Hi Jackson,  - hi nice to - meet you.\n"]
    text3 = ["This. is simply"," the average, number of! characters; per word.", " calculated: after the !", "punctuation has been stripped using the already-written?" , " clean_up function"]
    a = '!This. is, fUN ! . Haha. this I lo!ve this..'
    text4 = ["How do you know, what I: am going\n", "To do; with what I have in my. Aresneal you\n" , "have to be crazy, if you: think I'm.\n", "done:.\n"]
    text5 = ['The time has come, the Walrus said\n', 'To talk of many things: of shoes - and ships - and sealing wax,\n', 'Of cabbages; and kings.\nAnd why the sea is boiling hot;\nand whether pigs have wings.\n']
    print hapax_legomana_ratio(text)
    print hapax_legomana_ratio(text2)
    print hapax_legomana_ratio(text3)
    print average_word_length(text)
    print average_word_length(text2)
    print average_word_length(text3)
    print type_token_ratio(text)
    print type_token_ratio(text2)
    print type_token_ratio(text3)
    b = ['', '', 's', '          ','  ', 'c' ,'b ']
    w = ['jack', 4.0, 2.3, 4.5 , 1.2, .54]
    g = ['steve', 21.0, .31, 1.4, 53.3, 21.4]
    we = ['s', 3, 3,5, 1,5]
    print compare_signatures(w, g, we)
    print avg_sentence_complexity(text)