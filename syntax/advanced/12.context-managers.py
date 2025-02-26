"""SHALLOW VS DEEP COPYING"""

org = [0, 1, 2, 3, 4]
cpy = org
cpy[0] = -10
print(cpy) # This will print: [-10, 1, 2, 3, 4]
print(org) # This will print: [-10, 1, 2, 3, 4]

# Shallow Copy vs Deep Copy
"""
1. Shallow Copy: A shallow copy creates a new object but does not create new objects for the nested objects.
2. Deep Copy: A deep copy creates a new object and creates new objects for the nested objects.
3. The copy module in Python provides functions for shallow and deep copying.
4. The copy.copy() function creates a shallow copy.
5. The copy.deepcopy() function creates a deep copy.
"""
# Shallow Copy
import copy
org = [0, 1, 2, 3, 4]
cpy = copy.copy(org)
# cpy = org.copy() --> This is another way to create a shallow copy
# cpy = org[:] --> This is another way to create a shallow copy
# cpy = list(org) --> This is another way to create a shallow copy

cpy[0] = -10
print(cpy) # This will print: [-10, 1, 2, 3, 4]
print(org) # This will print: [0, 1, 2, 3, 4]

# Deep Copy
org = [[0, 1], [2, 3]] # This is a nested list
cpy = copy.deepcopy(org)
cpy[0][0] = -10
cpy[1][0] = 2
print(cpy) # This will print: [[-10, 1], [2, 3]]
print(org) # This will print: [[0, 1], [2, 3]]

 