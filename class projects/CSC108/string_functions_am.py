'''Some functions to practise working with strings. Exercises: (1) complete
all the functions. (2) Write a main block that tests them.'''

def num_vowels(s):
    '''Return the number of vowels in string s. Do no treat the letter "y" as
    a vowel.'''

    vowel_count = 0
    for char in s:
        if char in "aeiou":
            vowel_count += 1  # short for vowel_count = vowel_count + 1
    return vowel_count

 
def reverse(s):
    '''Return a new string that is s in reverse.'''
    
    # An accumulator:
    reverse_s = ""
    # build up the proper value of reverse_s
    for char in s:
        reverse_s = char + reverse_s
    return reverse_s


def remove_spaces(s):
    '''Return a new string that is the same as s but with any blanks
    removed.'''
    
    no_space = XX
    for char in s:
        if char != " ":  # Short for if not(char == " "):
            # Add char into no_space
            no_space = no_space + char
    return no_space

    
def num_matches(s1, s2):
    '''Return the number of characters in s1 that appear in s2.'''
    
    pass