"""
1. Sets
# A set in Python is an unordered collection of unique elements.
# This code collects unique house names from the list of students and prints them in sorted order.
"""
students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Padma", "house": "Ravenclaw"},
]

houses = set() # Create an empty set to store house names
for student in students:
    houses.add(student["house"]) # Add the house name to the set if it's not already there (unique)

# Output: {'Gryffindor', 'Ravenclaw', 'Slytherin'}

for house in sorted(houses):
    print(house)

# Output: Gryffindor Ravenclaw Slytherin

"""2. Global Variables

# Global variables are defined outside of functions and can be accessed globally. However, modifying them within functions requires the global keyword.
# Using global variables is generally discouraged due to potential unintended side effects.
"""
balance = 0

def deposit(n):
    global balance
    balance += n

def withdraw(n):
    global balance
    balance -= n

"""3. Constants

Constants are variables meant to remain unchanged. By convention, they are named in uppercase letters."""

MEOWS = 3

for _ in range(MEOWS):
    print("meow")

# Output: meow meow meow
# Python does not enforce immutability of constants; it's a convention to indicate that the variable should not be modified.

"""4. Type Hints
# Type hints specify the expected data types of function arguments and return values, aiding in code readability and debugging.
# Tools like mypy can be used to check for type consistency in your code.
"""
def meow(n: int) -> None: # None is used to indicate that the function does not return a value
    for _ in range(n):
        print("meow") # The output will be the same as before. That is meow meow meow.

"""5. Docstrings

# Docstrings provide documentation for modules, classes, and functions, explaining their purpose and usage.
# Docstrings are enclosed in triple quotes and can span multiple lines.
"""

def meow(n: int) -> None:
    """
    Print 'meow' n times.

    :param n: Number of times to meow
    # :param is used to describe the function parameter & n: is the parameter name
    # : is used to describe the function parameter & Number of times to meow is the description
    """
    for _ in range(n):
        print("meow")

"""
6. Argument Parsing with argparse

# The argparse module allows for parsing command-line arguments, enabling dynamic input to programs.
# This script allows the user to specify how many times to print "meow" using the -n flag. 
"""

import argparse

parser = argparse.ArgumentParser(description="Meow like a cat")
parser.add_argument("-n", type=int, default=1, help="number of times to meow") # This line adds an argument -n to the parser. The default value is 1, and the help message describes its purpose.
args = parser.parse_args()

for _ in range(args.n):
    print("meow") 
    # The output will be the same as before. That is meow meow meow. 
    # 3 comes in the output because of the default value of n is 1.

"""
7. Unpacking with *args and **kwargs

*args and **kwargs enable functions to accept an arbitrary number of positional and keyword arguments, respectively.
This function will output the positional and keyword arguments passed to it.
"""

def f(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

f(1, 2, 3, a=4, b=5)

"""8. Functional Programming Tools"""

# map: Applies a function to all items in an input list.

numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)

# List Comprehensions: Provide a concise way to create lists.

squared = [x ** 2 for x in numbers]
print(squared)

# filter: Filters items out of a list.

even = list(filter(lambda x: x % 2 == 0, numbers))
print(even)

# Dictionary Comprehensions: Provide a concise way to create dictionaries.

squared_dict = {x: x ** 2 for x in numbers}
print(squared_dict)

# enumerate: Adds a counter to an iterable.

for index, value in enumerate(numbers):
    print(f"Index: {index}, Value: {value}")

for index, value in enumerate(numbers, start=1):
    print(f"Index: {index}, Value: {value}")