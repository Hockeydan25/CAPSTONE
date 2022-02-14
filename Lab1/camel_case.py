"""
Lab1 Dan Smestad ITEC 2905-80 Software Dev. Capstone Clara James
Write a program that turns a sentence into camel case. 
The first word is lowercase, the rest of the words have their initial letter capitalized, 
and all of the words are joined together. For example, with the input "fOnt proCESSOR and ParsER", 
 your program will output "fontProcessorAndParser". 
 """
import re
#made several changes here for lab3 Branches lesson.


def camelcase(sentence):
    """ 
    Convert sentence to camelCase, for example, "Display all books" 
    is converted to "displayAllBooks" 
    """
    title_case = sentence.title()  # Uppercase first letter of each word
    upper_camel_cased = title_case.replace(' ', '')  # remove spaces 
    special_character_filter = re.sub(r'[\\@_!#$%^&*()<>?/|}{~:;[\]]', '', upper_camel_cased)
    # Lowercase first letter, join with rest of string 
    # Slices don't produce index out of bounds errors. 
    # So this still works on empty strings, strings of length 1
    return special_character_filter[0:1].lower() + special_character_filter[1:] 

def banner():
    """Display program name"""
    message = 'Awesome camelcase program!!'
    stars= '*' * len(message)
    print(f'\n{stars} \n{message} \n{stars}')

def main():
    banner()
    sentence = input('Enter your sentence: ')
    output = camelcase(sentence)
    print(output)
if __name__ == '__main__':
    main()