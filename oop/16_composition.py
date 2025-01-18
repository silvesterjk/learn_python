# Aggregation = A relationship where one object contains references to other INDEPENDENT objects
            #   With a 'has-a' releatiobship

# Composition = The composed object directly owns its components, which cannot exist independently
            #   With a 'owns-a' relationship


# Example of Composition

class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

class Wheels:
    def __init__(self, size):
        self.num_wheels = size

class Car:
    def __init__(self, make, model, horsepower, wheel_size):
        self.make = make
        self.model = model
        self.engine = Engine(horsepower)
        self.wheels = [Wheels(wheel_size) for wheel in range(4)]
    
    def display_car(self):
        return f'{self.make} {self.model} with {self.engine.horsepower} hp and {self.wheels[0].num_wheels} wheels'


car1 = Car("Toyota", "Corolla", 100, 16)
print(car1.display_car())

car2 = Car(make="Honda", model="Civic", horsepower=150, wheel_size=17)
print(car2.display_car())

# If car1 and  car2 are to be destroyed, the engine and wheels objects will also be destroyed.
# That is why the relationship between the Car class and the Engine and Wheels classes is a composition relationship.