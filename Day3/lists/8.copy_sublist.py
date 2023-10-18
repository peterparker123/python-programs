# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 12:08:30 2023

@author: Radhakrishna
"""

import copy
# If we have a sublist inside a list
# we want to ensure that those sublists also gets copied element by element
# instead of the memory address

lst = [1,2,[4,5]]

# Shallow copy operation

lst_shallow_copy = copy.copy(lst)

# Modify the first list

lst.append(3)
print("First list after modification: ", lst)
print("Shallow copied list: ", lst_shallow_copy)

# Modify the sublist in the original list
lst[2].append(6)

print("First list after modification: ", lst)
print("Shallow copied list: ", lst_shallow_copy)

print("Memory address of sublist in first list: ", id(lst[2]))
print("Memory address of sublist in shallow copied list: ", id(lst_shallow_copy[2]))
