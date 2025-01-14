from _class import Prey, Predator, Rabbit, Hawk, Fish

# Create an instance of the Rabbit class
fish = Fish("Nemo", 2)
print(fish.__dict__)

print(fish.name)
print(fish.age)

print(fish.eat_fish())
print(fish.hunt_fish())
print(fish.eat())
print(fish.sleep())