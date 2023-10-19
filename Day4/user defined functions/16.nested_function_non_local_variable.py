# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 11:47:20 2023

@author: Radhakrishna
"""

def outer_func():
    # Variable x is local for the outer function
    # This variable x will also create a binding for the inner function
    
    x = "hi"
    
    def inner_func():
        nonlocal x
        x = "hello"
        
        def innermost_func():
            nonlocal x
            x = "lambu"
            return x # innermost function x
        print('x from the innermost function',innermost_func())
        
        return x # inner function x
    print('x from the inner function', inner_func())
        
    return x # outer function x


print('x from the outer function: ', outer_func())