# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 10:23:54 2023

@author: Radhakrishna
"""

# Broadcasting on the 3d array

import numpy as np


threed_array = np.array([[
                        [3,4,5],[6,7,8]],
                        [[9,10,11],[12,13,14]],
                        [[15,16,17],[18,19,20]]])

print(threed_array.shape)

# The shape of the above array is 3 x 2 x3

# The broadcasting is allowed with the matrix
# which has the dimension either 2 x 1 or 2 x 3

# because, the last of the trailing dimension needs to be matched

oned_array = np.array([3,4])
print(oned_array.shape)

# Illegal because the shape of the matrix would be 1 x 2, which is not allowed
# to work with 3 x 2 x 3
# broadcasted_array = threed_array * oned_array
# print(broadcasted_array)

# In numpy, we have a reshape function, which allows us to reshape
# the shape of the matrix

reshaped_arry = np.reshape(oned_array,[2,1])
print(reshaped_arry.shape)
print(reshaped_arry)

broadcasted_array = threed_array * reshaped_arry

print(broadcasted_array)