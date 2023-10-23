# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 10:55:55 2023

@author: Radhakrishna
"""

# We can also read the python file by specifying the function readline
# it reads the content of the file line by line

try:
    f = open("sherlock.txt")
    
    print(f.readline())
    
    f.close()
    
except FileNotFoundError:
    print("File does not exist")
    
    