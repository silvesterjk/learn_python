
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

