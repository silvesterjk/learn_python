# Polimorphism = many forms
# Polymorphism is an ability (in OOP) to use a common interface for multiple forms (data types).
# Suppose, we need to color a shape, there are multiple shapes (circle, square, triangle, etc).
# However we could use the same method to color any shape. This concept is called Polymorphism.
# Polymorphism is based on the greek words Poly (many) and morphism (forms).

# Two was to achieve polymorphism:
# 1. Duck Typing = Objects of different classes are able to be used interchangeably if they have the same method names.
# 2. Inheritance = Inheritance allows us to define a class that inherits all the methods and properties from another class.

"""
class Shape:
    pass

class Circle(Shape):
    pass
    
A Circle is a shape. And it is itself a circle. Thus carrying two forms.

"""

# Inheritance Polymorphism

from abc import ABC, abstractmethod # To work with abstract classes.

class Shape:
    @abstractmethod
    def area(self):
        pass
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

class Pizza(Circle):
    # Pizza is a circle with a topping. And circle is a shape.
    # Hence the pizaa has three forms. Circle, Shape, Pizza.
    def __init__(self, topping, radius):
        super().__init__(radius)
        self.topping = topping

    # def area(self):
    #     return 3.14159 * self.radius ** 2    

# Create instances of the classes
shapes = [Circle(5), Square(10), Triangle(5, 10), Pizza("Pepperoni", 5)]
# We can make it a dictionary to store the shapes and their areas.
shapes_dict = {"Circle": Circle(5), "Square": Square(10), "Triangle": Triangle(5, 10), "Pizza": Pizza("Pepperoni", 5)}

for shape in shapes:
    print(f"{shape.area()} cm squared")

# We can call the dictionary to get the area of a specific shape.
for key, value in shapes_dict.items(): # items() returns a list of tuples.
    print(f"The area of the {key} is {value.area()}")

# or 

for shape in shapes_dict:
    print(f"This is a {shapes_dict[shape].__class__.__name__}")
    print(f"The area of the {shape} is {shapes_dict[shape].area()}") 
    # In the above line: shapes_dict[shape] returns the object of the shape class.
    # .area() calls the area method of the object of the shape class. Returns the area of the shape.
    # shape is the key of the dictionary. It is the name of the shape.


# Duck Typing Polymorphism
# Duck typing is a concept related to dynamic typing, where the type or the class of an object is less important than the methods it defines.
# When you use duck typing, you do not check types at all. Instead, you check for the presence of a given method or attribute.
# If a method or attribute is present, the object is considered to be of the type you need.
# Object must have the minimum required methods or attributes to be considered as the required type.
# If it looks like a duck, swims like a duck, and quacks like a duck, then it probably is a duck.

class Animal:
    alive = True

class Dog(Animal):
    def speak(self):
        return "Woof!"
    
class Cat(Animal):
    def speak(self):
        return "Meow!"
    
class Car:
    # def sound(self):
    def speak(self):
        return "Vroom!"
    
animals = [Dog(), Cat(), Car()]

for animal in animals:
    # print(animal.speak())
    # The above line will return an error for the Car class as it does not have the speak method and for sound instead.
    # AttributeError: 'Car' object has no attribute 'speak'
    print(animal.speak())