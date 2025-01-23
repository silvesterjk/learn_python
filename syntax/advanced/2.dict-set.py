"""DICTIONARY"""

mydict = {"name": "John", "age": 36, "country": "Norway", "city": "Oslo"}
print(mydict)

value = mydict["name"]
print(value) # John

mydict["lastname"]
print(mydict) # KeyError: 'lastname'

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

try:
    print(mydict["supername"])
except KeyError:
    print("KeyError: 'supername'")

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

mydict6 = {["name", "age"]: "John"}  # TypeError: unhashable type: 'list' 
# List is mutable and cannot be used as a key in a dictionary