'''
SEQUENCES
- IMMUTABLE
    - strings
    - tuples
    - bytes
- MUTABLE
    - lists
    - byte arrays

IMMUTABLE SEQUENCES
- STRINGS AND BYTES
Textual data in Python is handle with str objects, more commonly known as strings. They are immutable sequences of unicode code points. Unicode code points can represent a character, but can also have other meanings, such as formatting data for example.
'''

# 4 ways to make a string
str1 = 'This is a string. We built it with single quote.'
str2 = "This is also a string, but built with double quotes."
str3 = '''This is built using triple quotes,
so it can span multiple lines.'''
str4 = """This too
is a multiline one
built with triple double-quotes."""

'''
>>> str4 #A
'This too\nis a multiline one\nbuilt with triple double-quotes.'
'''

'''
>>> print(str4) #B
This too
is a multiline one
built with triple double-quotes.
'''

'''
In #A and #B, we print str4, first implicity, then explicity using the print function. Why are they different?
'''

'''
Strings, like any sequence, have a length. You can get this by calling the len function:
>>> len (str1)
'''

'''
Encoding and decoding strings
'''

'''
Indexing and slicing strings
'''


'''
- TUPLES
A tuple is a sequence of arbitrary Python objects. In a tuple, items are separated by commas. They are used everywhere in Python, because they allow for pattern that are hard to reproduce in other languages. Sometimes tuples are used implicity, for example to set up multiple variables on one line, or to allow a function to return multiple different objects (usually a function returns one object only, in mamy other languages), and even in the Python console, you can use tuples implicity to print multiple elements with one single instruction.
'''

t = () # empty tuple
type(t)
one_element_tuple = (42, ) # you need the comma!
three_elements_tuple = (1, 3, 5)
a, b, c = 1, 2, 3 # tuple for multiple assignment
a, b, c # implicit tuple to print with one instruction
3 in three_elements_tuple # membership test

# Notice that the membership operator in can alse be used with lists, strings, dictionaries, and in general with collection and sequence objects.

# Notice that to create a tuple with one item, we need to put that comma after the item. The reason is that without the comma that item is just itself wrapped in braces, kind of in a redundant mathematical expression. Notice also that on assignment, braces are optional so my_tuple = 1, 2, 3 is the same as my_tuple = (1, 2, 3)

# swapping two values
a, b = 1, 2
c = a # we need three lines and a temporary var c
a = b
b = c
a, b # a and b have been swapped

# in Python, we would do swapping this way:
a, b = b, a # this is th Pythonic way to do it

# Because they're immutable, tuples can be used as keys for dictionaries