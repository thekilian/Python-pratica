# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 20:07:55 2018

@author: vegetto
"""

# Local versus Global

def local():
    # m doesn't belong to the scope defined by the local function so Python will keep looking into the next enclosing scope. m is finally found in the global scope
    print(m, 'printing from the local scope')
    
m = 5
print(m, 'printing from the global scope')

local()