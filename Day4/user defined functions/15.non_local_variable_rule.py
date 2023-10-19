# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 11:36:32 2023

@author: Radhakrishna
"""


def outer_func():
    # no local or global variable x exists in the outer function
   # x = "hi"
    
    def inner_func():
        nonlocal x
        x = "hello"
        return x
    
    print(inner_func())
    return x


print(outer_func())