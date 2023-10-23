# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 12:06:39 2023

@author: Radhakrishna
"""

# A better mechanism to write to a file is using the append mode
# append only adds the new data to the file, and does not remove the
# old data
lst = ["This is first line\n", "This is second line"]

lst_new =  ["This is first line\n", "This is second line\n","This is third line"]

# lst_new =  ["This is first line\n", "This is second line\n","This is third line"]
with open('MyFile', mode='a') as f:
    
 
    for i in lst_new:
        f.write("---appending to the file----")
        print("appending to the file")
        f.write(i)