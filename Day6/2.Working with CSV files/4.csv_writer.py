# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 12:39:49 2023

@author: Radhakrishna
"""

# The writer function allows us to write
# the data to the csv file

import csv


headers=['EMPLOYEE_ID','FIRST_NAME','LAST_NAME','EMAIL','PHONE_NUMBER','HIRE_DATE','JOB_ID','SALARY',
           'COMMISSION_PCT','MANAGER_ID','DEPARTMENT_ID']
rows = [['198','Donald','OConnell','DOCONNEL','650.507.9833','21-Jun-07'	,'SH_CLERK','2600','-','124',
                '50'],
               ['199','Douglas','Grant','DGRANT','650.507.9844','13-Jan-08','SH_CLERK','2600','-' ,'124','50']]
with open('mycsv.csv','w',newline='') as csvfile:
    csvwriter = csv.writer(csvfile,delimiter=',')
    csvwriter.writerow(headers)
    
    for line in rows:
        csvwriter.writerow(line)