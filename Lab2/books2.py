# alternate version:
'''Dan Smestad 2905 Capstone
Part 2: Author class - no duplicate books
Start with the program from part 1.
In this version, an author can't publish two books with the same name.
When the publish function is called, print an error message if the book 
given has the same name as a book currently in the books list. 
(In other words, make sure the Author object's book list doesn't already contain that name).
'''

class Aurthor:
    
    def __init__(self, name):#initilized object, name instant variable.
        self.name = name     #setting the object parameters
        self.books = set()   #empty set

    def publish(self, title):        
        self.books.add(title) #appending to the books list.

    def __str__(self):      #data = a or b = truthy a falsy b is set. # does the same as above less code more consice
        titles = ', '.join(self.books) or 'No published books' # empty:str/List/None are false/falsy.
        return f'Name: {self.name} Books Published: {titles}' 


        

question_bank = {"art": {"questions": 
["Who painted the Mona Lisa?","What precious stone is used to make the artist\'s pigment ultramarine?",
"Anish Kapoor\'s bean-shaped Cloud Gate scuplture is a landmark of which city?"],
"correct_answers" : ["Leonardo Da Vinci","Lapiz lazuli","Chicago"]},
"Space": {"questions":
["Which planet is closest to the sun?", 
"Which planet spins in the opposite direction to all the others in the solar system?",
"How many moons does Mars have?"],
"correct_answers": ["Mercury" ,"Venus","two"]}}    

question_bank["hockey"] = {"questions", "correct_answers"}#add new pair to existing dictionary.
question_bank['question'] = 8; # update existing entry
question_bank['hockey'] = "what do the letters NHL stand?"; # Add new entry    

def main ():
    rowling = Aurthor('J.K Rowling') #creates name of an aurthor.
    rowling.publish('Harry Potter books 1')  #aurthors book titles.
    rowling.publish('Harry Potter books 2')
    rowling.publish('Harry Potter books 3')
    rowling.publish('Harry Potter books 1') #duplicate we want to remove set will do that.
    rowling.publish('Fantsic Beasts and where to find them')

    print(rowling) #print statement for the variable list name. 

    dan = Aurthor('Dan') # new name added, will use our  calss for formatting new obeject.
    dan.publish('USCHOL Hockey Journal')
    print(dan)#print statement for the variable list name. 

    for key, value in question_bank.items():
        print(f'{value}')
    


    # print "dict[]: ", dict[]
    # print "dict[]: ", dict[]
    
main()    