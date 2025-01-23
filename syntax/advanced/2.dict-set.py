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

mydict.clear()