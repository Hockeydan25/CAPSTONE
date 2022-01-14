#Lab1 Dan Smestad ITEC 2905-80 Software Dev. Capstone Clara James.
# Write a program that asks for the names of all of the classes you are taking this semester
# Save these class names in a list. while loop
# Print all the items in the list, one per line.

classes = [] #empty list here to store class names. Array
class_number = int(input('How Many classes are you taking this semester? ')) #user prompt to enter how many classes we aren't using int. 

while True: # while loop, user exits with enter key breaks loop
    class_name = input('Enter the name of the class, or enter to quit: ') #prompt to enter class names
    if not class_name: # if name is Ture prompt is repeated.
        break # enter is keyed and loop exits.
    classes.append(class_name)#calling the list of names user enters,we created empty list/array to start.   

for x in classes: # prints out the each class name
    print(x) # x is printed variable name chosen to rep the class list names. Much more could be done to diplay.



