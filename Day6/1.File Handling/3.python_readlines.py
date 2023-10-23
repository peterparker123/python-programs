# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 10:58:31 2023

@author: Radhakrishna
"""

try:
    f = open('sherlock.txt')
    
      
    # the readlines function allows us to process
    # the content of file through an iterable
    for line in f.readlines():
        print(line)
    
    f.close()
    
except FileNotFoundError:
    print('File does not exist')
    
# Read lines can also be used to specify
# how many lines needs to be read

# for e.g, we can use an index 

try:
    f = open('sherlock.txt')
    # print(f.readlines()[:2])
      
    # the readlines function allows us to process
    # the content of file through an iterable
    for line in f.readlines()[:2]:
        print(line)
    
    f.close()
    
except FileNotFoundError:
    print('File does not exist')
    
    
# extracting specific line by using an index

try:
    f = open('sherlock.txt')
    # print(f.readlines()[:2])
      
    # the readlines function allows us to process
    # the content of file through an iterable
    print(f.readlines()[4])
    
    f.close()
    
except FileNotFoundError:
    print('File does not exist')
    
# We can use an iterator to process the content of the file
# this allows us to extract the content, which we desire, and not more than that
try:
    f = open('sherlock.txt')
    # print(f.readlines()[:2])
      
    # the readlines function allows us to process
    # the content of file through an iterable
    file_iterator = iter(f.readlines())
    print(file_iterator)
    
    # use the next method to access the contents

    try:
        while True:
            result = next(file_iterator)
            print(result)
    except StopIteration:
        print("Iterator is empty")
    
    f.close()
    
except FileNotFoundError:
    print('File does not exist')