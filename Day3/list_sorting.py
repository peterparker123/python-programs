# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 12:46:32 2023

@author: Radhakrishna
"""

# Sorting of list
# sort() function - Sorts the list in place
# Default is always ascending 

import random

random.seed(6)

numbers_lst = random.sample(range(1,100),10)

print("Original unsorted list", numbers_lst)

# sorting the list by using the sort() function

# sort function does not have any return value
# as it modifies the original list

numbers_lst.sort()

print("List after sorting", numbers_lst)

# sorting in the decreasing order

numbers_lst.sort(reverse=True)
print("List after sorting in decreasing order", numbers_lst)