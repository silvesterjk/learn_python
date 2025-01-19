"""1. Introduction to Regular Expressions

Regular expressions are sequences of characters that define search patterns. 
They are utilized for tasks such as validating email formats, searching for specific patterns in text, and more. 
In Python, the `re` module provides support for working with regular expressions."""

"""2. The re.search() Function

The re.search() function scans through a string and returns a match object if it finds a match for the pattern; otherwise, it returns None."""

import re

email = input("What's your email? ").strip()

if re.search(r".+@.+\.edu", email):
    print("Valid")
else:
    print("Invalid")

"""
In this example, the pattern r".+@.+\.edu" is used to check if the input string contains an '@' symbol followed by '.edu'. 
The + signifies one or more occurrences of any character except a newline, and \. matches a literal period. 

The . after @ in the regular expression r".+@.+\.edu" is a crucial part of the pattern. Here's a breakdown:

@: This ensures that the string contains the @ symbol, which is required for email addresses.
.: In a regular expression, a standalone . matches any single character except a newline.
\.: A backslash \ escapes the . to indicate that it should be treated as a literal dot (period). 
This is important because, without the escape, the . would act as a wildcard character.

In the context of the pattern:
.+ before @ ensures there are one or more characters before the @.
.+ after @ ensures there are one or more characters between the @ and .edu.
\.edu specifically matches the literal string .edu.
"""
"""3. Raw Strings in Python

In Python, prefixing a string with r denotes a raw string, which tells the interpreter to treat backslashes as literal characters and not as escape characters."""

import re

email = input("What's your email? ").strip()

if re.search(r"^.+@.+\.edu$", email):
    print("Valid")
else:
    print("Invalid")

"""
Here, ^ asserts the start of the string, and $ asserts the end, ensuring the entire string matches the pattern. 
Using raw strings (r"...") prevents Python from interpreting backslashes as escape characters.
"""

"""4. Special Characters in Regular Expressions

Regular expressions utilize various special characters for pattern matching:

.: Matches any character except a newline.
+: Matches one or more of the preceding element.
*: Matches zero or more of the preceding element.
?: Matches zero or one of the preceding element.
^: Matches the start of the string.
$: Matches the end of the string.
\: Escapes a special character, allowing it to be treated as a literal."""

"""
5. Using Character Sets and Ranges

Square brackets [] define a character set, matching any one character from the set. Ranges can be specified using a hyphen - :

"""
import re

username = input("Enter a username: ").strip()

if re.search(r"^[a-zA-Z0-9_]+$", username):
    print("Valid username")
else:
    print("Invalid username")

#This pattern ensures the username contains only letters (uppercase or lowercase), digits, or underscores.

"""6. Grouping and Capturing

Parentheses () are used to group parts of a pattern and capture matching content.
Here, \d{4} matches exactly four digits, and the parentheses capture the year, month, and day parts of the date separately:
"""

import re

date = input("Enter a date (YYYY-MM-DD): ").strip()

match = re.search(r"^(\d{4})-(\d{2})-(\d{2})$", date) # Here r" is used to denote a raw string and ^ and $ are used to match the start and end of the string respectively.
if match:
    year, month, day = match.groups()
    print(f"Year: {year}, Month: {month}, Day: {day}")
else:
    print("Invalid date format")

"""7. Substitution with re.sub()

The re.sub() function replaces occurrences of a pattern with a specified replacement string.
This replaces all occurrences of "ain" with "###" in the given text:
"""
import re

text = "The rain in Spain stays mainly in the plain."

new_text = re.sub(r"ain", "###", text) # Here ain is replaced with ### by using re.sub() function. 
print(new_text) # The output would look like "The r### in Sp### stays m###ly in the pl###."

"""8. Splitting Strings with re.split()

The re.split() function splits a string by occurrences of a pattern.
This splits the text into a list of fruits, using commas, semicolons, or vertical bars as delimiters, and removes any surrounding whitespace:
"""

import re

text = "apple, banana; cherry|date"

fruits = re.split(r"[,;|]\s*", text) # Here re.split() function is used to split the text into a list of fruits using commas, semicolons, or vertical bars as delimiters.
print(fruits) # The output would look like ['apple', 'banana', 'cherry', 'date']


"""9. Finding All Matches with re.findall()

The re.findall() function returns a list of all non-overlapping matches of a pattern in a string."""

import re

text = "Contact us at support@example.com or sales@example.org."

# This extracts all email addresses from the given text.
emails = re.findall(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", text)
print(emails)

"""10. Compiling Regular Expressions

For patterns used multiple times, compiling them can improve efficiency."""

import re

# Regular expression pattern for a Social Security Number (SSN)
pattern = re.compile(r"\b\d{3}-\d{2}-\d{4}\b")

# Example text containing SSNs
text = "SSN: 123-45-6789, SSN: 987-65-4321"

# Find all SSNs in the text
ssns = pattern.findall(text)
print(ssns)  # Output: ['123-45-6789', '987-65-4321']

 
