from enemy import *

orc = Enemy() # This is a constructor.

orc.type_of_enemy = "Orc"

# print(f"The type of enemy is {enemy.type_of_enemy} and it has {enemy.enemy_health} health points and does {enemy.enemy_damage} damage points.")

# ABSTRACTION 

"""
1. It allows us to not worry about the details of the implementation of a class.
2. You can create simple and reusable code.
3. Allows for a better use of DRY principle (Don't Repeat Yourself).
4. Enables python object to be more scalable.
"""

print(orc.walk())

