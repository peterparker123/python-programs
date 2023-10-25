# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 12:05:04 2023

@author: Radhakrishna
"""

# Mathematical functions on 2-d array

import numpy as np

a = np.array([
              [3,5],
              [4,2]
             ])

print(a)
print(a.shape)

# Extracting the rows
print(a[:,:])

print(a[0,:])

print(a[1,:])

# Extraction of the columns

print(a[:,0])
print(a[:,1])


# Finding the minimum and maximum from the entire array

print(a.max())

# Finding the maximum value from an array of each column
print("The max value of each column is: " ,a.max(axis=0))

# Finding the max value from an array of each row
print("The max value of each row is : " , a.max(axis=1))

# Sum function -> Sums all the elements of the array

print("The sum of the array is: ", a.sum())

# Finding the sum for column axes

print("The sum of column value is: ",a.sum(axis=0))
print("The sum of row value is: ",a.sum(axis=1))


# Finding the diagonal of a matrix

print(a.diagonal())

# Transpose of the matrix

print(a.transpose())
