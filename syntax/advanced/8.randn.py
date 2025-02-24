# RANDOM NUMBERS

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

aa = secrets.randbelow(10) # This will generate a random number between 0 and 9. Includes 0 but excludes 10
bb = secrets.randbits(16) # This will generate a random integer with 16 bits
cc = secrets.choice([1, 2, 3, 4, 5]) # This will randomly select an element from the list
dd = secrets.token_bytes(16) # This will generate a random byte string with 16 bytes
ee = secrets.token_hex(16) # This will generate a random hexadecimal string with 16 bytes
ff = secrets.token_urlsafe(16) # This will generate a random URL-safe string with 16 bytes


# With NumPy
# NumPy is a library for the Python programming language, adding support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays.

import numpy as np

# Random numbers from a uniform distribution
a = np.random.rand(3, 2) # This will generate a 3x2 array of random numbers from a uniform distribution --> print(a) --> [[0.5488135  0.71518937] [0.60276338 0.54488318] [0.4236548  0.64589411]]
b = np.random.randint(0, 10, (3, 3)) # This will generate a 3x3 array of random integers between 0 and 10 --> print(b) --> [[3 7 9] [3 7 2] [9 2 3]]
# For higher dimensions:
c = np.random.randint(0, 10, (3, 3, 3)) # This will generate a 3x3x3 array of random integers between 0 and 10 --> print(c) --> [[[3 5 2] [4 7 6] [8 8 1]] [[6 7 7] [8 1 5] [9 8 9]] [[4 3 0] [3 5 0] [2 3 8]]]
d = np.random.choice([1, 2, 3, 4, 5], 3) # This will randomly select 3 elements from the list --> print(d) --> [3 4 2]
e = np.random.choice([1, 2, 3, 4, 5], 3, replace=False) # This will randomly select 3 unique elements from the list --> print(e) --> [2 4 1]
f = np.array([1, 2, 3], [4, 5, 6], [7, 8, 9])
np.random.shuffle(f) # This will shuffle the array f --> print(f) --> [[7 8 9] [1 2 3] [4 5 6]] -- Only shuffles the first axis of a multi-dimensional array

# Using seed
np.random.seed(1)
print(np.random.rand(2, 2)) # [[4.17022005e-01 7.20324493e-01] [1.14374817e-04 3.02332573e-01]]

np.random.seed(1)
print(np.random.rand(2, 2)) # [[4.17022005e-01 7.20324493e-01] [1.14374817e-04 3.02332573e-01]]