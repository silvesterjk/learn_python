# DECORATORS
# There are two types of decorators in Python: function decorators and class decorators.
# Function Decorators: Modify the behavior of a function or a method.
# Class Decorators: Modify the behavior of a class.
# Decorators are used to modify the behavior of functions or methods. They are used to add functionality to existing functions or methods without changing their structure.

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

def start_end_decorator(func):
    def wrapper():
        print("Start")
        func()
        print("End")
    return wrapper

def say_hello():
    print("Hello!")

say_hello = my_decorator(say_hello)
say_hello()