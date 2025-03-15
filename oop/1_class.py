class Student: # This is a class. The blueprint/template for creating new data types / objects.
    ...

def main():
    student = student_info()
    print(f"Hello, {student.name} from {student.house} house!")

def student_info():
    student = Student() 
    #`Student` is a class, and `student` is an object. 
    # Here class is the blueprint and object is the actual thing created from the blueprint.
    student.name = input("Enter your name: ") # We don't use square brackets as in dict. here because classes use dot notation
    student.house = input("Enter your house: ")
    return student

if __name__ == "__main__":
    main()