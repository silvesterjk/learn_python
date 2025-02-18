from enemy import *

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

# INHERITANCE

