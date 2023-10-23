# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 12:29:49 2023

@author: Radhakrishna
"""

# csv dictioary reader
# reads the values of the file as a key value pair

import csv

with open('employees.csv') as f:
    reader = csv.DictReader(f)
    
    print(reader)

  #  for row in reader:
  #     print(row,end=' ')
       
     # The dict reader gives the flexiblity
     # to read the values by providing the key 
    
    print('EmployeeID   Salary    Department_id')
    for row in reader:
        print(row['EMPLOYEE_ID'], row['SALARY'],row['DEPARTMENT_ID'])
      
      