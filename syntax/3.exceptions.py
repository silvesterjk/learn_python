""" 1. Exceptions

Exceptions are events that disrupt the normal flow of a program's instructions. They occur due to errors such as syntax mistakes or invalid operations.

Example of a syntax error: This code will raise a SyntaxError because of the missing closing quotation mark. """

# print("Hello, world)


"""2. Runtime Errors

Runtime errors happen during the execution of a program, often due to unexpected user input or operations. Example: """

x = int(input("What's x? "))
print(f"x is {x}")

""" If the user inputs a non-integer value like "cat", the program will raise a ValueError. """

""" 3. The try and except Blocks

To handle exceptions gracefully, Python provides the try and except blocks. Code that might raise an exception is placed inside the try block, and the handling of the exception is done in the except block

Syntax:

try:
    # code that might raise an exception
except ExceptionType:
    # code to handle the exception

In this example, if the user inputs a non-integer value, the program will print "x is not an integer". Otherwise, it will print the value of x. """

try:
    x = int(input("What's x? "))
except ValueError:
    print("x is not an integer")
else:
    print(f"x is {x}")

"""4. The else Clause

The else clause can be used after the except block to execute code that should run only if no exceptions were raised in the try block.

Here, the else block executes only if the try block succeeds without raising an exception. """

try:
    x = int(input("What's x? "))
except ValueError:
    print("x is not an integer")
else:
    print(f"x is {x}")

"""5. Creating a Function to get an Integer

To repeatedly prompt the user until a valid integer is provided, we can define a function that utilizes a loop along with try and except.

Example : This function will keep prompting the user until a valid integer is entered. """

def get_int():
    while True:
        try:
            return int(input("What's x? "))
        except ValueError:
            print("x is not an integer")

x = get_int()
print(f"x is {x}")

"""6. The pass Statement

The pass statement is a null operation; it does nothing when executed. It's useful as a placeholder in situations where syntactically some code is required but you don't want to execute any code.

Example: In this case, if a ValueError occurs, the program simply ignores it and continues prompting the user. """

def get_int():
    while True:
        try:
            return int(input("What's x? "))
        except ValueError:
            pass  # Ignore the error and prompt again