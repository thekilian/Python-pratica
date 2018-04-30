'''
NUMBERS
- Integers
- Booleans
- Reals
- Complex numbers
- Fractions and decimals

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


'''
BOOLEANS
Boolean algebra is that subset of algebra in which the values of the variables are the truth values: true and false. In Python, True and False are two keywords that are used to represent thuth values. Booleans are subclass of integers, and behave respectively like 1 and 0. The equivalent of the int class for Booleans is the bool class, which returns either True or False. Every built-in Python object has a value in the Boolean context, which means they basically evaluate to either True or False when fed to the bool function.
Boolean values can be combined in Boolean expressions using the logical operators and, or and not.

Examples:

int(True)
int(False)
bool(1)
bool(-42)
bool(0)

# quick pick at the operators (and, or, not)
not True
not False
True and True
False and True

# You can see that True and False are subclasses of integers when you try to add  them. Python upcasts* them to integers and perform addition:
1 + True
False + 42
7 - True

*Upcasting is a type conversion operation that goes from a subclass to its parent. In the example, True and False, which belong to a class that belong to a class derived from the integer class, are converted back to integers when needed.
'''

'''
REALS
Float point numbers
'''

pi = 3.1415926536
radius = 4.5
area = pi * (radius ** 2)
area

'''
The sys.float_info struct sequence holds information about how floating point numbers will behave on our system:
>>> import sys
>>> sys.float_info
sys.float_info(max=1.7976931348623157e+308, max_exp=1024, max_10_exp=308, min=2.2250738585072014e-308, min_exp=-1021, min_10_exp=-307, dig=15, mant_dig=53, epsilon=2.220446049250313e-16, radix=2, rounds=1)
P.S.: if you need to handle prices or financial calculations or any data that needs not to be approximated, you can use the Decimal type, which doesn't suffer from this issue. 
'''

'''
COMPLEX NUMBERS
Numbers that can be expressed in the form a + ib (a and b are real numbers, and i is the imaginary unit, that is, the square root of -1. a and b are called respectively the real and imaginary part of the number).
It's more used to code something scientific.

>>> c = 3.14 + 2.73j
>>> c.real # real part
3.14
>>> c.imag # imaginary part
2.73
>>> c.conjugate() # conjugate of A + Bj is S - Bj
(3.14-2.73j)
>>> c * 2 # multiplication is allowed
(6.28+5.46j)
>>> c ** 2 # power operation as well
(2.4067000000000007+17.1444j)
>>> d = 1 + 1j # addition and subtracrion as well
>>> c - d
(2.14+1.73j)
'''

'''
FRACTIONS AND DECIMALS
Fractions hold a rational numberator and deniminator in their lowest forms

>>> from fractions import Fraction
>>> Fraction(10, 6)
Fraction(5, 3) # notice it's been reduced to lowest terms
>>> Fraction(1, 3) + Fraction(2, 3) # 1/3 + 2/3 = 3/3 = 1/1
Fraction(1, 1)
>>> f = Fraction(10, 6)
>>> f.numerator
5
>>> f.denominator
3

# You can get and set the precision by accessing decimal.getcontext().prec
'''

'''
Decimal example:

>>> from decimal import Decimal as D # rename for brevity
>>> D(3.14) #pi, from float, so approximation issues
Decimal('3.140000000000000124344978758017532527446746826171875')
>>> D('3.14') #pi, from a string, so no approximation issues
Decimal('3.14')
>>> D(0.1) * D(3) - D(0.3) # from float we still have the issues
Decimal('2.775557561565156540423631668E-17')
>>> D('0.1') * D(3) - D('0.3') # from string, all perfect
Decimal('0.0')

# Notice that when we construct a Decimal number from a float, it takes on all the approximation issues the float may come from. On the other hand, when the Decimal has no approximation issues, for example, when we feed an int or a string representation to the constructor, then the calculation has no quirky behavior. When it comes to money, use decimals.
'''