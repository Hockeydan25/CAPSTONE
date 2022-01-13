# Write a program that asks for your name and the month you were born in.
# Then, your program should print
# •	A greeting to you, using your name
# •	A message with the number of letters in your name
# •	A 'Happy birthday month!' message if you were born in the current month
# o	Easier - compare the user's input to "January" or "August" or whatever the current month is
# o	Harder - use Python to figure out the current month and use that in the comparison. 
#     Check out the  datetime library.
#Lab1 Dan Smestad ITEC 2905-80 Software Dev. Capstone Clara James
name = input('What is your name? ')
birthday_month = input('What month were you born in? ')

if birthday_month == "january":
    print('Happy Birthday Month!!')
else:
    print(f'hello + {name},+ nice to meet you!')
    
len('dan') 



 
