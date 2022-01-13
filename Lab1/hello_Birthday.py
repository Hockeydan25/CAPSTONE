#Lab1 Dan Smestad ITEC 2905-80 Software Dev. Capstone Clara James
# Write a program that asks for your name and the month you were born in.
# Then, your program should print
# •	A greeting to you, using your name
# •	A message with the number of letters in your name
# •	A 'Happy birthday month!' message if you were born in the current month
# o	Easier - compare the user's input to "January" or "August" or whatever the current month is
# o	Harder - use Python to figure out the current month and use that in the comparison. 
# Check out the  datetime library.


import datetime

x = datetime.datetime.now() # calculates current date and time

print('Current month is: ' + x.strftime("%B")) # this output is only month + note to say what out pot is.

name = input('What is your name? ')#user input prompt
birthday_month = input('What month were you born in? ') # another input to use data in out program.

if birthday_month == x : #special event message if January is the month 
    print('Happy Birthday Month!!')
else:
    print(f'hello + {name},+ nice to meet you!') # could make several messages here with specail month also.

name_length = len(name)    #variable to hold length of name
print('There are ' + str(name_length) + ' letters in your name: ') 
#using the variable in a useful way.   



 
