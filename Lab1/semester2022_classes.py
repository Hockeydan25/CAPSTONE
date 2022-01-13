#Lab1 Dan Smestad ITEC 2905-80 Software Dev. Capstone Clara James.
# Write a program that asks for the names of all of the classes you are taking this semester
# Save these class names in a list. while loop
# Print all the items in the list, one per line.

classes = []
class_number = int(input('How Many classes are you taking this semester? '))

while True:
    class_name = input('Enter the name of the class, or enter to quit: ') 
    if not class_name:
        break
    classes.append(class_name)    

for x in classes: # prints out the each class name
    print(x)



