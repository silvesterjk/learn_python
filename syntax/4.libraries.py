"""1. Modules and the import Statement

Python's functionality can be extended by importing modules, which are files containing Python code. You can import an entire module or specific functions from it.

Importing an entire module:"""

import random

number = random.randint(1, 10)
print(number)

# Importing a spectific function from a module:

from random import choice

color = choice(['red', 'blue', 'green'])
print(color)

"""2. The random Module

The random module provides functions to generate random numbers and make random selections."""

# random.choice(seq): Returns a random element from the non-empty sequence seq.

import random

coin = random.choice(['heads', 'tails'])
print(coin)

# random.randint(a, b): Returns a random integer N such that a <= N <= b.

import random

number = random.randint(1, 6)
print(number)

# random.shuffle(x): Shuffles the sequence x in place.

import random

cards = ['jack', 'queen', 'king']
random.shuffle(cards)
print(cards)

"""3. The statistics Module

The statistics module provides functions for mathematical statistics of numeric data.

statistics.mean(data): Returns the arithmetic mean of the data."""

import statistics

average = statistics.mean([100, 90, 80])
print(average)


"""4. Command-Line Arguments with the sys Module

The sys module allows interaction with the Python interpreter, including accessing command-line arguments.

This script expects exactly one command-line argument and greets the user by name."""

import sys

if len(sys.argv) != 2:
    sys.exit("Usage: python program.py <name>")

name = sys.argv[1]
print(f"Hello, {name}")

"""5. Slicing Lists

Slicing allows you to access a subset of elements from a list."""

# list[start:end]

names = ['Alice', 'Bob', 'Charlie', 'David']
print(names[1:3])  # Outputs: ['Bob', 'Charlie'] |  This retrieves elements from index 1 up to, but not including, index 3.

"""
6. Packages and pip

Packages are collections of modules. Python's Package Index (PyPI) hosts thousands of third-party packages. You can install packages using pip.

"""

# pip install cowsay

import cowsay

cowsay.cow("Hello, world!")


"""7. APIs and the requests Module

APIs (Application Programming Interfaces) allow interaction with external services. The requests module enables sending HTTP requests in Python."""

import requests

response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=weezer")
data = response.json()
print(data)

# This sends a GET request to the iTunes API and prints the JSON response.

"""8. Creating Your Own Modules

You can create reusable modules by writing functions in a separate .py file and importing them.

Example:

Create a file helpers.py:"""

def greet(name):
    return f"Hello, {name}!"

# In your main program:

from helpers import greet

print(greet("Alice"))