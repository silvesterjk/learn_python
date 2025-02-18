"""
Flow Control: If, Elif, Else
"""

x = 10

if x > 5:
    print("x is greater than 5")
elif x == 5:
    print("x is equal to 5")
else:
    print("x is less than 5")

"""
Flow Control: For Loops
"""

mylist = [1, 2, 3, 4, 5]

for item in mylist: # Used to iterate over a sequence (a list, a tuple, a dictionary, a set, or a string).
    print(item)
    # 1
    # 2
    # 3
    # 4
    # 5

for x in range(2, 5): # Used to iterate over a sequence of numbers
    print(x)
    # 2
    # 3
    # 4

for x in range(2, 10, 2): # Used to iterate over a sequence of numbers with a step
    print(x)
    # 2
    # 4
    # 6
    # 8

for x in mylist:
    sum = x + 1
    print(sum)
    # 2
    # 3
    # 4
    # 5
    # 6

"""
Flow Control: While Loops
"""

x = 0

while x < 5: # Used to execute a block of code as long as a condition is true.
    print(x)
    x += 1
    # 0
    # 1
    # 2
    # 3
    # 4

# While if else 

x = 0

while x < 5:
    print(x)
    x += 1
    if x == 3:
        break
    else:
        print("x is not equal to 3")
    # 0
    # 1
    # 2

"""
Object Oriented Programming: Classes and Objects
"""

# We can define an object with either based on its behavior or its state.

# Class based on behavior
class Dog:
    def bark(self):
        print("Woof!") # Behavior of a dog object

# Class based on state
class Dog:
    def __init__(self, name):
        self.name = name # State of a dog object

dog = Dog("Buddy")
print(dog.name) # Buddy 

# Four pillars of object-oriented programming: Encapsulation, Inheritance, Polymorphism, and Abstraction.


