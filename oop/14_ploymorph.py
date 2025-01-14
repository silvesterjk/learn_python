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