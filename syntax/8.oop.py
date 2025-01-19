"""1. Introduction to Object-Oriented Programming:
OOP allows developers to model real-world entities as objects in code, encapsulating data (attributes) and functions (methods) that operate on that data. 
This approach promotes modularity, reusability, and organization in software development.
"""

"""2. Defining Classes and Creating Objects:
A class serves as a blueprint for creating objects, defining the attributes and methods common to all objects of that type. An object is an instance of a class."""

# Here, Student is a class with an initializer method __init__ that sets the name and house attributes for each student object.
class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

"""3. Creating and Using Objects

Once a class is defined, objects can be instantiated and their attributes accessed or modified."""

student = Student("Harry", "Gryffindor")
print(student.name)  # Outputs: Harry
print(student.house)  # Outputs: Gryffindor

"""4. Adding Methods to Classes

Methods are functions defined within a class that describe the behaviors of an object."""

class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    def introduce(self):
        return f"My name is {self.name} and I belong to {self.house} house."

# Now, each Student object has an introduce method:

student = Student("Hermione", "Gryffindor")
print(student.introduce())  # Outputs: My name is Hermione and I belong to Gryffindor house.

"""5. Encapsulation and Data Validation

Encapsulation restricts direct access to an object's attributes to prevent unintended modifications. 
This can be achieved by defining methods that control how attributes are accessed or modified.
In this example, the `Student` class includes getter and setter methods to validate and encapsulate the `name` and `house` attributes."""

class Student:
    def __init__(self, name, house):
        self.name = name  # Uses the setter
        self.house = house  # Uses the setter

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name

    @property
    def house(self):
        return self._house

    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house

""" Equally correct way to implement this: 

class Student:
    def __init__(self, name, house):
        self.name = name  # Uses the setter
        self.house = house  # Uses the setter

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name

    @property
    def house(self):
        return self._house

    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house

Here: In this example, the Student class includes getter and setter methods to validate and encapsulate the name and house attributes.

"""


