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