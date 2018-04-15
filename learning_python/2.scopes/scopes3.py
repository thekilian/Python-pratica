# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 20:10:28 2018

@author: vegetto
"""

# Local, Enclosing and Global

def enclosing_func():
    m = 13
    def local():
        # m doesn't belong to the scope defined by the local function so Python will keep looking into the next enclosing scope. This time m is found in the enclosing scope
        print(m, 'printing from the local scope')
        
    #calling the function local
    local()

m = 5
print(m, 'printing from the global scope')

enclosing_func()