# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 10:34:57 2023

@author: Radhakrishna
"""

# File basics in python
# in Python, the function open allows us to work with file

# The default mode in which the Python program opens the file is always 'read'


try:
    f = open('sherlock.txt',mode='r')
    
    print(type(f))
    
    # in order to print the content of the file
    # we use the read() function
    print(f.read())  
    print()
    # In the read function, we can specify how many character or bytes needs to be read
    f = open('sherlock.txt',mode='r')
    
    f.close()
except FileNotFoundError:
    print("The file does not exist")