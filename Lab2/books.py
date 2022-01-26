"""# dan Smestad video instructions lab2 
Part 1: Author class
Create a new class called Author.
An Author has a name, and a list of books published.
When you create a new Author, they don't have any books. So create an empty books list attribute in the __init__ method.
Your Author class should have a publish method, which takes the title of a book as an argument. Add the title of this book to this object's books list.
Add a __str__ method that returns a String with the author's name, and the names of all of their book's titles.
Write a main function to test your class, create some example authors, and publish some example books."""

class Aurthor:
    def __init__(self, name): #initilized object, name instant variable.
        self.name = name         #setting the object parameters.
        self.books = [] # empty list. 

    def publish(self, title):
        
        self.books.append(title) #appending to the books list.

    def __str__(self):
        if self.books:
            books_list = ', '.join(self.books) # create a join of books publish.here 
        else:
            books_list = 'No Books Published'      
        #books_list  = ', '.join(self.books) # create a join of books publish.
        return f'Name: {self.name} Books Published: {books_list}'        
    


            
shakespeare = Aurthor('William Shakespeare') #creates name of an aurthor.
shakespeare.publish('Hamlet') #creates tittle for books.
shakespeare.publish('RichardIII')

print(shakespeare)#print statement for the variable list name .

dan = Aurthor('Dan') #creates name of an aurthor.
print(dan)#print statement for the variable list name .


