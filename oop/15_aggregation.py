# Aggregation represents a relationshios where one object is composed of multiple objects. It is a "has-a" relationship.

"""
class Library:
    pass

class Book:
    pass
"""

# Here the Library class has a list of Book objects. This is an example of aggregation.
# They can exist independently of each other. The Library class can exist without the Book class and vice versa.
# This is the difference between aggregation and composition. In composition, the objects are dependent on each other.

class Library:
    def __init__(self, name):
        self.name = name # attribute to store the name of the library
        self.books = []  # attribute to store the list of books
    
    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        for index, book in enumerate(self.books):
            print( f'{index}. {book.title} by {book.author}')


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

library = Library("Central Library")
book1 = Book("The alchemist", "Paulo Coelho")
book2 = Book("The song of ice and fire", "George R. R. Martin")
book3 = Book("The similarion", "J. R. R. Tolkien")


library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# The Library class has a list of Book objects. This is an example of aggregation.
# The Book object can exist independently of the Library object. The Library object can exist without the Book object.
library.display_books()
