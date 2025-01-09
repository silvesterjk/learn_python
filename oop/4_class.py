class Student: 
    def __init__(self, name, house=None, patronus=None): # By adding None as default value, we can make the parameter optional.
        # Note: Place all non-default arguments before any default arguments.
        if not name:
            raise ValueError("Name is required.")
        if house is not None and house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house.")

        self.name = name
        self.house = house
        self.patronus = patronus

    def __str__(self):
        return f"{self.name} from {self.house} house with the partonus of {self.patronus}."

def main():
    student = student_info()
    print(student)

def student_info():
        name = input("Enter your name: ")
        house = input("Enter your house: ")
        patronus = input("Enter your patronus: ")
        try:
            return Student(name, house, patronus)
        except ValueError as error:
            print(error)
            return student_info()
        
if __name__ == "__main__":
    main()