# Inheritance.
# Inheritance is a way to form new classes using classes that have already been defined.

# class Student:
#     def __init__(self, name, house):
#         if not name:
#             raise ValueError("Name is required.")  
#         self.name = name
#         self.house = house

#     ...


# class Professor:
#     def __init__(self, name, subject):
#         if not name:
#             raise ValueError("Name is required.")
#         self.name = name
#         self.subject = subject


# In the above case we duplicated the code for checking if name is provided.

class Wizard: # Parent class
    def __init__(self, name, age):
        if not name:
            raise ValueError("Name is required.")  
        self.name = name
        if not isinstance(age, int) or not (1 <= age <= 150):
            # isinstance returns True if the object is an instance of the class or subclass
            # For example, isinstance(1, int) returns True
            raise ValueError("Age must be an integer between 1 and 150.")
        self.age = age

class Student(Wizard): # Child class
    def __init__(self, name, age, _class):
        super().__init__(name, age) # Because we are inheriting from Wizard, we need to call the __init__ method of the parent class
        self._class = _class

class Professor(Wizard): # Child class
    def __init__(self, name, age, subject):
        super().__init__(name, age) # Because we are inheriting from Wizard, we need to call the __init__ method of the parent class
        self.subject = subject

student = Student("Harry Potter", 11, "Gryffindor")
professor = Professor("Severus Snape", 38, "Potions")

print(student.__dict__) # We added __dict__ to print the attributes of the object. Alternatively, we can use vars(student)
print(vars(professor)) # vars() is a built-in function that returns the __dict__ attribute of an object
