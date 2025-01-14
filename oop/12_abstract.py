# Abstract Class: A class that cannot be instantiated. It is used as a base class for other classes; meant to be inherited (subclassed) but not instantiated.
# Benefits of Abstract Classes:
# 1. Prevents the instantiation of the class directly.
# 2. Requires children to implement (use inherited) the abstract methods.

from abc import ABC, abstractmethod # abc means Abstract Base Class

class Vehicle(ABC): # Abstract class

    @abstractmethod
    def drive(self):
        # We don't need to implement the method here.
        # We just need to define the method in the abstract class.
        # Because the method will be implemented in the subclass.
        pass

    @abstractmethod
    def stop(self):
        pass


class Car(Vehicle): # Subclass of Vehicle

    def drive(self):
        return "The car is driving."

    def stop(self):
        return "The car is stopping."

class Motorcycle(Vehicle):

    # def go(self): # This will not work as the go method is not implemented in the Vehicle class.
    #     return "The motorcycle is going."

    def drive(self):
        return "This motorcycle is driving."
    
    def stop(self):
        return "The motorcycle is stopping."

car = Car()
print(car.drive())
print(car.stop())

bike = Motorcycle()
# print(bike.go())
#  Would return an error because the bike method is not implemented in the Motorcycle class.
# TypeError: Can't instantiate abstract class Motorcycle without an implementation for abstract method 'drive'

print(bike.drive())
print(bike.stop())


class Boat(Vehicle):

    def drive(self):
        return "The boat is driving."

    # def stop(self):
    #     return "The boat is anchored."

    # Would return an error because the stop method is not implemented in the Boat class.
    # TypeError: Can't instantiate abstract class Boat without an implementation for abstract method 'stop'

boat = Boat()
print(boat.drive())