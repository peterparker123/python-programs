# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 10:16:48 2023

@author: Radhakrishna
"""

# For the higher dimension the same rule applies
# The trailing dimnension should be equal
# And at least, one of them should be 1


import numpy as np


twod_arry = np.array([[3,5],[4,2]])

print(twod_arry.shape)

# Try to multiply this with a 1d array

oned_array = np.array([3,4])

print(oned_array.shape)

broadcasted_array = twod_arry * oned_array

print(broadcasted_array)