# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 10:03:06 2023

@author: Radhakrishna
"""

# split function
# returns the elements of the string in a list format


Str = "hello"

split_str = Str.split()

print(split_str)

Str = "hello world"
split_str = Str.split()
print(split_str)

Str = "This,is,my,string"

split_str = Str.split(sep=",")
print(split_str)