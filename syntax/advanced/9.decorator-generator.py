# DECORATORS
# There are two types of decorators in Python: function decorators and class decorators.
# Function Decorators: Modify the behavior of a function or a method.
# Class Decorators: Modify the behavior of a class.
# Decorators are used to modify the behavior of functions or methods. They are used to add functionality to existing functions or methods without changing their structure.
# Functions in python are first-class objects. This means that functions can be passed as arguments to other functions, returned as values from other functions, and assigned to variables.
# A decorator is a function that takes another function as an argument and returns a new function. The @ symbol is used to apply a decorator to a function.
"""
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper
"""
def start_end_decorator(func):
    def wrapper():
        print("Start")
        func()
        print("End")
    return wrapper

def say_hello():
    print("Hello man!")

say_hello = start_end_decorator(say_hello)
say_hello() # This will print:

"""
Start
Hello man
End
"""

# This is the same as:
@start_end_decorator
def say_hello():
    print("Hello man") # THis will print:

"""
Start
Hello man
End
"""

# Decorators with arguments
# Decorators can also take arguments. To do this, we need to add another layer of functions.