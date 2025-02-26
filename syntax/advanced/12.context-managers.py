"""SHALLOW VS DEEP COPYING"""

org = [0, 1, 2, 3, 4]
cpy = org
cpy[0] = -10
print(cpy) # This will print: [-10, 1, 2, 3, 4]
print(org) # This will print: [-10, 1, 2, 3, 4]

# Shallow Copy vs Deep Copy
"""
1. Shallow Copy: A shallow copy creates a new object but does not create new objects for the nested objects.
2. Deep Copy: A deep copy creates a new object and creates new objects for the nested objects.
3. The copy module in Python provides functions for shallow and deep copying.
4. The copy.copy() function creates a shallow copy.
5. The copy.deepcopy() function creates a deep copy.
"""
# Shallow Copy
import copy
org = [0, 1, 2, 3, 4]
cpy = copy.copy(org)
# cpy = org.copy() --> This is another way to create a shallow copy
# cpy = org[:] --> This is another way to create a shallow copy
# cpy = list(org) --> This is another way to create a shallow copy

cpy[0] = -10
print(cpy) # This will print: [-10, 1, 2, 3, 4]
print(org) # This will print: [0, 1, 2, 3, 4]

# Deep Copy
org = [[0, 1], [2, 3]] # This is a nested list
cpy = copy.deepcopy(org)
cpy[0][0] = -10
cpy[1][0] = 2
print(cpy) # This will print: [[-10, 1], [2, 3]]
print(org) # This will print: [[0, 1], [2, 3]]

"""Implementing this with a class"""

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __copy__(self):
        return Point(self.x, self.y)
    
    def __deepcopy__(self, memo): # memo is a dictionary that stores the original object and the copied object to avoid infinite recursion.
        return Point(copy.deepcopy(self.x, memo), copy.deepcopy(self.y, memo))
    
org = Point(0, 0)
cpy = copy.copy(org)
cpy.x = -10
print(cpy) # This will print: Point(-10, 0)
print(org) # This will print: Point(0, 0)

org = Point(Point(0, 0), Point(1, 1))
cpy = copy.deepcopy(org)
cpy.x.x = -10
cpy.y.x = 2
print(cpy) # This will print: Point(Point(-10, 0), Point(2, 1))
print(org) # This will print: Point(Point(0, 0), Point(1, 1))

 
"""
CONTEXT MANAGERS
1. Context managers are objects that manage resources.
2. The with statement is used to create a context manager.
3. Context managers can be created using classes or functions.
4. Context managers are used to allocate and release resources.
5. The contextlib module provides utilities for creating context managers.
"""

with open("file.txt", "w") as file:
    file.write("Hello, World!")
"""
1. The with statement is used to create a context manager.
2. The open() function is used to open a file.
3. The file.write() method is used to write to the file.
4. The file is automatically closed when the with block is exited.
"""
file = open("file.txt", "w")
try:
    file.write("Hello, World!")
finally:
    file.close()

# The same can be used for lock in multi threading and to establish DB connections.
# For example:

from threading import Lock
lock = Lock() # This is a lock object
lock.acquire()
try:
    print("Critical section")
finally:
    lock.release()

# -or-

lock = Lock()
with lock:
    print("Critical section")

# ____________________________________________

# The same can be done with a context manager:
with Lock():
    print("Critical section")


# The same can be done with a context manager:
import contextlib  
@contextlib.contextmanager
def my_context_manager():
    print("Enter")
    yield
    print("Exit")

with my_context_manager():
    print("Hello, World!")

# OR

from contextlib import contextmanager

@contextmanager
def my_context_manager(filename):
    """
    1. The yield statement is used to return the resource to be managed.
    2. The resource is assigned to the variable in the with statement.
    3. The resource is returned to the caller.
    4. The resource is closed in the finally block.
    5. The program prints "Enter" when the with block is entered.
    6. The program prints "Exit" when the with block is exited.
    7. The program writes to the file if the filename argument is provided.
    8. The program writes to the file "file.txt" if the filename argument is not provided.
    """
    f = open(filename, "w")
    try:
        print("Enter")
        yield f
    finally:
        print("Exit")
        f.close()

with my_context_manager():
    print("Hello, World!")

with my_context_manager("file.txt") as file:
    file.write("Hello, World!") # This will write to the file "file.txt"

# With a class:

"""
The following can be used in cases where you want to manage a file.
"""

class ManagedFile:
    """
    1. The __enter__ method is called when the with block is entered.
    2. The __exit__ method is called when the with block is exited.
    3. The __exit__ method is called even if an exception is raised.
    """
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        """
        1. The __enter__ method returns the resource to be managed.
        2. The resource is assigned to the variable in the with statement.
        """
        print("Enter")
        self.file = open(self.filename, "w")
        return self.file

    def __exit__(self, exc_type, exc_value, exc_traceback):
        """
        1. The exc_type argument is the exception type.
        2. The exc_value argument is the exception value.
        3. The exc_traceback argument is the exception traceback.
        4. The __exit__ method returns True if the exception has been handled, False otherwise.
        5. If the exception has been handled, the program continues normally.
        6. If the exception has not been handled, the program exits.
        7. The file is closed in the __exit__ method.
        8. The exception is printed if it has been raised.
        9. The program prints "Exit" when the with block is exited.
        """
        if self.file:
            self.file.close()
        if exc_type is not None:
            print (f"Exception has been handled: {exc_type}, {exc_value}")
        # print("Exc:", exc_type, exc_value) -- Or you can print the exception
        print("Exit")

with ManagedFile("file.txt") as file:
    print("Do something here...")
    file.write("Hello, World!")
    file.some_method() # This will raise an AttributeError

print("Continue...")


"""
OUTPUT:

Enter
Do something here...
Exception has been handled: <class 'AttributeError'>, 'TextIOWrapper' object has no attribute 'some_method'
Exit
Continue...
"""
