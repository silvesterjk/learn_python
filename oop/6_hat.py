# class methods are bound to the class, not the object. They can access and modify class state.
# Static methods are not bound to the class or object. They are used for utility functions that do not modify class state.
import random

class Hat:

    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"] # class attribute/variable. Can be accessed using Hat.houses

    @classmethod
    def sort(cls, name): # cls is a reference to the class. We use this because we are working with the class, not the object.
        print(f"{name} is sorted into {random.choice(cls.houses)} house.")

# The following would allow us to instantiate the class multiple times.
# hat = Hat()
# hat.sort("Harry Potter")

# The following would allow us to call the class method without instantiating the class.
Hat.sort("Harry Potter") # This is the preferred way of calling class methods.
 
# This logic can be written in a function as well.

houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

def sort(name):
    print(f"{name} is sorted into {random.choice(houses)} house.")

sort("Harry Potter")

# Which to use when depends on the context. If the method is related to the class, use a class method. If it is not, use a function.