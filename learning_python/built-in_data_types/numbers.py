'''
Numbers are immutable objects

INTEGERS
It doesn't matter how big the number you want to store - as long as it can fir in your computer's memory, Python will take care of it.
'''

a = 12
b = 3

a + b
b - a
a // b
a / b
a * b
b ** a
2 ** 1024

'''
About division:
Python has two division operators:
- true division (/)
- integer division (//)
'''

7 / 4 # true division
# 1.75

7 // 4 # integer division, flooring returns 1
# 1

-7 / 4 # true division (result is opposite of previous)
# -1.75

-7 // 4 # true division (result is NOT the opposite of previous)
# -2

# The result of an integer division in Python is always rounded towards minus infinity.


'''
If instead of flooring you want to truncate a number to an integer, you can use the built-in int fucntion:
'''

int(1.75) # 1
int(-1.75) # -1

# Truncation is done towards 0

'''
There is also an operator to calculate the reminder of a division. It's called modulo operator, and it's represented by a percent (%):
'''

10 % 3 # reminder of the division 10 // 3
# 1
10 % 4 # reminder of the division 10 // 4
# 2