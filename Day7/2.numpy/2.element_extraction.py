# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 11:42:12 2023

@author: Radhakrishna
"""

import numpy as np

# Extracting the element from a 3d array

threed_arr = np.array([[
                        [1,2,3],
                        [4,5,6]
                        ],    
                        [[7,8,9],
                        [10,11,12]
                    ]])
print(threed_arr)
print(threed_arr.shape)

# perform indexing on the array
print(threed_arr[0])

print(threed_arr[1][0][2])