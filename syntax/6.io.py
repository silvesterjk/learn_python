""". Introduction to File I/O

Previously, data handled within a program was stored in memory and lost upon the program's termination. 
File I/O allows programs to read from and write to files, enabling data to persist between executions.

"""

"""2. Writing to a File

To write data to a file in Python, the open function is used with the mode 'w' (write mode):

"""
name = input("What's your name? ")

file = open("names.txt", "w")
file.write(name)
file.close()

"""In this example:

* open("names.txt", "w") opens (or creates) a file named names.txt in write mode.
* file.write(name) writes the user's input to the file.
* file.close() closes the file, ensuring the data is saved properly.
* Note: Using 'w' mode will overwrite the file if it already exists."""

"""3. Appending to a File

To add data to the end of an existing file without overwriting its contents, use the append mode 'a':
Here, each new name is appended to names.txt, with each entry on a new line.
"""

name = input("What's your name? ")

file = open("names.txt", "a")
file.write(f"{name}\n")
file.close()

"""4. Reading from a File

To read the contents of a file, open it in read mode 'r':"""

file = open("names.txt", "r")
for line in file:
    print("hello,", line.rstrip())
file.close()

# This script reads each line from names.txt and prints a greeting. 
# The rstrip() method removes any trailing whitespace, including the newline character.
# For example, if names.txt contains "Alice\nBob\n", the output will be:
# hello, Alice
# hello, Bob

"""5. Using the `with` Statement

Managing files using open and close requires careful handling to ensure files are properly closed, even if an error occurs. 
The `with` statement simplifies this by automatically managing the file's context:"""

name = input("What's your name? ")

with open("names.txt", "a") as file:
    file.write(f"{name}\n")

#In this structure, the file is automatically closed when the block inside the with statement is exited, even if an exception occurs.

"""6. Working with CSV Files

CSV (Comma-Separated Values) files are commonly used for storing tabular data. Python's csv module facilitates reading from and writing to CSV files:
"""
# Writing to a CSV file:

import csv

name = input("What's your name? ")
home = input("Where's your home? ")

with open("students.csv", "a", newline='') as file: # Here, newline='' is used to prevent extra newlines in the output. & a is used to append to the file.
    writer = csv.writer(file)
    writer.writerow([name, home]) # This writes the name and home to the CSV file.

# Reading from a CSV file:

import csv

with open("students.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(f"{row[0]} is from {row[1]}")

# Here, each row in the CSV file represents a student and their home, and the program reads and prints this information.

"""7. Handling Binary Files and Images

Python can also handle binary files, such as images, using the Pillow library (PIL). To manipulate images:"""

from PIL import Image, ImageFilter

before = Image.open("bridge.bmp")
after = before.filter(ImageFilter.BoxBlur(10))
after.save("out.bmp")

# This script opens an image file, applies a box blur filter, and saves the modified image to a new file.