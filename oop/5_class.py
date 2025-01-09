# Decorators in Python modify/enhance behavior of functions or methods.
# Properties in Python are special attributes that provide getter, setter, and deleter methods.

class Student: 
    def __init__(self, name, house=None):
        self.name = name
        self.house = house # reason for not using _house here is to avoid overwriting the house property

    def __str__(self):
        return f"{self.name} from {self.house} house."
    
    @property
    def name(self):
        return self._name # _name because we don't want to overwrite the name property
        # _ is python convention to indicate that a variable is private
        # It is not enforced by the language, but it is a convention that is widely followed.
    
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Name is required.")
        self._name = name
    
    # Getter
    @property
    def house(self):
        return self._house
    
    # Setter
    @house.setter
    def house(self, house):
        if house is not None and house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house.")
        self._house = house # _house becuase we don't want to overwrite the house property

def main():
    student = student_info()
    print(student)

def student_info():
        name = input("Enter your name: ")
        house = input("Enter your house: ")
        try:
            return Student(name, house)
        except ValueError as error:
            print(error)
            return student_info()
        
if __name__ == "__main__":
    main()


"""

# Decorators in Python modify/enhance behavior of functions or methods.
# Example of a simple decorator:
def simple_decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@simple_decorator  # Applying the decorator
def say_hello():
    print("Hello!")

say_hello()

# @property is a built-in decorator for creating getters/setters.
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property  # Getter for radius
    def radius(self):
        return self._radius

    @radius.setter  # Setter for radius
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value

c = Circle(5)
print(c.radius)  # Access property
c.radius = 10    # Modify property

"""