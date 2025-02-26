"""ARGS"""

def myfunc(a, b, c, *args):
    """
    1. The *args parameter is used to pass a variable number of arguments to a function.
    2. The *args parameter is used to pass a variable number of positional arguments to a function.
    3. Positional arguments are arguments that are passed by position. They are not named.
    4. The *args parameter is a tuple that holds the positional arguments passed to the function.
    """
    print(a, b, c)
    for arg in args:
        print(arg)

myfunc(1, 2, 3, 4, 5)

# Output:
# 1 2 3
# 4
# 5

def myfunc(a, b, c, *args):
    """
    1. The *args parameter is used to pass a variable number of arguments to a function.
    2. The *args parameter is used to pass a variable number of positional arguments to a function.
    """
    print(a, b, c)
    for arg in args:
        print(arg)

myfunc(1, 2, 3, 4, 5, 6, 7, 8, 9)

# Output:
# 1 2 3
# 4
# 5
# 6
# 7
# 8
# 9


"""KWARGS"""

def myfunc(a, b, c, *args, **kwargs):
    """
    1. The **kwargs parameter is used to pass a variable number of keyword arguments to a function.
    2. The **kwargs parameter is used to pass a variable number of named arguments to a function.
    3. Named arguments are arguments that are passed by name.
    4. The **kwargs parameter is a dictionary that holds the named arguments passed to the function.
    5. The **kwargs parameter must be the last parameter in the function definition.
    6. The **kwargs parameter is optional.
    """
    print(a, b, c)
    for arg in args:
        print(arg)
    for key in kwargs:
        print(key, kwargs[key]) 

myfunc(1, 2, 3, 4, 5, 6, 7, 8, 9, name="John", age=30)

# Output:
# 1 2 3
# 4
# 5
# 6
# 7
# 8
# 9
# name John
# age 30


"""ARGS AND KWARGS"""

def myfunc(*args, **kwargs):
    for arg in args:
        print(arg)
    for key in kwargs:
        print(key, kwargs[key])

myfunc(1, 2, 3, name="John", age=30)

# Output:
# 1
# 2
# 3
# name John
# age 30

def myfunc(a,b,*,c,d): # This will only accept c and d as keyword arguments
    print(a,b,c,d)

myfunc(1,2,c=3,d=4) # This will print 1 2 3 4

# myfunc(1,2,3,4) # This will raise a TypeError because c and d are not keyword arguments


"""UNPACKING LISTS AND DICITONARIES WITH A FUNCTION"""

# Lists

def myfunc(a, b, c):
    """
    1. The myfunc function takes three arguments, a, b, and c.
    2. The function prints the arguments.
    3. The mylist list contains the values 1, 2, and 3.
    4. The *mylist syntax is used to unpack the list and pass the values to the function.
    5. The function is called with the unpacked values.
    """
    print(a, b, c)

mylist = [1, 2, 3]
myfunc(*mylist) # This will print 1 2 3


# Dictionaries

def myfunc(a, b, c):
    """
    1. The myfunc function takes three arguments, a, b, and c.
    2. The function prints the arguments.
    3. The mydict dictionary contains the key-value pairs a: 1, b: 2, and c: 3.
    4. The **mydict syntax is used to unpack the dictionary and pass the values to the function.
    5. The function is called with the unpacked values.
    """
    print(a, b, c)

mydict = {'a': 1, 'b': 2, 'c': 3}
myfunc(**mydict) # This will print 1 2 3. Here the keys in the dictionary are the same as the parameters in the function. Otherwise, it will raise a TypeError.


"""ARGS AND KWARGS WITH DECORATORS"""

def my_decorator(func):
    """
    1. The my_decorator function takes a function as an argument.
    2. The wrapper function takes any number of positional and keyword arguments.
    3. The wrapper function prints the positional and keyword arguments.
    4. The wrapper function calls the original function with the positional and keyword arguments.
    5. The wrapper function returns the result of the original function.
    6. The my_decorator function returns the wrapper function.
    7. The @my_decorator syntax is used to apply the decorator to a function.
    8. The example_function function is decorated with the my_decorator decorator.
    """
    def wrapper(*args, **kwargs):
        print("Args:", args)
        print("Kwargs:", kwargs)
        func(*args, **kwargs)
    return wrapper

@my_decorator
def example_function(a, b, c):
    print(a, b, c)

example_function(1, 2, 3) # This will print: Args: (1, 2, 3) Kwargs: {} 1 2 3 


num_list = [1, 2, 3, 4, 5]
num_tuple = (1, 2, 3, 4, 5)
num_dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
num_dict2 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
num_dict3 = {'f': 1, 'g': 2, 'h': 3, 'i': 4, 'j': 5}
num_set = {1, 2, 3, 4, 5}

*beginning, last = num_list
print(beginning) # This will print [1, 2, 3, 4]
print(last) # This will print 5

beginning, *last = num_list
print(beginning) # This will print 1
print(last) # This will print [2, 3, 4, 5]

beginning, *middle, last = num_list
print(beginning) # This will print 1
print(middle) # This will print [2, 3, 4]
print(last) # This will print 5

beginning, *middle, secondlast, last = num_tuple
print(beginning) # This will print 1
print(middle) # This will print [2, 3] --> This is a list because the *middle syntax unpacks the values into a list.
print(secondlast) # This will print 4
print(last) # This will print 5

beginning, *middle, last = num_dict
print(beginning) # This will print a
print(middle) # This will print ['b', 'c', 'd']
print(last) # This will print e

beginning, *middle, last = num_dict.values()
print(beginning) # This will print 1
print(middle) # This will print [2, 3, 4]
print(last) # This will print 5

new_list = [*num_tuple, *num_list] # This will unpack the values in num_tuple and num_list and create a new list.
print(new_list) # This will print [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]

new_set = {*num_tuple, *num_set} # This will unpack the values in num_tuple and num_set and create a new set.
print(new_set) # This will print {1, 2, 3, 4, 5} --> This is a set because the * syntax unpacks the values into a set.

new_dict = {**num_dict1, **num_dict2} # This will unpack the key-value pairs in num_dict1 and num_dict2 and create a new dictionary.
print(new_dict) # This will print {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5} --> This is a dictionary because the ** syntax unpacks the key-value pairs into a dictionary.
# If there are duplicate keys, the value from the second dictionary will overwrite the value from the first dictionary.

new_dict = {**num_dict1, **num_dict3} # This will unpack the key-value pairs in num_dict1 and num_dict3 and create a new dictionary.
print(new_dict) # This will print {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 1, 'g': 2, 'h': 3, 'i': 4, 'j': 5} --> This is a dictionary because the ** syntax unpacks the key-value pairs into a dictionary.

# The * syntax can be used to unpack the values in a list, tuple, or set.
# The ** syntax can be used to unpack the key-value pairs in a dictionary.