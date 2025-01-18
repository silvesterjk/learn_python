# Statics methods are methods that belong to the class and not to the object.
# They are defined using the @staticmethod decorator.
# They do not have access to the object's state.

# Instance Methods: They have access to the object's state. Best for working with the object's state.
# Static Methods: They do not have access to the object's state. Best for utility functions that do not require access to the object's state.
                  # Such as converting units, etc.

class Employee:
    def __init__(self, name, age, position):
        self.name = name
        self.age = age
        self.position = position

    def display_employee(self):
        return f'{self.name} is a {self.position} and is {self.age} years old.'

    @staticmethod # This decorator is used to define a static method
    def is_adult(age):
        return age >= 18

    @staticmethod
    def is_senior(age):
        return age >= 60
    
employee1 = Employee("John Doe", 30, "Software Engineer") # This is an instance of the Employee class. Which is not required for static methods.
employee2 = Employee("Jane Doe", 25, "Data Scientist")
employee3 = Employee("Alice", 35, "Product Manager")


print(employee1.display_employee()) # This is how to call an instance method. You need to create an instance of the class to call an instance method.

print(Employee.is_adult(30)) # This is how to call a static method. You do not need to create an instance of the class to call a static method.
# This is a general method that can be used by all instances of the class. Utility functions that do not require access to the object's state.