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
mystring5[0] = 'h' # TypeError: 'str' object does not support item assignment
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