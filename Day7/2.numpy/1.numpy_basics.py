# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 11:14:41 2023

@author: Radhakrishna
"""

import numpy as np

# Creating an one dimensional array

myarr = np.array([1,2,3,4])


print(myarr)
print(type(myarr))

# Create an array by using arange function

myarr = np.arange(10)
print(myarr)
print("Python list : " , list(myarr))
# specify the dtype of the object

float_arr = np.arange(10,dtype=float)

print(float_arr)

# Creating twod array

twod_arr =np.array([[1,2],[3,4]])
print(twod_arr)

# checking the dimension of a numpy array
# shape function specifies the number of dimension of a numpy arr
print(twod_arr.shape)
# size specifies the total length of the numpy array
print(twod_arr.size)

threed_arr = np.array([[[1,2,3],[4,5,6],[7,8,9]]])
print(threed_arr)

threed_arr = np.array([[[1,2],[4,5],[7,8]]])
print(threed_arr)

print(threed_arr.shape)


threed_arr = np.array([[
                        [1,2,3],
                        [4,5,6]
                        ],    
                        [[7,8,9],
                        [10,11,12]
                    ]])
print(threed_arr)
print(threed_arr.shape)


