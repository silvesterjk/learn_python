"""1. Introduction to Unit Tests

Traditionally, you might test your code using print statements or by manually checking outputs. 
However, as programs grow in complexity, systematic testing becomes crucial. 
Unit tests allow you to automate the testing of individual functions or components to ensure they work correctly under various conditions."""

"""2. Writing a Simple Function

Consider a function square that returns the square of a number:"""

def square(n):
    return n * n

"""3. Creating a Test File

To test the square function, create a separate file named test_calculator.py with the following content:"""

from calculator import square

def main():
    test_square()

def test_square():
    if square(2) != 4:
        print("2 squared was not 4")
    if square(3) != 9:
        print("3 squared was not 9")

if __name__ == "__main__":
    main()

# This script imports the square function and defines tests to check if it returns the expected results for specific inputs.

"""4. Using assert Statements

To simplify and enhance the readability of tests, Python's assert statement can be used:
# With assert, if the condition evaluates to True, the program continues silently. 
# If it evaluates to False, an AssertionError is raised, indicating a failed test.
"""

from calculator import square

def test_square():
    assert square(2) == 4
    assert square(3) == 9

"""5. Introducing pytest

For more advanced testing capabilities, the pytest framework is commonly used. 
It provides detailed information about test failures and supports a wide range of testing needs.
To use pytest, first install it as  a package using pip: pip install pytest
Then, modify your test file as follows:
"""

from calculator import square

def test_square():
    assert square(2) == 4
    assert square(3) == 9
    assert square(-2) == 4
    assert square(0) == 0

"""
To run the tests, execute pytest in the terminal: pytest test_calculator.py

pytest will automatically discover functions prefixed with test_ and execute them, providing a summary of passed and failed tests.

"""

"""6. Testing Strings

When testing functions that return strings, it's important to consider different cases and whitespace. For example:"""

def capitalize_string(s):
    return s.capitalize()

# A corresponding test could be:

def test_capitalize_string():
    assert capitalize_string('hello') == 'Hello'
    assert capitalize_string('') == ''

"""7. Organizing Tests into Folders

As the number of tests grows, organizing them into folders can improve maintainability. A common structure is:
Note: Ensure that the tests folder contains an empty __init__.py file to indicate it's a package.

project/
│
├── calculator.py
└── tests/
    └── test_calculator.py
    └── __init__.py

This structure allows for organized and scalable testing as your project expands.
    
"""

