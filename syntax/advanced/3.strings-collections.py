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