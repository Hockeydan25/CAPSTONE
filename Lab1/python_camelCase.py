"""Lab1 Dan Smestad ITEC 2905-80 Software Dev. Capstone Clara James
Write a program that turns a sentence into camel case. 
The first word is lowercase, the rest of the words have their initial letter capitalized, 
and all of the words are joined together. For example, with the input "fOnt proCESSOR and ParsER", 
 your program will output "fontProcessorAndParser". """

"""made several more changes here for lab3 Branches lesson."""

"""Camelcase converter program! have fun, it's useful!"""

def camelCase(sentence):
	""" Convert sentence to camelCase, for example, "Display all books" 
	is converted to "displayAllBooks" """
    
	title_case = sentence.title() # Uppercase first letter of each word
	upper_camel_cased = title_case.replace(' ', '') # remove spaces
    #Optional: implement a filter to remove special characters from the input string. 
	# Lowercase first letter, join with rest of string 
	# Slices don't produce index out of bounds errors. 
	# So this still works on empty strings, strings of length 1
	return upper_camel_cased[0:1].lower() + upper_camel_cased[1:] 



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
    sentence = input('Enter your sentence: ')
    output = camelCase(sentence)
    print(output)
if __name__ == '__main__':
    main()

#output = '' #empty varible string we can put the new string in for storing. 

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

  # TODO Optional: implement a filter to remove special characters from the input string. 
#   Write a test for this filter.   
#     Python program to remove all special characters from string:

#     take string
#     string = input('Enter any string: ')

#     initializing special characters
#     special_char = '@_!#$%^&*()<>?/\|}{~:;[]'
    
#     using join() + generator to remove special characters
#     new_string = ''.join(x for x in string if not x in special_char)
    
#     print string without special characters
#     print('New string:', new_string)      


