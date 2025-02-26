# DECORATORS
# There are two types of decorators in Python: function decorators and class decorators.
# Function Decorators: Modify the behavior of a function or a method.
# Class Decorators: Modify the behavior of a class.
# Decorators are used to modify the behavior of functions or methods. They are used to add functionality to existing functions or methods without changing their structure.
# Functions in python are first-class objects. This means that functions can be passed as arguments to other functions, returned as values from other functions, and assigned to variables.
# A decorator is a function that takes another function as an argument and returns a new function. The @ symbol is used to apply a decorator to a function.

"""FUNCTION DECORATORS"""

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

# Using functools.wraps
# When we use decorators, the metadata of the original function is lost. This means that the name and the docstring of the original function are lost.
# To preserve the metadata of the original function, we can use the wraps decorator from the functools module.
# The wraps decorator is used to preserve the metadata of the original function when using decorators.
# The following code shows how to use the wraps decorator:

import functools

def start_end_decorator_two(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Do something now
        print("Start")
        result = func(*args, **kwargs)
        # Do something else
        print("End")
        return result
    return wrapper

@start_end_decorator_two
def say_hello_two():
    print("Hello") # This will print: Start Hello End

"""ANOTHER EXAMPLE"""

# Decorators with arguments
# Decorators can also take arguments. To do this, we need to add another layer of functions.
# The outer function takes the arguments, and the inner function takes the function to be decorated.
# The inner function then returns the wrapper function that will be applied to the function to be decorated.
# The following code shows a decorator that takes an argument:  --> This is a decorator factory

def repeat(num_times):
    def decorator_repeat(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat

# This is how we use the decorator with arguments:
@repeat(num_times=3)
def greet(name):
    print(f"Hello {name}")

greet("World") # This will print Hello World three times --> Hello World Hello World Hello World

def add5(x):
    return x + 5

add5 = repeat(num_times=3)(add5)
result = add5(10)
print(result) # This will print 20

"""
Following function will:
1. Call the repeat function with num_times=3 as an argument.
2. The repeat function returns the decorator_repeat function.
3. The decorator_repeat function takes the add5 function as an argument.
"""
def debug(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__}({signature})")
        result = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {result!r}")
        return result
    return wrapper

@debug
@start_end_decorator_two
def say_hello_two(name):
    greet = f'Hello {name}'
    print(greet)
    return greet

say_hello_two("World") # This will print: Calling say_hello_two('World') Start Hello World End 'Hello World' say_hello_two returned 'Hello World'


"""CLASS DECORATORS"""

# Class decorators are used to modify the behavior of a class. They are used to add functionality to existing classes without changing their structure.
# The following code shows how to use class decorators:

class CountCalls:
    def __init__(self, func):
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f"This is executed {self.num_calls} times")
        return self.func(*args, **kwargs)

@CountCalls 
def say_hello():
    print("Hello")

say_hello() # This will print: This is executed 1 times - And print: Hello
say_hello() # This will print: This is executed 2 times - And print: Hello 
say_hello() # This will print: This is executed 3 times - And print: Hello

"""GENERATORS"""
# Generators are a type of iterable, like lists or tuples. They do not allow indexing, but they can still be iterated through using for loops.
# Generators are a type of iterable that does not store the values in memory. Instead, they generate the values on the fly.
# It returns objects that can be iterated over. They are used to create iterators.
# Generators are used to create iterators. They are a type of iterable that does not store the values in memory. Instead, they generate the values on the fly.
# Generators are created using functions and the yield keyword.
# The following code shows how to create a generator:

my_generator = (x*x for x in range(3))
print(my_generator) # This will print: <generator object <genexpr> at 0x7f8b3c6c6a50>
for i in my_generator:
    print(i) # This will print: 0 1 4

# The following code shows how to create a generator using a function:
def my_generator_two():
    yield 1 # Only one is returned at a time. This is the difference between a generator and a normal function. The normal function will return all the values at once.
    yield 2 # Only returns what is asked for
    yield 3

gen = my_generator_two()
print(gen) # This will print: <generator object my_generator_two at 0x7f8b3c6c6a50>
for i in gen:
    print(i) # This will print: 1 2 3

#OR

value = next(gen)
print(value) # This will print: 1 --> Returns only till the first yield
value = next(gen)
print(value) # This will print: 2 --> Returns only till the second yield
value = next(gen)
print(value) # This will print: 3 --> Returns till the third yield
value = next(gen)
print(value) # This will raise a StopIteration error because there are no more values

# Inputs to other functions

g = my_generator_two()
double = map(lambda x: x*2, g)
print(list(double)) # This will print: [2, 4, 6]

sorted_gen = sorted(g)
print(sorted_gen) # This will print: [1, 2, 3]

def countdown(num):
    print("Starting")
    while num > 0:
        yield num # This will remember the state of the function and will continue from where it left off
        num -= 1 # This will subtract 1 from the num
        # This is the difference between a generator and a normal function. The normal function will return all the values at once.

cd = countdown(4)
value = next(cd)
print(value) # This will print: 4
value = next(cd)
print(value) # This will print: 3
value = next(cd)
print(value) # This will print: 2
value = next(cd)
print(value) # This will print: 1
value = next(cd)
print(value) # This will raise a StopIteration error because there are no more values

def firstn(n):
    num = 0
    while num < n:
        yield num
        num += 1

sum_of_first_n = sum(firstn(1000000))
print(sum_of_first_n) # This will print: 499999500000

# Ineffienct way to do this would be:
def firstn_list(n):
    nums = []
    num = 0
    while num < n:
        nums.append(num)
        num += 1
    return nums

sum_of_first_n = sum(firstn_list(1000000))
print(sum_of_first_n) # This will print: 499999500000

# This is inefficient because it stores all the values in memory. Generators are more memory efficient.