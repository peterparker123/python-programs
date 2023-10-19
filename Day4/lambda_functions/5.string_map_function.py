# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 13:51:24 2023

@author: Radhakrishna
"""

# list of strings with a map function

lst = ["john","max","charles","francis"]

mapped_str = map(len,lst)

upper_str = map(str.upper,lst)

print(list(mapped_str))

print(list(upper_str))