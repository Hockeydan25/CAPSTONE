"""# dan Smestad video instructions lab2 
Part 1: Author class
Create a new class called Author.
An Author has a name, and a list of books published.
When you create a new Author, they don't have any books. So create an empty books list attribute in the __init__ method.
Your Author class should have a publish method, which takes the title of a book as an argument. Add the title of this book to this object's books list.
Add a __str__ method that returns a String with the author's name, and the names of all of their book's titles.
Write a main function to test your class, create some example authors, and publish some example books."""

# class Aurthor:
#     def __init__(self, name):
#         self.name = name
#         self.books = [] # empty list 

#     def publish(self, title):
        
#         self.books.append(title) #appending to the books list.

#     def __str__(self):
#         if self.books:
#             books_list = ', '.join(self.books) # create a join of books publish.here 
#         else:
#             books_list = 'No Books Published'      
#         #books_list  = ', '.join(self.books) # create a join of books publish.
#         return f'Name: {self.name} Books Published: {books_list}'        

# shakespeare = Aurthor('William Shakespeare') 
# shakespeare.publish('Hamlet')
# shakespeare.publish('RichardIII')

# print(shakespeare)

# dan = Aurthor('Dan')
# print(dan)

# alternate version:
'''Part 2: Author class - no duplicate books
Start with the program from part 1.
In this version, an author can't publish two books with the same name.
When the publish function is called, print an error message if the book given has the same name as a book currently in the books list. (In other words, make sure the Author object's book list doesn't already contain that name).
'''

class Aurthor:
    def __init__(self, name):
        self.name = name
        self.books = [] # empty list 

    def publish(self, title):        
        self.books.append(title) #appending to the books list.

    def __str__(self):      #data = a or b = truthy a falsy b is set. # does the same as above less code more consice
        titles = ', '.join(self.books) or 'No published books' # empty:str/List/None are false/falsy.
        return f'Name: {self.name} Books Published: {titles}' 

def main ():
    rowling = Aurthor('J.K Rowling')
    rowling.publish('Harry Potter books 1')
    rowling.publish('Fantsic Beasts and where to find them')
    print(rowling)

    dan = Aurthor('Dan')
    dan.publish('USCHOL Hockey Journal')
    print(dan)

main()    

