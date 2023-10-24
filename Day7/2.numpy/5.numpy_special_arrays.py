# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 12:39:06 2023

@author: Radhakrishna
"""

# Constructing the array of zeros
import numpy as np

# Creation of a 2 d 3x3 zero aarary
zeros = np.zeros((3,3))

print(zeros)

# Creating a 2 3x3 zero array

zeros = np.zeros((2,3,2))
print(zeros)

# Create a 2d array of ones

ones =  np.ones((2,2))
print(ones)

ones = np.ones((3,2,3))
print(ones)


# Identify matrix - The matrix whose diagonals will always have 1

identity = np.identity(2)
print(identity)

identity = np.identity(5)
print(identity)

