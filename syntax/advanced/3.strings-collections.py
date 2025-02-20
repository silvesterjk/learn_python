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


# COLLECTIONS

# Counter
from collections import Counter
a = "aaaaabbbbcccdde"
my_counter = Counter(a) # We could use list or tuple as well
print(my_counter) # Counter({'a': 5, 'b': 4, 'c': 3, 'd': 2, 'e': 1})
print(my_counter.items()) # dict_items([('a', 5), ('b', 4), ('c', 3), ('d', 2), ('e', 1)])
print(my_counter.keys()) # dict_keys(['a', 'b', 'c', 'd', 'e'])
print(my_counter.values()) # dict_values([5, 4, 3, 2, 1])
print(my_counter.most_common(1)) # [('a', 5)] --> Returns the most common element in the dictionary
print(my_counter.most_common(2)) # [('a', 5), ('b', 4)] --> Returns the most common
print(my_counter.most_common(1)[0][0]) # a --> Returns the tuple at index 0 and the element at index 0
print(my_counter.most_common(1)[0][1]) # 5 --> Returns the tuple at index 0 and the element at index 1
print(my_counter.elements()) # <itertools.chain object at 0x7f3c7c7b5e80> --> Returns an iterator
print(list(my_counter.elements())) # ['a', 'a', 'a', 'a', 'a', 'b', 'b', 'b', 'b', 'c', 'c', 'c', 'd', 'd', 'e'] --> Returns a list of the elements


#namedTuple
from collections import namedtuple
Point = namedtuple("Point", "x,y") # Point is the name of the tuple and x and y are the fields. x and y can also be seperated by space.
pt = Point(1, -4)
print(pt) # Point(x=1, y=-4)
print(pt.x) # 1

#OrderedDict
from collections import OrderedDict
ordered_dict = OrderedDict()
ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['d'] = 4
ordered_dict['e'] = 5
print(ordered_dict) # OrderedDict([('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)]) --> Maintains the order of the elements
# OrderDict is used for ordered dictionaries. It is a dictionary subclass that remembers the order in which the elements were inserted.
# Can be used to implement a stack or queue.

#defaultdict
from collections import defaultdict
d = defaultdict(int) # If we use float instead of int then the default value would be 0.0. Similarly the usage of list would be []
d['a'] = 1
d['b'] = 2
print(d) # defaultdict(<class 'int'>, {'a': 1, 'b': 2})
print(d['c']) # 0 --> Returns 0 because the key does not exist in the dictionary
print(d) # defaultdict(<class 'int'>, {'a': 1, 'b': 2, 'c': 0}) --> Adds the key to the dictionary with the default value of 0
# defaultdict is a dictionary subclass that calls a factory function to supply missing values.
# It is used to create a dictionary with a default value for each key.

#deque --> Double-ended queue
from collections import deque
d = deque()
d.append(1)
d.append(2)
d.appendleft(3)
print(d) # deque([3, 1, 2])
d.pop()
print(d) # deque([3, 1])
d.popleft()
print(d) # deque([1])
d.extend([4, 5, 6])
print(d) # deque([1, 4, 5, 6])
d.rotate(1)
print(d) # deque([6, 1, 4, 5])
d.rotate(-1)
print(d) # deque([1, 4, 5, 6])
# deque is a list-like container with fast appends and pops on either end. 
# It is used to implement queues and stacks.

#ChainMap
from collections import ChainMap
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
chain_map = ChainMap(dict1, dict2)
print(chain_map) # ChainMap({'a': 1, 'b': 2}, {'c': 3, 'd': 4})
print(chain_map['a']) # 1
print(chain_map['c']) # 3
print(chain_map.maps) # [{'a': 1, 'b': 2}, {'c': 3, 'd': 4}]
dict2['c'] = 5
print(chain_map.maps) # [{'a': 1, 'b': 2}, {'c': 5, 'd': 4}]
print(chain_map['c']) # 5
print(chain_map['e']) # KeyError: 'e'
# ChainMap is a dictionary-like class that makes it easy to work with multiple dictionaries.
# It is used to combine multiple dictionaries or mappings.





