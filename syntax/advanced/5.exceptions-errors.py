# ERRORS AND EXCEPTIONS

a = 5 #print(a) # SyntaxError: invalid syntax --> This is a syntax error because we did not add a newline after the value of a

# ZeroDivisionError
a = 5
b = 0
try:
    print(a/b)
except ZeroDivisionError as e:
    print("You cannot divide by zero")
    print(e)

# FileNotFoundError
try:
    file = open("test.txt")
except FileNotFoundError as e:
    print("File not found")
    print(e)

# Import Error

# try:
#     import module 
# except ImportError as e:
#     print("Module not found")
#     print(e)

# ValueError
a = '5'
try:
    a = int(a)
    print(a)
except ValueError as e:
    print("Value error")
    print(e)    

# TypeError
a = 5
b = '10'
try:
    print(a+b)
except TypeError as e:
    print("Type error")
    print(e)

# AssertionError
a = 5
assert a > 10, "This is not true" # AssertionError: This is not true

# Out of range error
a = [1, 2, 3]
try:
    print(a[3])
except IndexError as e:
    print("Index out of range")
    print(e)

# Key error
a = {'name': 'John', 'age': 25}
try:
    print(a['names']) # KeyError: 'names'
    print(a)
except KeyError as e:
    print("Key not found")
    print(e)

# Exception
try:
    a = 5/0
except Exception as e:
    print("An error occurred")
    print(e)