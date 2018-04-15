'''
BUILT-IN DATA TYPES

Mutable - the value can change
Immutable - the value cannot change
'''

# Immutable object

age = 99
id(age)

age = 100
id(age)

'''
We didn't change 99 to 100. We actually just pointed age to a different location: the new int object whose value is 100.
We print the IDs by calling the built-in id function.
'''

# Mutable object

'''
fab = Person(age=99)
fab.age
# 99
id(fab)
# some numbers here
fab.age = 100
id(fab)
# same 'some numbers here'
'''