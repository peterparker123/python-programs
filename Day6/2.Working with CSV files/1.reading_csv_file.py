# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 12:15:37 2023

@author: Radhakrishna
"""

# In order to read csv file, we import the module
# csv

import csv

with open('employees.csv',newline='') as csvfile:
    csvreader = csv.reader(csvfile)
    print(csvreader)
    
    # in order to print the values out of the csv file
    # we need to use an iterable such as for loop
    
    # the csv reader function returns the values
    # of the csv file as a list
    
    
    for elem in csvreader:
        print(elem)