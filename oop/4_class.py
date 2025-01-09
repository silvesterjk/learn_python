class Student: 
    def __init__(self, name, house=None, patronus=None): # By adding None as default value, we can make the parameter optional.
        # Note: Place all non-default arguments before any default arguments. Here 'None' is a default argument.
        if not name:
            raise ValueError("Name is required.")
        if house is not None and house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house.")

        self.name = name
        self.house = house
        self.patronus = patronus

    def __str__(self):
        return f"{self.name} from {self.house} house with the partonus of {self.patronus}."
    
    def charm(self):
        match self.patronus:
            case "Stag":
                return "Produces a powerful, corporeal Patronus! 🐴"
            case "Otter":
                return "Produces a playful, corporeal Patronus! 🦦"
            case "Jack Russell Terrier":
                return "Produces a loyal, corporeal Patronus! 🐶"
            case _:
                return "Produces an incorporeal Patronus! 🪄"

def main():
    student = student_info()
    print("Expecto Patronum!")
    print(student.charm())

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