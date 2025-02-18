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
    For example:
        class Enemy:
            def __init__(self, type_of_enemy, enemy_health=10, enemy_damage=5):
                self.__type_of_enemy: str = type_of_enemy
                self.enemy_health: int = enemy_health
                self.enemy_damage: int = enemy_damage

            def talk(self):
                print(f'I am a {self.__type_of_enemy}. I will kill you') 

12. Multiple Inheritance is when a class inherits from more than one class.
    For example:
        
"""