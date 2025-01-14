# super() = function that allows us to call a method from the parent class
# Allowes us to call the __init__ method of the parent class and extend the functionality of the inherited methods.

class Shape:
    
    def __init__(self, colour, filled):
        self.colour = colour
        self.filled = filled
    
    def colour(self):
        return f"The colour is {self.colour} and the fill state is state: {'filled' if self.filled else 'not filled'}"

class Circle(Shape):
    
    def __init__(self, radius, colour, filled):
        super().__init__(colour, filled)
        self.radius = radius

    def area(self):
        return f"The area is {3.14159 * self.radius ** 2}"
    
    def circumference(self):
        return f"The circumference is : {2 * 3.14159 * self.radius} | Of Colour: {self.colour} and the state: {self.filled}"

class Square(Shape):
    
    def __init__(self, side, colour, filled):
        super().__init__(colour, filled, )
        self.side = side
        
    def area(self):
        return self.side ** 2
    
    def perimeter(self):
        return f" The perimeter is of {4 * self.side} and of Colour: {self.colour} and the state: {self.filled}"

class Triangle(Shape):
    
    def __init__(self, base, height, colour, filled):
        super().__init__(colour, filled)
        self.base = base
        self.height = height
        
    def area(self):
        return 0.5 * self.base * self.height
    
    def perimeter(self):
        return f" The perimeter is of {self.base + 2 * self.height} and of Colour: {self.colour} and the state: {self.filled}"
    
# Create an instance of the Circle class
Circle1 = Circle(5, "Red", True)
Circle2 = Circle(radius=10, colour="Blue", filled=False)

print(Circle1.__dict__)
print(Circle1.area())
print(Circle1.circumference())

# Create an instance of the Square class
Square1 = Square(5, "Green", True)
Square2 = Square(10, "Yellow", False)

print(Square1.__dict__)
print(Square1.area())
print(Square1.perimeter())

# Create an instance of the Triangle class
Triangle1 = Triangle(5, 10, "Purple", True)
Triangle2 = Triangle(10, 20, "Orange", False)

print(Triangle1.__dict__)
print(Triangle1.area())
print(Triangle1.perimeter())
