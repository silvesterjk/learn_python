"""DICTIONARY"""

mydict = {"name": "John", "age": 36, "country": "Norway", "city": "Oslo"}
print(mydict)

value = mydict["name"]
print(value) # John

# mydict["lastname"]
# print(mydict) # KeyError: 'lastname'

mydict["lastname"] = "Doe"
print(mydict) # {'name': 'John', 'age': 36, 'country': 'Norway', 'city': 'Oslo', 'lastname': 'Doe'}

mydict.pop("lastname")

del mydict["city"]
print(mydict) # {'name': 'John', 'age': 36, 'country': 'Norway'}

if "lastname" in mydict:
    print("yes")
else:
    print("no")

print(len(mydict)) # 3

# try:
#     print(mydict["supername"])
# except KeyError:
#     print("KeyError: 'supername'")

for value in mydict.values():
    print(value) # John 36 Norway

for key in mydict.keys():  
    print(key) # name age country

for key, value in mydict.items():
    print(key, value) # name age country

# Assigning a dictionary to a variable will not create a new copy of the dictionary
# It will only create a reference to the dictionary
# To create a copy of the dictionary, use the copy() method

mydict2 = mydict.copy()

mydict3 = dict(name="Dola", age=32, country="Sweden", city="Stockholm")  # Corrected line

# mydict.clear()  # clear the dictionary

print(mydict3)  # {'name': 'Dola', 'age': 32, 'country': 'Sweden', 'city': 'Stockholm'}

 # A tuple can be used as a key in a dictionary
mydict4 = {("name", "age"): "John"}
print(mydict4)  # {('name', 'age'): 'John'}

# Numbers can be used as keys in a dictionary
mydict5 = {4: "apple", 5: "banana"}
print(mydict5)  # {1: 'apple', 2: 'banana'}
print(mydict5[4])  # apple -- 4 instead of 0 because the key is 4

# List is mutable and cannot be used as a key in a dictionary
# mydict6 = {["name", "age"]: "John"}  # TypeError: unhashable type: 'list' 

"""SET"""

myset = {"apple", "banana", "cherry"}
print(myset)  # {'banana', 'apple', 'cherry'} -- unordered

myset2 = {"apple", "banana", "cherry", "cherry", "banana"}
print(myset2) # {'banana', 'apple', 'cherry'} -- no duplicates


# myset = {"apple", "banana", "cherry", "apple"}  # {'banana', 'apple', 'cherry'} -- no duplicates

# If we try to access an element in a set using an index, we will get an error
# If there are duplicates in the set, only one will be 

myset.add("orange")
print(myset)  # {'banana', 'apple', 'cherry', 'orange'}

myset.update(["orange", "mango", "grapes"])
print(myset)  # {'orange', 'banana', 'apple', 'mango', 'grapes', 'cherry'}
# The update() method can take lists, tuples, dictionaries, and sets

# An empty set cannot be created using {}
myset3 = set() # create an empty set

myset3.add(1)
myset3.add(2)
myset3.add(3)
myset3.add(4)
print(myset3)  # {1, 2, 3, 4}

myset3.remove(2) # remove 2 from the set
print(myset3)  # {1, 3, 4}

myset3.discard(3) # remove 3 from the set
print(myset3)  # {1, 4}

myset3.pop() # removes an arbitrary element from the set
print(myset3) # {4} -- 1 is removed

myset3.clear() # clear the set

for x in myset:
    print(x)  # orange banana apple mango grapes cherry

if "apple" in myset:
    print("yes")
else:  
    print("no")

# Union of two sets
set1 = {1, 2, 3}
set2 = {4, 5, 6}
set3 = set1.union(set2)
print(set3)  # {1, 2, 3, 4, 5, 6}


# Intersection of two sets
set4 = set1.intersection(set2)
print(set4)  # set()

# Difference of two sets
set5 = set1.difference(set2)
print(set5)  # {1, 2, 3} --> set1 - set2

# Symmetric difference of two sets
set6 = set1.symmetric_difference(set2)
print(set6)  # {1, 2, 3, 4, 5, 6} --> (set1 - set2) U (set2 - set1)

# issubset() method
set7 = {1, 2, 3}
set8 = {1, 2, 3, 4, 5}
set9 = {1, 2, 4}
print(set7.issubset(set8))  # True
print(set7.issubset(set9))  # False

set7.update(set9)
print(set7)  # {1, 2, 3, 4}

set7.intersection_update(set9)
print(set7)  # {1, 2, 4} --> Here we are updating set7 with the intersection of set7 and set9

set7.difference_update(set9)
print(set7)  # {2} --> Here we are updating set7 with the difference of set7 and set9

set7.symmetric_difference_update(set9)
print(set7)  # {1, 4} --> Here we are updating set7 with the symmetric difference of set7 and set9

# isdisjoint() method
set10 = {1, 2, 3}
set11 = {4, 5, 6}
set12 = {7, 8, 9}
print(set10.isdisjoint(set11))  # True
print(set10.isdisjoint(set12))  # True
print(set11.isdisjoint(set12))  # True

# issuperset() method
set13 = {1, 2, 3, 4, 5}
set14 = {1, 2, 3}
set15 = {1, 2, 3, 4, 7}
print(set13.issuperset(set14))  # True -- set13 is a superset of set14
print(set14.issuperset(set15)) # False -- set14 is not a superset of set15
