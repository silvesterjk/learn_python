"""
name = input("Name of student: ")
house = input("House of house: ")
print(f"{name} is in the house {house}.")
"""

def main():
    name = get_name()
    house = get_house()
    print(f"{name} is in the house {house}.")

def get_name():
    return input("Name of student: ")

def get_house():
    return input("House of house: ")

if __name__ == "__main__":
    main()