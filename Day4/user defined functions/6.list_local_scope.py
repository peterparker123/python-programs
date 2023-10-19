# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 10:52:13 2023

@author: Radhakrishna
"""

# scoping of mutable object

def func(lst = []):
    lst = [i for i in range(1,10)]
    return lst

print(func())
