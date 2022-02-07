"""Lab1 Dan Smestad ITEC 2905-80 Software Dev. Capstone Clara James
Write a program that turns a sentence into camel case. 
The first word is lowercase, the rest of the words have their initial letter capitalized, 
and all of the words are joined together. For example, with the input "fOnt proCESSOR and ParsER", 
 your program will output "fontProcessorAndParser". """

"""made several more changes here for lab3 Branches lesson."""

"""Camelcase converter program! have fun, it's useful!"""
import re

def camelCase(sentence):     
    remove_multiple_spaces = re.sub(r'\s+', ' ', sentence)  # Replace any groups of whitespace with a single space    
    remove_surrounding_space = remove_multiple_spaces.strip()  # remove any remaining whitespace

    words = remove_surrounding_space.split(' ')

    title_case = sentence.title() # Uppercase first letter of each word
    
    
    #Optional: implement a filter to remove special characters from the 
    # input string. 
	# Lowercase first letter, join with rest of string 
	# Slices don't produce index out of bounds errors. 
	# So this still works on empty strings, even strings with length of 1
	

def lowercase(word):
    return word.lower()

def uppercase(word):
    return word[0:1].lower() + word[1:]

#   TODO Optional: implement a filter to remove special characters 
#   from the input string. 
#   Write a test for this filter.   
#   Python program to remove all special characters from string:

def special_character_filter(words):
    #initializing special characters
    special_characters = '@_!#$%^&*()<>?/\|}{~:;[]'
    #using join() + generator to remove special characters
    words = ''.join(x for x in words if not x in special_characters)
    #print string without special characters
    return words

def banner():
    """Display program name, using stars."""
    message = 'Awesome camelcase program!!'       
    stars= '*' * len(message)
    print(f'\n{stars} \n{message} \n{stars}')

def instructions():
    """Display instructions for how to use our program."""
    print('Enter two word pairs and this program will convert it to camelcase.')    

def main():
    banner()
    instructions()
    sentence = input('Enter your two word pairs: ')
    output = camelCase(sentence)
    print(output)

if __name__ == '__main__':
    main()

output = '' #empty varible string we can put the new string in for storing. 

#edit = 'fOnt proCESSOR and ParsER' # string we want to edit.

#words = edit.split() # function split will seperate the string into a manageablbe list.
# print(words)

#for i in range(len(words)): # setup for loop in range , using the length of the words to set loop count. 
#    if i == 0: # set i to zero first word we will apply a lower casing to it. 
#        output = words[i].lower() # takes our emtpy variable ans put the lowercase word font into.
#    else:                         # when not zero we will count trough 1-3 and capitalize each word.  
#        output = output + words[i].capitalize() #placeing words with function Cap to each and adding first output.
#print(output)         
# print statement prints the final version. I would have thouth I needed to to use
#  end= '' to remove new line? but it plsaced and words on one line. The loop probably did this inplace of the print statement where it would be new lines.


#version one:
# video code following along. 
# class_code = { 2950: 'cap', 2905: 'physical', 3300: 'resumes', 3142: 'Literacy'}

# for code in class_code:
#     print(code)
#     print(class_code[code])

# for code, name in class_code.items(): # tuple I need help with tuple understaning.
#     print('The class code is ' + str(code) + 'and the name is ' + name) 

# for code, name in class_code.items(): # tuple I need help with tuple understaning.
#     print(f'The class code is {code} and the name is {name}') # f  format string



