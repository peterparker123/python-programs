# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 12:20:45 2023

@author: Radhakrishna
"""


import csv

with open('employees.csv',newline='') as csvfile:
    csvreader = csv.reader(csvfile)
    print(csvreader)
    
    # in order to print the values out of the csv file
    # we need to use an iterable such as for loop
    
    # the csv reader function returns the values
    # of the csv file as a list
    
    # by converting the csv.reader's object
    # as an iterable, we can print out the first element
    # of the csv file which is columns
    
    csv_iter = iter(csvreader)
  #  for i in  next(csv_iter):
  #     print(
 #   print()
    for lines in csv_iter:
        print('||'.join(lines))
   