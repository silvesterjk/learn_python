from car_class import Car

car1 = Car("Toyota", 2021, "Red", True)
print(car1.__dict__)
car2 = Car("Honda", 2022, "Blue", False)
print(vars(car2))
car3 = Car("Ford", 2023, "Green", True)
print(vars(car3))

# The __dict__ attribute is a dictionary that contains the object's attributes.
# The vars() function is a built-in function that returns the __dict__ attribute of an object.
print(car1)
print(car1.drive())
print(car1.description())


# Class variables are shared among all instances of a class. They are defined outside the __init__ method.
# __str__ can be called using the print() function. For example, print(car1) will call the __str__ method of the Car class.