# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 09:50:59 2023

@author: Radhakrishna
"""

# Broadcasting operation in numpy array signifies that the scalar or the 
# array gets stretched so that it does not need to create multiple copies
# By using Broadcasting, the numpy array saves lot of memory for the computation

import numpy as np

# Broadcasting of the scalar value

a = np.arange(10)
print(a.shape)

print("The original array: ",a)

# Multiply the above array with the value a
broadcasted_array = a * 2

print("The broadcasted array:" , broadcasted_array)


# broadcasting with the array
# In this case, we need to ensure that broadcasting is done with the
# arrays which have similar dimensions

b = np.arange(3)

broadcasted_array = a * b

print(broadcasted_array)