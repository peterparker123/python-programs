# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 11:15:46 2023

@author: Radhakrishna
"""

# The with keyword provides a context to work with resrouce
# The with keyword ensures that the resource is being managed at it's own end
# Programmers need not worry about closing of the file etc

try:
    with open('sherlock.txt',mode = 'r') as f:
        for line in f.readlines():
            print(line)
except FileNotFoundError:
    print("File does not exist")
    
print(f.closed)