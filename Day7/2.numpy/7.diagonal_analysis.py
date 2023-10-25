# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 13:33:52 2023

@author: Radhakrishna
"""

import numpy as np

# Define the 2x2 array
array = np.array([[3, 5], [4, 2]])

# Extract the desired diagonal elements
desired_diagonal = [array[0, -1], array[1, 0]]

# Create a new 2x2 array with the extracted diagonal elements
new_array = np.diag(desired_diagonal)

# Output the new array
print(new_array)
