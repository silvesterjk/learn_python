class Student: 
    def __init__(self, name, house=None): # By adding None as default value, we can make the parameter optional.
        if not name:
            # print("Name is required.")
            # sys.exit("Name is required.") # sys.exit() is used to exit the program
            raise ValueError("Name is required.")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house.")

        self.name = name
        self.house = house

def main():
    student = student_info()
    print(f"Hello, {student.name} from {student.house} house!")

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