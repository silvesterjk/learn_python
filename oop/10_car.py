from _class import Car

car1 = Car("Toyota", 2021, "Red", True)
print(car1.__dict__)
car2 = Car("Honda", 2022, "Blue", False)
print(vars(car2))
car3 = Car("Ford", 2023, "Green", True)
print(vars(car3))

# The __dict__ attribute is a dictionary that contains the object's attributes.
# The vars() function is a built-in function that returns the __dict__ attribute of an object.
# __str__ can be called using the print() function. For example, print(car1) will call the __str__ method of the Car class.
print(car1)
print(car1.drive())
print(car1.description())


# Class variables are shared among all instances of a class. They are defined outside the __init__ method.
# Instance variables are unique to each instance of a class. They are defined inside the __init__ method.
# Class variables are accessed using the class name. For example, Car.wheels.
# Instance variables are accessed using the self keyword. For example, self.model.
# Inheritance is a way to create a new class from an existing class. The new class is called a subclass, and the existing class is called a superclass.
# Inheritance allows you to reuse code and create a hierarchy of classes.

