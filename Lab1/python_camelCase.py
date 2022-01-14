#Lab1 Dan Smestad ITEC 2905-80 Software Dev. Capstone Clara James
# Write a program that turns a sentence into camel case. 
# The first word is lowercase, the rest of the words have their initial letter capitalized, 
# and all of the words are joined together. For example, with the input "fOnt proCESSOR and ParsER", 
# your program will output "fontProcessorAndParser". 

output = '' #empty varible string we can put the new string in for storing. 

edit = 'fOnt proCESSOR and ParsER' # string we want to edit.

words = edit.split() # function split will seperate the string into a manageablbe list.
# print(words)

for i in range(len(words)): # setup for loop in range , using the length of the words to set loop count. 
    if i == 0: # set i to zero first word we will apply a lower casing to it. 
        output = words[i].lower() # takes our emtpy variable ans put the lowercase word font into.
    else:                         # when not zero we will count trough 1-3 and capitalize each word.  
        output = output + words[i].capitalize() #placeing words with function Cap to each and adding first output.
print(output)         
# print statement prints the final version. I would have thouth I needed to to use
#  end= '' to remove new line? but it plsaced and words on one line. The loop probably did this inplace of the print statement where it would be new lines.



#video code following along. 
# class_code = { 2950: 'cap', 2905: 'physical', 3300: 'resumes', 3142: 'Literacy'}

# for code in class_code:
#     print(code)
#     print(class_code[code])

# for code, name in class_code.items(): # tuple I need help with tuple understaning.
#     print('The class code is ' + str(code) + 'and the name is ' + name) 

# for code, name in class_code.items(): # tuple I need help with tuple understaning.
#     print(f'The class code is {code} and the name is {name}') # f  format string




