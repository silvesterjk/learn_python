# ITERTOOLS: product, permutations, combinations, accumulate, groupby, and infinite iterators

# product: cartesian product of input iterables
from itertools import product
a = [1, 2]
b = [3, 4]
prod = product(a, b)

print(list(prod)) # [(1, 3), (1, 4), (2, 3), (2, 4)]
prod2 = product(a, b, repeat=2)
print(list(prod2)) 
"""
[(1, 3, 1, 3), (1, 3, 1, 4), (1, 3, 2, 3), (1, 3, 2, 4), (1, 4, 1, 3), 
(1, 4, 1, 4), (1, 4, 2, 3), (1, 4, 2, 4), (2, 3, 1, 3), (2, 3, 1, 4), 
(2, 3, 2, 3), (2, 3, 2, 4), (2, 4, 1, 3), (2, 4, 1, 4), (2, 4, 2, 3), (2, 4, 2, 4)]
"""

# permutations: all possible orderings of an input iterable
from itertools import permutations
a = [1, 2, 3]
perm = permutations(a)
print(list(perm)) # [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]
perm2 = permutations(a, 2) # length of the permutation is 2
print(list(perm2)) # [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]

# combinations: all possible combinations of an input iterable
from itertools import combinations, combinations_with_replacement
a = [1, 2, 3, 4]
comb = combinations(a, 2) # length of the combination is 2
print(list(comb)) # [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]

comb_wr = combinations_with_replacement(a, 2) # length of the combination is 2 with replacement of the elements in the iterable
print(list(comb_wr)) # [(1, 1), (1, 2), (1, 3), (1, 4), (2, 2), (2, 3), (2, 4), (3, 3), (3, 4), (4, 4)]

# accumulate: returns accumulated sums or products
from itertools import accumulate
import operator
a = [1, 2, 3, 4]
acc = accumulate(a)
print(a) # [1, 2, 3, 4]
print(list(acc)) # [1, 3, 6, 10] --> 1+2 = 3, 3+3 = 6, 6+4 = 10
acc2 = accumulate(a, func=max)  # returns the maximum value of the accumulated sum
print(list(acc2)) # [1, 2, 3, 4] --> 1, 2, 3, 4 are the maximum values at each index\
acc3 = accumulate(a, func=min)  # returns the minimum value of the accumulated sum
print(list(acc3)) # [1, 1, 1, 1] --> 1, 1, 1, 1 are the minimum values at each index
acc4 = accumulate(a, func=lambda x, y: x*y)  # returns the product of the accumulated sum
print(list(acc4)) # [1, 2, 6, 24] --> 1*2 = 2, 2*3 = 6, 6*4 = 24
acc5 = accumulate(a, func=operator.mul)  # returns the division of the accumulated sum
print(list(acc5)) # [1, 2, 6, 24] --> 1*2 = 2, 2*3 = 6, 6*4 = 24

# groupby: groups consecutive elements based on a key
from itertools import groupby
a = [1, 2, 3, 4]
group_obj = groupby(a, key=lambda x: x<3) # groups the elements based on the key
for key, value in group_obj:
    print(key, list(value))
"""
True [1, 2]
False [3, 4]
""" 

persons = [{'name': 'Tim', 'age': 25}, {'name': 'Dan', 'age': 25},
           {'name': 'Lisa', 'age': 27}, {'name': 'Claire', 'age': 28}]
group_obj = groupby(persons, key=lambda x: x['age'])
for key, value in group_obj:
    print(key, list(value))

# Infinite iterators: count, cycle, repeat
from itertools import count, cycle, repeat

for i in count(10): # starts from 10 and goes on infinitely
    print(i)
    if i == 15:
        break

a = [1, 2, 3]
for i in cycle(a): # cycles through the elements in the list infinitely
    print(i)
    if i == 3:
        break

for i in repeat(1, 4): # repeats the element 1 four times
    print(i)

# LAMBDA FUNCTIONS

# lambda arguments: expression | lambda x: x+10
add10 = lambda x: x+10
print(add10(5)) # 15

mult = lambda x, y: x*y
print(mult(2, 7)) # 14

sorted_list = sorted([5, 2, 3, 1, 4], key=lambda x: x) # sorts the list in ascending order
print(sorted_list) # [1, 2, 3, 4, 5]

reverse_sorted_list = sorted([5, 2, 3, 1, 4], key=lambda x: -x) # sorts the list in descending order
print(reverse_sorted_list) # [5, 4, 3, 2, 1]

# map function --> map(function, iterable)
a = [1, 2, 3, 4]
b = map(lambda x: x*2, a) # multiplies each element in the list by 2
print(list(b)) # [2, 4, 6, 8] | map cannot be printed directly as it returns an iterator object

# Similarly:
c = [x*2 for x in a]
print(c) # [2, 4, 6, 8] | List comprehension can also be used to achieve the same result

# filter function --> filter(function, iterable)
a = [1, 2, 3, 4, 5, 6]
b = filter(lambda x: x%2==0, a) # filters the even elements from the list | % is modulo operator not division
print(list(b)) # [2, 4, 6] | filter cannot be printed directly as it returns an iterator object

# Similarly:
c = [x for x in a if x%2==0] # % is modulo operator not division
print(c) # [2, 4, 6] | List comprehension can also be used to achieve the same result


"""
1 lambda functions are used when we require a nameless function for a short period of time.
2 They are defined using the lambda keyword.
3 They can have any number of arguments but only one expression.
4 They are syntactically restricted to a single expression.
"""

# reduce function --> reduce(function, iterable)
from functools import reduce
a = [1, 2, 3, 4]
product_a = reduce(lambda x, y: x*y, a) # multiplies all the elements in the list
print(product_a) # 24 | 1*2 = 2, 2*3 = 6, 6*4 = 24 | reduce cannot be printed directly as it returns an iterator object