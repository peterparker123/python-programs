# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 11:07:21 2023

@author: Radhakrishna
"""

# list append function

# append function adds an element at the end of the list
# the data type which we provide gets added at the end 

lst = [1,2,3]

lst.append(4)
print(lst)

# adding a character

lst.append('a')

print(lst)

# adding a list data structure by using append
lst.append([1,2])

print(lst)

lst[5].append(3)

print(lst)
