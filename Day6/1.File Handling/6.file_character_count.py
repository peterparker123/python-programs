# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 11:49:02 2023

@author: Radhakrishna
"""

# This program would count the number of different characters present in a file

# For this, we would create an empty dictionary
# The key of this dictionary is the number of character
# the value would be counts
word_dct = {}

try:
    f = open('sherlock.txt')
    
    for lines in f.readlines():
        for line in lines:
            # if the key exists 
            if line in word_dct:
                word_dct[line]+=1
            else:
                word_dct[line]=1
 
    # print(word_dct)
    for k,v in word_dct.items():
        print(f'Total number of {k} in the file is {v}')
except FileNotFoundError:
    print("File does not exist")