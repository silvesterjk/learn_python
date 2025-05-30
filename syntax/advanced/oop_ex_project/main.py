from enemy import *
from zombie import *
from orge import *

orc = Enemy("Orc", 20, 5) # This is an instance of the class Enemy. Example of a constructor.

# print(f"The type of enemy is {enemy.type_of_enemy} and it has {enemy.enemy_health} health points and does {enemy.enemy_damage} damage points.")

# ABSTRACTION 

"""
1. It allows us to not worry about the details of the implementation of a class.
2. You can create simple and reusable code.
3. Allows for a better use of DRY principle (Don't Repeat Yourself).
4. Enables python object to be more scalable.
"""

print(orc.walk())

print(orc.attack())

print(orc.talk())

# CONSTRUCTOR

"""
1. A constructor is a special method that is called when an object is created.
2. There are 4 types of constructors in Python:
    - Default/Empty constructor
    - Parameter constructor
    - No Argument constructor

    A. Default constructor is the one that doesn't take any arguments.
        - Example code: 
            def __init__(self):
                pass
    B. Parameter constructor is the one that takes arguments.
        - Example code:
            def __init__(self, name, age):
                self.name = name
                self.age = age
    C. No Argument constructor is the one that takes no arguments.
        - Example code:
            def __init__(self):
                print("Enemy has been created.")
            def talk(self):
                return "I am an enemy."
"""

orc = Enemy("Orc", 20, 5) # This is an instance of the class Enemy. Example of a constructor.
big_orc = Enemy("Big Orc", 30, 10) # This is an instance of the class Enemy. Example of a constructor.

# ENCAPSULATION

"""
1. Encapsulation is a way to restrict access to some parts of an object.
2. It bundles the data (attributes) and the methods (functions) that operate on the data into a single unit.
3. It is used to prevent the accidental modification of data.
4. It is used to hide the data from the outside world.
5. The following are public variables: --> They are accessible from outside the class.
    - self.type_of_enemy
    - self.enemy_health
    - self.enemy_damage
6. The following are private variables: --> They are not accessible from outside the class.
    - self.__type_of_enemy
    - self.__enemy_health
    - self.__enemy_damage
7. The following are protected variables: --> They are accessible from outside the class but only in a subclass.
    - self._type_of_enemy
    - self._enemy_health
    - self._enemy_damage

8. Getter and Setter methods are used to access and modify the private variables.
9. Getter methods are used to access the private variables.
10. Setter methods are used to modify the private variables.
11. The following are getter methods:
    - def get_type_of_enemy(self):
        return self.__type_of_enemy
    - def get_enemy_health(self):
        return self.__enemy_health
    - def get_enemy_damage(self):
        return self.__enemy_damage
12. The following are setter methods:
    - def set_type_of_enemy(self, type_of_enemy):
        self.__type_of_enemy = type_of_enemy
    - def set_enemy_health(self, enemy_health):
        self.__enemy_health = enemy_health
    - def set_enemy_damage(self, enemy_damage):
        self.__enemy_damage = enemy_damage
"""
orc_type = orc.get_the_type_of_enemy()
print(f"The type of enemy is {orc_type}.")

# INHERITANCE

"""
1. Inheritance is a way to form new classes using classes that have already been defined.
2. The new classes, known as derived classes, inherit attributes and methods from the base class.
3. The derived class can also override the base class methods.
4. The derived class can also have new methods.
5. The derived class can also have new attributes.
6. The derived class can also have new constructors.
7. The derived class can also have new getter and setter methods.
8. The derived class can also have new private, public and protected variables.
9. The derived class can also have new public methods.

-- Method overriding is when a method in a derived class has the same name, same parameters or signature and same return type as a method in the base class.
-- Method overloading is when a method in a derived class has the same name but different parameters or signature as a method in the base class.


10. The following are the types of inheritance:
    - Single Inheritance
    - Multiple Inheritance
    - Multilevel Inheritance
    - Hierarchical Inheritance
    - Hybrid Inheritance

11. Single Inheritance is when a class inherits from only one class.
12. Multiple Inheritance is when a class inherits from more than one class.
13. Multilevel Inheritance is when a class inherits from a class which in turn inherits from another class.
14. Hierarchical Inheritance is when more than one class inherits from a single class.
15. Hybrid Inheritance is when a class is derived from two or more classes.

Examples of inheritance:
    - class DerivedClassName(BaseClassName):
        pass
    - class DerivedClassName(BaseClassName1, BaseClassName2):
        pass
    - class DerivedClassName(BaseClassName1, BaseClassName2, BaseClassName3):
        pass

"""

# POLYMORPHISM

"""
1. Polymorphism is the ability to present the same interface for different data types.
2. Polymorphism allows methods to do different things based on the object it is acting upon.
3. Polymorphism is a way to make the code more scalable.
4. Polymorphism is a way to make the code more reusable.

For example:
    - The + operator is used to add two numbers and concatenate two strings.
    - The * operator is used to multiply two numbers and repeat a string multiple times.
"""

# SELF VS. SUPER

"""
1. self is a reference to the current instance of the class.
2. self is used to access the attributes and methods of the class.
3. Super is a reference to the parent class.
4. Super is used to call the constructor and methods of the parent class.
"""

# INHERITENCE

zombie = Zombie(30, 10) # This is an instance of the class Zombie. Example of a constructor.

print(zombie.get_the_type_of_enemy()) # This is a method in the Enemy class.
print(zombie.talk()) # Method overide
print(zombie.spread_infection()) # This is a new method in the Zombie class.

# POLYMORPHISM

"""
1. Polymorphism is the ability to present the same interface for different data types.
2. Polymorphism allows methods to do different things based on the object it is acting upon.
3. Polymorphism is a way to make the code more scalable.
4. Polymorphism is a way to make the code more reusable.
"""

def battle(e: Enemy): # e: Enemy means --> e is an instance of the class Enemy
    e.attack()
    e.talk()


zombie = Zombie(10,1)
orge = Orge(20, 5)

battle(zombie)
battle(orge)


# COMPOSITION

"""
1. Composition is a way to combine objects or classes together.
2. Composition is a way to make the code more scalable, reusable and maintainable.
3. HAS-A and IS-A are two types of relationships in object-oriented programming.
4. HAS-A : A car has an engine but an engine does not have a car.
5. IS-A : A car is a vehicle.
"""

# COMPOSITION EXAMPLE

class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def start(self):
        return "Engine has started."

    def stop(self):
        return "Engine has stopped."
    
    def accelerate(self):
        return "Engine is accelerating."
    
    def decelerate(self):
        return "Engine is decelerating."

class Car:
    def __init__(self, make, model, year, engine):
        self.make = make
        self.model = model
        self.year = year
        self.engine = engine

    def start(self):
        return self.engine.start()

    def stop(self):
        return self.engine.stop()
    
    def accelerate(self):
        return self.engine.accelerate()
    
    def decelerate(self):
        return self.engine.decelerate()

engine = Engine(200)
car = Car("Toyota", "Corolla", 2022, engine)

print(car.start()) # Engine has started.
print(car.accelerate()) # Engine is accelerating.
print(car.decelerate()) # Engine is decelerating.
print(car.stop()) # Engine has stopped.