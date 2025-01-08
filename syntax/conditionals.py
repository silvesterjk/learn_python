
"""
1. Boolean Expressions

A Boolean expression evaluates to either True or False. These expressions are essential for making decisions in code.

"""
x = 5
y = 10
print(x < y)  # Outputs: True

"""
2. The if Statement

The if statement allows execution of a block of code only if a specified condition is True.

if condition:
    # code to execute if condition is True
"""

age = 18
if age >= 18:
    print("You are an adult.")

"""
3. The else Statement

The else statement follows an if statement and executes a block of code if the if condition is False.

if condition:
    # code if condition is True
else:
    # code if condition is False

"""

age = 16
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")


"""
4. The elif Statement

The elif (short for else if) statement checks another condition if the previous if condition is False.

if condition1:
    # code if condition1 is True
elif condition2:
    # code if condition2 is True
else:
    # code if both conditions are False

"""

score = 85
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
else:
    print("Grade: C")

"""
5. Logical Operators

Logical operators combine multiple conditions:

and: True if both conditions are True.
or: True if at least one condition is True.
not: Inverts the Boolean value.

"""

# Using 'and'
x = 5
y = 10
if x > 0 and y > 0:
    print("Both numbers are positive.")

# Using 'or'
x = -5
if x < 0 or y < 0:
    print("At least one number is negative.")

# Using 'not'
is_raining = False
if not is_raining: # if is_raining is not True
    print("It's not raining.")

"""
6. Nested Conditionals

Conditionals can be nested within each other to check multiple conditions.

"""

num = 10
if num > 0:
    if num % 2 == 0:
        print("Positive even number.")
    else:
        print("Positive odd number.")
else:
    print("Non-positive number.")


"""
7. The match Statement (Python 3.10+)

Python 3.10 introduced the match statement, similar to switch-case in other languages, for matching values against patterns.

match variable:
    case pattern1:
        # code for pattern1
    case pattern2:
        # code for pattern2
    case _:
        # default case

"""

day = "Monday"
match day:
    case "Monday":
        print("Start of the work week.")
    case "Friday":
        print("End of the work week.")
    case _:
        print("Midweek day.")


