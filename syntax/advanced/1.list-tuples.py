"""LIST: ordered and changeable. Allows duplicate elements"""

mylist = [1, 3, 2, 4, 5]
print(mylist[1:3])  # Outputs: [2, 3]

for i in mylist:
    print (i)

if 1 in mylist:
    print("yes")

print(len(mylist))

mylist.append(6)
print(mylist)

mylist.insert(1, 7) # insert 7 at index 1
print(mylist)

mylist.remove(7) # remove 7 from list -- rermove first occurance of the value
mylist.pop() # remove last element and also return it. we can assign it to a variable if we want to use it later

print(mylist) # [1, 2, 3, 4, 5]
reverse_item = mylist.reverse() # reverse the list. We have assigned it to a new variable because reverse() method does not return anything.
print(mylist) # None. But printing reverse_item will give None. Because reverse() method does not return anything.

sort_item = mylist.sort() # sort the list

# clear_item = mylist.clear() # clear the list

newlist = [0] * 5
newlist2 = [3, 5, 6, 7, 8]

newlist = mylist + newlist2
print(newlist)

list_org = ["apple", "banana", "cherry"]
list_copy = list_org
list_copy2 = list_org.copy()


list_copy.append("orange")

print(list_org) # ['apple', 'banana', 'cherry', 'orange']
print(list_copy) # ['apple', 'banana', 'cherry', 'orange'] because list_copy is just a reference to list_org
print(list_copy2) # ['apple', 'banana', 'cherry'] because list_copy2 is a copy of list_org

# List comprehension
a = [1, 2, 3, 4, 5]
b = [i*i for i in a] # [1, 4, 9, 16, 25]  -- square of each element in list a -- Expression first - for each element in list a

"""TUPLE: orrdered and immutable. Allows duplicate elements"""

mytuple = ("apple", "banana", "cherry", 2, 2, 2.2)
# If there is only one value in tuple, then we need to add a comma after the value
# mytuple = ("apple",) # tuple
# mytuple = ("apple") # string

print(mytuple[1:3]) # ('banana', 'cherry')

mynewtuple = tuple(["apple", "banana", "cherry"]) # create a tuple using tuple() constructor
print(mynewtuple)

t_item = mytuple[0]
print(t_item) # apple

# mytuple[0] = "orange" # TypeError: 'tuple' object does not support item assignment

for x in mytuple:
    print(x) # apple banana cherry 2 2.2

if "apple" in mytuple:
    print("yes")
else:
    print("no")

print(len(mytuple)) # 5
print(mytuple.count(2)) # 2

print(mytuple.index(2.2)) # 5 is the first occurance of 2.2


# # Tuple unpacking
# a, b, c, d, e = mytuple  # apple banana cherry 2 2.2
