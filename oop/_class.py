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

class Animal: # Parent class -- Base class

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # def breathe(self):
    #     return "The animal is breathing."
    # def eat(self):
    #     return "The animal is eating."
    # def sleep(self):
    #     return "The animal is sleeping."

    def breathe(self):
        return f"{self.name} is breathing."
    def eat(self):
        return f"{self.name} is eating."
    def sleep(self):
        return f"{self.name} is sleeping."

class Prey(Animal): # Parent class
    def flee(self):
        return "The prey is fleeing."

class Predator(Animal): # Parent class
    def hunt(self):
        return "The predator is hunting."

class Rabbit(Prey): # Child class
    def eat_grass(self):
        return "The rabbit is eating grass."

class Hawk(Predator): # Child class
    def eat_meat(self):
        return "The hawk is eating meat."

class Fish(Prey, Predator): # Child class
    def eat_fish(self):
        return "The fish is being eaten."
    def hunt_fish(self):
        return "The fish is hunting a smaller fish."