"""LIST: ordered and changeable. Allows duplicate elements"""

mylist = [1, 3, 2, 4, 5]
print(mylist[1:3])  # Outputs: [2, 3]

for i in mylist:
    print (i)

if 1 in mylist:
    print("yes")

print(len(mylist))

mylist.append(6)
print(mylist)

mylist.insert(1, 7) # insert 7 at index 1
print(mylist)

mylist.remove(7) # remove 7 from list -- rermove first occurance of the value
mylist.pop() # remove last element and also return it. we can assign it to a variable if we want to use it later

print(mylist) # [1, 2, 3, 4, 5]
reverse_item = mylist.reverse() # reverse the list. We have assigned it to a new variable because reverse() method does not return anything.
print(mylist) # None. But printing reverse_item will give None. Because reverse() method does not return anything.

sort_item = mylist.sort() # sort the list

# clear_item = mylist.clear() # clear the list

newlist = [0] * 5
newlist2 = [3, 5, 6, 7, 8]

newlist = mylist + newlist2
print(newlist)

list_org = ["apple", "banana", "cherry"]
list_copy = list_org
list_copy2 = list_org.copy()


list_copy.append("orange")

print(list_org) # ['apple', 'banana', 'cherry', 'orange']
print(list_copy) # ['apple', 'banana', 'cherry', 'orange'] because list_copy is just a reference to list_org
print(list_copy2) # ['apple', 'banana', 'cherry'] because list_copy2 is a copy of list_org

# List comprehension
a = [1, 2, 3, 4, 5]
b = [i*i for i in a] # [1, 4, 9, 16, 25]  -- square of each element in list a -- Expression first - for each element in list a

"""TUPLE: orrdered and immutable. Allows duplicate elements"""

mytuple = ("apple", "banana", "cherry", 2, 2, 2.2)
# If there is only one value in tuple, then we need to add a comma after the value
# mytuple = ("apple",) # tuple
# mytuple = ("apple") # string

print(mytuple[1:3]) # ('banana', 'cherry')

mynewtuple = tuple(["apple", "banana", "cherry"]) # create a tuple using tuple() constructor
print(mynewtuple)

t_item = mytuple[0]
print(t_item) # apple

# mytuple[0] = "orange" # TypeError: 'tuple' object does not support item assignment

for x in mytuple:
    print(x) # apple banana cherry 2 2.2

if "apple" in mytuple:
    print("yes")
else:
    print("no")

print(len(mytuple)) # 5
print(mytuple.count(2)) # 2

print(mytuple.index(2.2)) # 5 is the first occurance of 2.2

# Tuple unpacking
a, b, c, d, e, f  = mytuple  # matching one for one between the variable and the items in the tuple -- the values must match the number of elements in the tuple
print(a) # apple
print(b) # banana
print(c) # cherry
print(d) # 2
print(e) # 2
print(f) # 2.2


# Slicing tuple
print(mytuple[1:3]) # ('banana', 'cherry')

import sys
mytestlist = [0, 1, 2, "apple", "banana", "cherry", 2.2]
mytesttuple = (0, 1, 2, "apple", "banana", "cherry", 2.2)
print(sys.getsizeof(mytestlist), "bytes") # 120 bytes
print(sys.getsizeof(mytesttuple), "bytes") # 96 bytes

import timeit
print(timeit.timeit(stmt="[0, 1, 2, 3, 4, 5]", number=1000000)) # ~0.087 seconds
# Here we are creating a list and tuple with the same elements and then we are measuring the time taken to create the list and tuple.
# We are creating the list and tuple 1000000 times and then we are measuring the time taken to create the list and tuple.
print(timeit.timeit(stmt="(0, 1, 2, 3, 4, 5)", number=1000000)) # `0.019 seconds -- tuple is faster than list. In this case by 4.5 times

"""
In Summary: 
* List is mutable and tuple is immutable
* tuple is more efficient than list. Because tuple is immutable and it is faster to access the elements in tuple than in list.
* tuple is used when we want to make sure that the data is not changed.
* tuple has less footprint than list. So, tuple is used when we want to store the data in less memory.
* List is used when we want to store the data that can be changed. List is used when we want to store the data that can be changed.
"""