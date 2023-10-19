# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 11:58:25 2023

@author: Radhakrishna
"""

# built in scope
# In python, the first priority to any variable is always in the local scope
# if the function cannot find a variable in it's local scope, then it checks in it's global scope
# if the function cannot find a variable in it's global scope, then it checks in the built-in scope

def func(len):
    
    return len


print(func('hello'))


def len():
    return 
    