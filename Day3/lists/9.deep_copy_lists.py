# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 12:00:52 2023

@author: Radhakrishna
"""

import copy
from copy import deepcopy

# If we have a sublist inside a list
# we want to ensure that those sublists also gets copied element by element
# instead of the memory address

# Deep copying operation
print("---Deep Copying Operation----")

lst = [1,2,[4,5]]

lst_deep_copy = copy.deepcopy(lst)

# Modify the first list

lst.append(3)
print("First list after modification: ", lst)
print("Deep copied list: ", lst_deep_copy)

# Modify the sublist in the original list
lst[2].append(6)

print("First list after modification: ", lst)
print("Deep copied list: ", lst_deep_copy)

print("Memory address of sublist in first list: ", id(lst[2]))
print("Memory address of sublist in shallow copied list: ", id(lst_deep_copy[2]))





