# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 20:00:47 2018

@author: vegetto
"""

# Learning Python - Scopes, p. 27

'''
The order in whinch the namespaces are scanned when looking for a name is: local, enclosing, global, built-in (LEGB)
'''


# Local versus Global

# we define a function, called lcoal
def local():
    m = 7
    print(m)

m = 5
print(m)

# we call, or 'execute' the function local
local()

# terminal command: (activate virtualenv) $ python scopes1.py