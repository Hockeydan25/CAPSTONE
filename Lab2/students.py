"""dan Smestad video instructions lab2 ;
Part 3: Student dataclass
Type in the dataclass code from the slides/video. You would have done this before class.
Add one more field: gpa, a float.
Write a main function to create some example Student objects with some example names, college_id and GPA values. 
Verify you can read the name, college ID and GPA for an example student.  Verify when you print an example student, the GPA is included. 
Add some comments in your code to compare the dataclass version to the "traditional" version."""
from dataclasses import dataclass

@dataclass # decorator
class Student: #initilized object, name instant variable.
    name: str
    school_id: str
    gpa: dict

    def __str__(self):            #function to an override to cleanup how the out put looks.
        return f'Student name: {self.name}, ID: {self.school_id}, GPA: {self.gpa}'

def main(): #function main
    alex = Student('Alex','abcdef', 3.7) # Alex as argument passed to alex or name parameter.
    print(alex.name)
    print(alex.school_id)
    print(alex)# prints just that was have an object item.

    sam = Student ('Sam', 'asdff', 3.5)# another new student calling the __str__ method.
    print(sam.name)# testing print.
    print(sam)    

main() # this main method must be after because it is a call to main method.

# first version without data classes:

# class Student: #class student storing the funtcions creating new objects and storing data for students.
#     def __init__(self, name, school_id, gpa):  #initilized object, name instant variable.
#         self.name = name
#         self.school_id = school_id
#         self.gpa = gpa
#     def __str__(self):                  # needs to be duble underscore. I mistyped with singles _.
#         return f'Student name: {self.name}, ID: {self.school_id}, GPA: {self.gpa}'


# alex = Student('Alex','abcdef', 4.0) # Alex as argument passed to alex or name parameter.
# print(alex.name)
# print(alex.school_id)
# print(alex)# prints just that was have an object item.

# sam = Student ('Sam', 'asdff', 3.5)# new student calling the __str__ method.
# print(sam.name)# testing print.
# print(sam)

# new_gpa = alex[2](2.5)
# print(alex.gpa)

