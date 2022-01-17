"""# dan Smestad video instructions lab2 """

#List Comprehension syntax

#The classes a student is register for.
from tkinter import N


classes_registered = ['ITEC 2905','ITEC 2950','INFS 1000','PHED 1132',]
print(classes_registered)
#Make a list of only the ITEC classes
only_itec = [c for c in classes_registered if c.startswith('ITEC')]
print(only_itec )
#like - a loop nested inside a list 
only_itec = [c.lower() for c in classes_registered if c.startswith('ITEC')]
print(only_itec ) #this prints in a lower case with a operation lower().

only_itec = [c for c in classes_registered if c.startswith('INFS') ]
print(only_itec )
# Record temperature every day. Record -1 if not poessible to take measurement.
high_temps = [-1, 78, 72, 53, 42, -1, 51,87,82,-1,54,67,78,-1,70]
print(high_temps)
only_real_measurements = [temp for temp in high_temps if temp != -1] # removes -1 numbers/temps.
print(only_real_measurements)
#Make a list if numbers that represent a valid temperateures measurement.
temp_celsius = [round((temp_f -32)*5/9) for temp_f in only_real_measurements] 
print(f'Converted temps are rounded:{temp_celsius}')#a math operation on variable run against the list and converts.
#set round on math operation not sure if hurts math calculation.I think round rounds up.
average = sum(temp_celsius)/ len(temp_celsius)
print(f'The average to the 2 decimal is {average:.2f}C')

#Your turn
'''My try'''
# number_list = [2,4,6]
# print(number_list)
# new_number_list = [n for n in number_list + 1 ]
# print(new_number_list) 

number_list = [2,4,6]
one_plus = [n+1 for n in number_list]
print(one_plus)

# removes all negative number or ones less than zero.
number_list2 = [1,-10,40,-500,350]
pos_nums = [n for n in number_list2 if n >=0]
print(pos_nums)
# doubles all numbers, negative number too.
number_list3 = [1,10,-25,40,500,350,0]
double_nums = [n*2 for n in number_list3]
print(double_nums)

foods = ['chesse pizza', 'peperoni pizza', 'ice cream', 'veggie pizza', 'tacos']
pizzas = [food for food in foods if 'pizza' in food]
print(pizzas) #prints all the pizzas,had cheese pizza P capitalized and it didn't print.

foods = ['chesse pizza', 'peperoni pizza', 'ice cream', 'veggie pizza', 'tacos']
pizzas = [food.upper() for food in foods if 'pizza' in food]
print(pizzas)# prints ouput in uppercase.

#traditional loop statement Equivalent:
foods = ['chesse pizza', 'peperoni pizza', 'ice cream', 'veggie pizza', 'tacos']
pizzas = []
for food in foods:
    if 'pizza' in food:
        uppercase_pizza = food.upper()
        pizzas.append(uppercase_pizza)
print(pizzas)
#okay let's get some pizza, now I'm hungry for it...HA hA

#add a Condition filter the list:
example= [1,5,10]
is_one_in_list = 1 in example #True.
is_seven_in_list = 7 in example #False.
print(is_one_in_list)
print(is_seven_in_list)

course = 'ITEC 2905 Software Development Capstone'
if '2905' in course:
    print('This is Software Development Capstone')

