# 1. While Loops

# A `while` loop continues to execute a block of code as long as its condition remains `True`.

# Syntax:
# while condition:
#     # code to execute repeatedly

# Example:
i = 0
while i < 3:
    print("meow")
    i += 1
# In this example, "meow" is printed three times. The loop runs while `i` is less than 3, incrementing `i` by 1 after each iteration.

# 2. For Loops

# A `for` loop iterates over a sequence (like a list or range) and executes a block of code for each item in that sequence.

# Syntax:
# for variable in sequence:
#     # code to execute for each item

# Example:
for i in range(3):
    print("meow")
# Here, `range(3)` generates the sequence [0, 1, 2], and "meow" is printed three times.

# 3. Using the `range()` Function

# The `range()` function generates a sequence of numbers, which is particularly useful for loops.

# Examples:

# Range from 0 to 2
for i in range(3):
    print(i)  # Outputs: 0, 1, 2

# Range from 2 to 4
for i in range(2, 5):
    print(i)  # Outputs: 2, 3, 4

# Range from 0 to 4 with step 2
for i in range(0, 5, 2):
    print(i)  # Outputs: 0, 2, 4

# 4. Nested Loops

# Loops can be nested within each other to handle more complex iterations.

# Example:
for i in range(3):
    for j in range(2):
        print(f"i: {i}, j: {j}")
# This will output all combinations of `i` and `j` within the specified ranges.

# 5. Loop Control Statements

# - `break`: Exits the loop immediately.

# Example:
for i in range(5):
    if i == 3:
        break
    print(i)  # Outputs: 0, 1, 2

# - `continue`: Skips the current iteration and proceeds to the next one.

# Example:
for i in range(5):
    if i == 3:
        continue
    print(i)  # Outputs: 0, 1, 2, 4

# 6. Iterating Over Lists

# Loops are commonly used to iterate over elements in a list.

# Example:
students = ["Hermione", "Harry", "Ron"]
for student in students:
    print(student)
# This will print each student's name in the list.

# 7. Iterating Over Dictionaries

# Dictionaries store key-value pairs, and you can iterate over them to access both keys and values.

# Example:
students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
}

for student, house in students.items():
    print(f"{student} is in {house}")
# This will output each student's name along with their associated house.

# 8. List Comprehensions

# Python provides a concise way to create lists using list comprehensions.

# Example:
squares = [x**2 for x in range(6)]
print(squares)  # Outputs: [0, 1, 4, 9, 16, 25]
# This creates a list of squares for numbers 0 through 5.

# 9. The `len()` Function

# The `len()` function returns the number of items in a list (or other iterable).

# Example:
students = ["Hermione", "Harry", "Ron"]
print(len(students))  # Outputs: 3
# This indicates there are three students in the list.

# Understanding and utilizing loops effectively allows for efficient and concise code, especially when dealing with repetitive tasks or iterating over data structures.
