class Car:

    wheels = 4 # Class variable

    def __init__(self, model, year, colour, for_sale):
        self.model = model
        self.year = year
        self.colour = colour
        self.for_sale = for_sale

    def __str__(self):
        return f"Is the {self.year} {self.colour} {self.model} for sale? : {self.for_sale}."
    
    def drive(self):
        return f"{self.model} is driving with {Car.wheels} wheels."  
        # Here we are accessing the class variable using the class name.
        # This is because the class variable is shared among all instances of the class. 
        # And best practice is to access class variables using the class name.
    
    def description(self):
        return f"{self.year} {self.colour} {self.model} is a car for sale."
    
# Inheritance. A --> B(A), C(A), D(A)

class Animal: 
    ...

class Dog(Animal): 
    ...

class Cat(Animal): 
    ...

class Bird(Animal): 
    ...


# Multiple Inheritance --> Inherit from more than one parent class. C(A, B)

# Multi Level Inheritance --> Inherit from a parent class which is inherited from another parent class. C(B) < B(A) < A