# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 11:21:20 2023

@author: Radhakrishna
"""

# Checks for the scope of variables from the nested function
# The nested function always tries to locate the variables
# declared in the outer function, and would give it the first priority

def outer_func():
    
    x = 'hi'
    
    def inner_func():
        
        
        return 'x from the inner function :', x
    
    print(inner_func())
    
    return 'x from the outer function :',x

print(outer_func())