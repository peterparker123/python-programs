# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 11:31:53 2023

@author: Radhakrishna
"""

def outer_func():
    # Variable x is local for the outer function
    # This variable x will also create a binding for the inner function
    
    x = "hi"
    
    def inner_func():
        # x is not a local variable for the function now
        # but it persists through the entire functions or across the function
        nonlocal x
        x = "hello"
        return f'x from the inner function',x  
        
       
    print(inner_func())
    return f'x from the outer function', x


print(outer_func())