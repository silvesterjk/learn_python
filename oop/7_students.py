class Student: 
    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house} house."
    
    @classmethod
    def get(cls):
        name = input("Enter your name: ")
        house = input("Enter your house: ")
        try:
            return cls(name, house)
        except ValueError as error:
            print(error)
            return cls.get()
    
    # Getter
    @property
    def name(self):
        return self._name 
    
    #Setter
    @name.setter
    def name(self, name):
        if not name: raise ValueError("Name is required.")
        self._name = name
    
    @property
    def house(self):
        return self._house
    
    @house.setter
    def house(self, house):
        valid_houses = {"Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"}
        if house is not None and house not in valid_houses:
            raise ValueError("Invalid house.")
        self._house = house 

def main():
    student = Student.get()
    print(student)

if __name__ == "__main__":
    main()