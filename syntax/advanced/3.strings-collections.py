"""STRING"""
# Strings are immutable sequences of Unicode code points.
# Strings are arrays of bytes representing Unicode characters.

mystring = "Hello, World!"
mystring2 = 'Hello, World!'
mystring3 = 'Hello, \
    World!'

mystring4 = """Hello, 
    World!"""

print(mystring)
print(mystring2)
print(mystring3)
print(mystring4)

mystring5 = "Hello, World!"
# mystring5[0] = 'h' # TypeError: 'str' object does not support item assignment
char = mystring5[0]
print(char) # H

range_ = mystring5[0:5]
print(range_) # Hello

range_step2 = mystring5[0:5:2]
print(range_step2) # Hlo

step3 = mystring5[::3]
print(step3) # HlWl

step3rev = mystring5[::-1]
print(step3rev) # !dlroW ,olleH

# String concatenation
string1 = "Hello"
string2 = "-"
string3 = "World"
string4 = string1 + " " + string2 + " " + string3 # Hello - World
string5 = string1 + string2 + string3 # HelloWorld --> This does not concatenate the strings with a space because we did not add a space in the concatenation.
# That is why we have to add a space in the concatenation. For example, string1 + " " + string2 + " " + string3
print(string5) # HelloWorld
string6 = string1 + string3 # HelloWorld --> This concatenates the strings without a space because we did not add a space in the concatenation.

# String formatting
name = "John"
age = 25
formatted_string = "My name is {} and I am {} years old".format(name, age)
print(formatted_string) # My name is John and I am 25 years old

formatted_string2 = "My name is {0} and I am {1} years old".format(name, age)
print(formatted_string2) # My name is John and I am 25 years old

formatted_string3 = "My name is {name} and I am {age} years old".format(name="John", age=25)
print(formatted_string3) # My name is John and I am 25 years old

# f-strings
formatted_string4 = f"My name is {name} and I am {age} years old and I will be {age*2} in another 25 years."
print(formatted_string4) # My name is John and I am 25 years old and I will be 50 in another 25 years.

# % operator
formatted_string5 = "My name is %s and I am %d years old" % (name, age)
print(formatted_string5) # My name is John and I am 25 years old

pi_value = 3.14159
e_value = 2.71828
formatted_string6 = "The value of pi is %.2f" % pi_value # The value of pi is 3.14

# .format() method
formatted_string7 = "My name is {name} and I am {age} years old".format(name="John", age=25)
print(formatted_string7) # My name is John and I am 25 years old

formatted_string8 = "The value of pi is {:.2f} and the value of e is {:.3f}".format(pi_value, e_value) # The value of pi is 3.14 and the value of e is 2.718

# String presence and absence

string7 = "Hello, World!"
if 'x' in string7:
    print("x is in string7")
elif 'X' in string7:
    print("X is in string7")
else:
    print("Char not in string7")

string8 = "    Hello, World!    "
if string8.strip():
    print("string8 is not empty")

string8_check = string8.strip()
print(string8_check) # Hello, World! --> Removes the leading and trailing whitespaces

string9 = string8_check.split(",")
print(string9) # ['Hello', ' World!'] --> Splits the string into a list seperated by comma
string9_two = string8_check.split(" ")
print(string9_two) # The result would be ['Hello,', 'World!'] --> Splits the string into a list seperated by space

string10 = string8_check.replace("Hello", "Hi")
print(string10) # Hi, World! --> Replaces Hello with Hi 

string11 = string8_check.startswith("Hello")
print(string11) # True

string12 = string8_check.endswith("World!")
print(string12) # True
print(string8_check.count("l")) # 3 --> Returns the number of occurrences of the substring
print(string8_check.find("l")) # 2 --> Returns the index of the first occurrence of the substring

# bad way to concatenate strings
mylist = ["a", "b", "c"]

mystring = ""
for letter in mylist:
    mystring += letter
print(mystring) # abc --> bad because it creates a new string object for each concatenation

# good way to concatenate strings
mylist = ["a", "b", "c"]
mystring = "".join(mylist)

print(mystring) # abc --> good because it creates a new string object for each concatenation