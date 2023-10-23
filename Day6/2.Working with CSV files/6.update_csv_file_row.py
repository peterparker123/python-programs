# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 13:41:39 2023

@author: Radhakrishna
"""

# The writer function allows us to write
# the data to the csv file

import csv

headers=['EMPLOYEE_ID','FIRST_NAME','LAST_NAME','EMAIL','PHONE_NUMBER','HIRE_DATE','JOB_ID','SALARY',
           'COMMISSION_PCT','MANAGER_ID','DEPARTMENT_ID']

with open('employees.csv') as f:
    reader = csv.DictReader(f)
    with open('mycsv.csv','w',newline='') as csvwriter:
    
        fieldnames = headers
        writer = csv.DictWriter(csvwriter,fieldnames=fieldnames)
    
        writer.writeheader()
    
        for row in reader:
            
            print(row)   
            # convert the salary to string
            updated_sal = int(row['SALARY']) * 1.2
            print(str(updated_sal),end=' ')    
            
            writer.writerow({headers[0]:row['EMPLOYEE_ID'],
                             headers[1]:row['FIRST_NAME'],
                             headers[2]:row['LAST_NAME'],
                             headers[3]:row['EMAIL'],
                             headers[4]:row['PHONE_NUMBER'],
                             headers[5]:row['HIRE_DATE'],
                             headers[6]:row['JOB_ID'],
                             headers[7]:updated_sal,
                             headers[8]:row['COMMISSION_PCT'],
                             headers[9]:row['MANAGER_ID'],
                             headers[10]:row['DEPARTMENT_ID']})
            
        
        
        
           
    # extract the salary and convert it to a string

        
        
    
        
    