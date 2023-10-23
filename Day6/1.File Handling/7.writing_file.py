# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 10:34:39 2023

@author: Radhakrishna
"""

# In order to write textual data to file
# in the open command, the mode should be 'w'

lst = ["This is first line\n", "This is second line"]

print("")
lst_new =  ["This is first line\n", "This is second line\n","This is third line"]
with open('MyFile', mode='w') as f:
    for i in lst_new:
        f.write(i)
        
