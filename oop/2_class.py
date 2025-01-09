"""
Classes can have attributes and methods. Attributes are variables that store data. Methods are functions that perform actions. 
The __init__ method is a special method that initializes an object. It is called a constructor. 
The self parameter refers to the current instance of the class. It is used to access variables and methods of the class. 
The __init__ method is called when an object is created. It initializes the object's attributes. The object is passed to the self parameter. 
The __init__ method can also accept other parameters. These parameters are used to initialize the object's attributes. 
The __init__ method can have default values for its parameters. These values are used if no argument is provided. 
The __init__ method can have multiple parameters. The parameters are used to initialize the object's attributes.
"""
    
class Student: 
    def __init__(self, name = "Harry Potter", house = "Gryffindor"): # constructor
        self.name = name
        self.house = house

def main():
    student = student_info()
    print(f"Hello, {student.name} from {student.house} house!")

def student_info():
        name = input("Enter your name: ")
        house = input("Enter your house: ")
        student = Student(name, house) # passing variables to the constructor
        return student

if __name__ == "__main__":
    main()