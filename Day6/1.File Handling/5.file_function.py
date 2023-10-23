# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 11:34:13 2023

@author: Radhakrishna
"""

# file.size
import os

def file_size(f):
    cnt = 0
    for lines in f.readlines():
        for line in lines:
            if line not in '\n':
                cnt+=1
    return cnt

# the tell function returns the current stream position
def file_position(f):
    return f.tell()

with open('sherlock.txt') as f:
    print(file_size(f))
    print(file_position(f))
    