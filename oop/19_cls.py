# Class methods are methods that belong to the class and not to the object.
# They are defined using the @classmethod decorator.
# They have access to the class state and not the object's state. They take cls as the first argument/parameter.

class Student:

    count = 0 # Class variable

    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
        Student.count += 1

    # This is an instance method. It has access to the object's state.
    def display_student(self):
        return f'{self.name} is {self.age} years old and is in grade {self.grade}.'
    
    # This is a class method. It has access to the class state and not the object's state.
    @classmethod
    def total_students(cls):
        return f'There are {cls.count} students in the class.'

student1 = Student("John Doe", 30, 5)
student2 = Student("Jane Doe", 25, 4)
student3 = Student("Alice", 35, 6)

print(student1.display_student()) # This is how to call an instance method. You need to create an instance of the class to call an instance method.
print(Student.total_students()) # This is how to call a class method. You do not need to create an instance of the class to call a class method.