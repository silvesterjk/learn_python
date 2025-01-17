# Aggregation represents a relationshios where one object is composed of multiple objects. It is a "has-a" relationship.

"""
class Library:
    pass

class Book:
    pass
"""

# Here the Library class has a list of Book objects. This is an example of aggregation.
# They can exist independently of each other. The Library class can exist without the Book class and vice versa.
# This is the difference between aggregfation and composition. In composition, the objects are dependent on each other.


class Library:
    def __init__(self, name):
        self.name = name

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

library = Library("Central Library")
book1 = Book("The alchemist", "Paulo Coelho")
book2 = Book("The song of ice and fire", "George R. R. Martin")
book3 = Book("The similarion", "J. R. R. Tolkien")