# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 11:28:59 2023

@author: Radhakrishna
"""

# global variable x
x = "hi"

def outer_func():
    
    
    def inner_func():
        
     
        return 'x from the inner function :', x
    
    print(inner_func())
    
    return 'x from the outer function :',x

print(outer_func())