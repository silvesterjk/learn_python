"""ARGS"""

def myfunc(a, b, c, *args):
    print(a, b, c)
    for arg in args:
        print(arg)

myfunc(1, 2, 3, 4, 5)

# Output:
# 1 2 3
# 4
# 5

def myfunc(a, b, c, *args):
    print(a, b, c)
    for arg in args:
        print(arg)

myfunc(1, 2, 3, 4, 5, 6, 7, 8, 9)

# Output:
# 1 2 3
# 4
# 5
# 6
# 7
# 8
# 9


"""KWARGS"""

def myfunc(a, b, c, *args, **kwargs):
    print(a, b, c)
    for arg in args:
        print(arg)
    for key in kwargs:
        print(key, kwargs[key]) 

myfunc(1, 2, 3, 4, 5, 6, 7, 8, 9, name="John", age=30)

# Output:
# 1 2 3
# 4
# 5
# 6
# 7
# 8
# 9
# name John
# age 30


"""ARGS AND KWARGS"""

def myfunc(*args, **kwargs):
    for arg in args:
        print(arg)
    for key in kwargs:
        print(key, kwargs[key])

myfunc(1, 2, 3, name="John", age=30)

# Output:
# 1
# 2
# 3
# name John
# age 30

def myfunc(a,b,*,c,d): # This will only accept c and d as keyword arguments
    print(a,b,c,d)

myfunc(1,2,c=3,d=4) # This will print 1 2 3 4

# myfunc(1,2,3,4) # This will raise a TypeError because c and d are not keyword arguments

