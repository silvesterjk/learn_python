import random # To create pseudo random numbers

a = random.randint(0, 10) # This will generate a random number between 0 and 10. Includes 0 and 10
b = random.random() # This will generate a random float between 0 and 1. Includes 0 but excludes 1
c = random.uniform(1, 10) # This will generate a random float between 1 and 10. Includes 1 but excludes 10
d = random.choice([1, 2, 3, 4, 5]) # This will randomly select an element from the list
e = random.choices([1, 2, 3, 4, 5], k=3) # This will randomly select 3 elements from the list
f = random.shuffle([1, 2, 3, 4, 5]) # This will shuffle the list
g = random.sample([1, 2, 3, 4, 5], k=3) # This will randomly select 3 unique elements from the list
h = random.randrange(0, 101, 2) # This will generate a random number between 0 and 100 with a step of 2
i = random.normalvariate(0, 1) # This will generate a random float from a normal distribution with a mean of 0 and standard deviation of 1
j = random.seed(1) # This will set the seed to 1. This is used to generate the same random numbers every time
k = random.getstate() # This will get the current internal state of the random number generator
l = random.setstate(k) # This will set the internal state of the random number generator
m = random.getrandbits(16) # This will generate a random integer with 16 bits

# Usage of seed for reproducibility
random.seed(1)
print(random.randint(0, 10)) # 2
print(random.randint(0, 10)) # 9
print(random.randint(0, 10)) # 1

random.seed(2)
print(random.randint(0, 10)) # 8
print(random.randint(0, 10)) # 8
print(random.randint(0, 10)) # 6

# Due to security reasons the random module is not suitable for cryptographic purposes. Use secrets module instead.
# The secrets module is used for generating cryptographically strong random numbers suitable for managing data such as passwords, account authentication, security tokens, and related secrets.

import secrets
