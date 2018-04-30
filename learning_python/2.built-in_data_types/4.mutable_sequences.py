'''
MUTABLE SEQUENCES
Mutable sequences can be changed after creation.
(if dictionary is the king of data structures in Python, list is its rightful queen)

- LISTS
Very similar to tuples, but they don't have the restrictions due to immutability. Lists are common used to store collections of homogeneous objects, but there is nothing preventing you to store heterogeneous collections as well.
They can be created in many different ways:
'''


[] # empty list
# []
list() # same as []
# []
[1, 2, 3] #as with tuples, item are comma separated
# [1, 2, 3]
[x + 5 for x in [2, 3, 4]] # Python is magic
# [7, 8, 9]
list((1, 3, 5, 7, 9)) # list from a tuple
# [1, 3, 5, 7, 9]
list('hello') # list from a string
# ['h', 'e', 'l', 'l', 'o']


'''
List Methods:
append
count
extend
index
insert
pop
remove
reverse
sort
clear
min
sum
len
'''

a = [1, 2, 1, 3]

a.append(13) # we can append anything at the end
a
# [1, 2, 1, 3, 13]

a.count(1) # how many '1' are there in the list?
# 2

a.extend([5, 7]) # extend the list by another (or sequence)
a
# [1, 2, 1, 3, 13, 5, 7]

a.index(13) # position of '13' in the list (0-based indexing)
# 4

a.insert(0, 17) # insert '17' at position 0
a
# [17, 1, 2, 1, 3, 13, 5, 7]

a.pop() # (remove and return) last element
# 7 

a.pop(3) # pop alement at position 3
# 1

a
# [17, 1, 2, 3, 13, 5]

a.remove(17) # remove '17'from the list
a
# [1, 2, 3, 13, 5]

a.reverse() # reverse the order of the elements in the list
a
# [5, 13, 3, 2, 1]

a.sort() # sort the list
a
# [1, 2, 3, 5, 13]

a.clear() # remove all elements from the list
a
# []

# you can extend lists using any sequence type:

a = list('hello') # makes a list from a string
a
# ['h', 'e', 'l', 'l', 'o']

a.append(100) # append 100, heterogeneous type
a
# ['h', 'e', 'l', 'l', 'o', 100]

a.extend((1, 2, 3)) # extend using tuple
a
# ['h', 'e', 'l', 'l', 'o', 100, 1, 2, 3]

a.extend('...') # extend using string
a
# ['h', 'e', 'l', 'l', 'o', 100, 1, 2, 3, '.', '.', '.']

# the most common operations with lists:
a = [1, 3, 5, 7]

min(a) # minimum value in a list
# 1
max(a) # maximun value in a list
# 7
sum(a) # sum of all values in the lsit
# 16
len(a) # number of elements in the list
# 4

b = [6, 7, 8]
a + b # '+' with list means concatenation
# [1, 3, 5, 7, 6, 7, 8]
a * 2 # '*' has also a special meaning
# [1, 3, 5, 7, 1, 3, 5, 7]

# operator overloading - operators such as +, -, *, %, and so on, may represent different operations according to the context they are used in.

# example of the power of the sort method:
from operator import itemgetter
a = [(5, 3), (1, 3), (1, 2), (2, -1), (4, 9)]
sorted(a)
# [(1, 2), (1, 3), (2, -1), (4, 9), (5, 3)]
sorted(a, key=itemgetter(0))
# [(1, 3), (1, 2), (2, -1), (4, 9), (5, 3)]
sorted(a, key=itemgetter(0, 1))
# [(1, 2), (1, 3), (2, -1), (4, 9), (5, 3)]
sorted(a, key=itemgetter(1))
# [(2, -1), (1, 2), (5, 3), (1, 3), (4, 9)]
sorted(a, key=itemgetter(1), reverse=True)
# [(4, 9), (5, 3), (1, 3), (1, 2), (2, -1)]


'''
- BYTE ARRAYS

'''