
# Python and JSON Comparison:

"""
1. dict in python is equivalent to object in JSON
2. list in python is equivalent to array in JSON
3. tuple in python is equivalent to array in JSON
4. str in python is equivalent to string in JSON
5. int in python is equivalent to number in JSON
6. float in python is equivalent to number in JSON
7. True in python is equivalent to true in JSON
8. False in python is equivalent to false in JSON
9. None in python is equivalent to null in JSON
"""


# Example nested JSON

import json

log_record = {
    "time": "2020-07-01T12:00:00",
    "level": "INFO",
    "message": "This is an info message",
    "extra": {
        "user": "john",
        "role": "admin"
    }
}

# Nested JSON
person = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "languages": ["English", "Spanish", "French"],
    "programming": {
        "languages": ["Python", "Java"],
        "experience": 5
    },
    "has_children": False 
}

personJSON = json.dumps(person, indent=4, sort_keys=True)
print(personJSON)

"""
Output:
{
    "age": 30,
    "city": "New York",
    "has_children": false,
    "languages": [
        "English",  
        "Spanish",
        "French"
    ],
    "name": "John",
    "programming": {
        "experience": 5,
        "languages": [
            "Python",
            "Java"
        ]
    }
}
"""

# Writing the JSON data to a file
with open("person.json", "w") as file: # here we are writing the JSON data to a file
    json.dump(person, file, indent=4) # not dumps because we are writing to a file and not to the console

# Reading the JSON data from a file
with open("person.json", "r") as file: # here we are reading the JSON data from a file
    person = json.load(file)
    print(person)

# Output:
# {'name': 'John', 'age': 30, 'city': 'New York', 'languages': ['English', 'Spanish', 'French'], 'programming': {'languages': ['Python', 'Java'], 'experience': 5}, 'has_children': False}

# JSON to Python
person = json.loads(personJSON)
print(person)

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

user = User("John", 30)

userJSON = json.dumps(user.__dict__) # __dict__ is a dictionary that contains all the attributes of the object
print(userJSON)

# Output: {"name": "John", "age": 30}

print(type(userJSON)) # <class 'str'> --> This is not a dict but a string because we have converted the object to a JSON string

from json import JSONEncoder
# To make it a dict: 
"""
In the following code:
1. We have created a UserEncoder class that inherits from JSONEncoder.
2. We have overridden the default method to handle the User object.
3. If the object is an instance of User, we return a dictionary with the user's name and age.
4. We call the JSONEncoder's default method for other types of objects.
5. We have created an instance of the User class and converted it to a JSON string using the UserEncoder class.
6. We have converted the JSON string back to a dictionary using the json.loads method.
"""
class UserEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, User):
            return {"name": o.name, "age": o.age, o.__class__.__name__: True}
        return JSONEncoder.default(self, o)
    
userJSON2 = json.dumps(user, cls=UserEncoder)
print(userJSON2) # {"name": "John", "age": 30}

userJSON3 = json.loads(userJSON2)
print(type(userJSON3)) # <class 'dict'> --> This is a dict because we have converted the JSON string to a dict

# To decode:
# Which means: If the dictionary contains the key "name" and "age", then it is a User object.

def decode_user(dct):
    if User.__name__ in dct:
        return User(name=dct["name"], age=dct["age"])
    return dct

user = json.loads(userJSON2, object_hook=decode_user)
print(user.name) # John --> This is the name of the user object
print(user.age) # 30 --> This is the age of the user object
print(type(user)) # <class '__main__.User'> --> This is the type of the user object
