# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 11:47:04 2023

@author: Radhakrishna
"""

import copy

lst = [4,5,6]

lst1 = copy.copy(lst)

print("Memory address of first list: ", id(lst))
print("Memory address of second list: ", id(lst1))

# Modify the first list

lst.append(8)

print("First list after modification: ",lst)
print("Second list: ",lst1)

# Modify the second list

lst1.append(9)
print("First list :",lst)
print("Second list after modification: ",lst1)