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

"""6. Inheritance

Inheritance allows a new class (subclass) to acquire the properties and methods of an existing class (superclass), promoting code reuse.

Here, Student inherits from Person, reusing the name attribute and adding a new house attribute."""

class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, house):
        super().__init__(name)
        self.house = house

"""7. Class Methods and Static Methods

Class Methods: Operate on the class itself rather than instances. Defined using the @classmethod decorator.

Static Methods: Do not operate on the class or its instances. Defined using the @staticmethod decorator."""

class School:
    students = []

    @classmethod
    def add_student(cls, student):
        cls.students.append(student)

    @staticmethod
    def school_motto():
        return "Knowledge is power."


"""8. Operator Overloading

Operator overloading allows defining how operators behave with objects of a class."""

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

# This enables the use of the + operator to add two Vector objects.

v1 = Vector(2, 4)
v2 = Vector(1, 3)
v3 = v1 + v2 # v3 = v1.__add__(v2) --> (3, 7) that is (x, y)
print(v3.x)  # Outputs: 3 --> Here we're calling the x attribute of the v3 object.

"""
# Because we defined the __add__ method, the + operator can be used to add two Vector objects.
# The resulting Vector object has x = 2 + 1 = 3 and y = 4 + 3 = 7.
# The __add__ method returns a new Vector object with these values.
# The resulting Vector object is stored in v3, and its x attribute is printed.

"""


# COMPOSITION

"""
1. Composition is a way to combine objects or classes together.
2. Composition is a way to create complex objects.
3. Composition is a way to create a has-a relationship.
4. Composition is a way to create a part-of relationship.
5. Composition is a way to create a whole-part relationship.
"""

