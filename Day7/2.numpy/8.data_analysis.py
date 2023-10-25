# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 13:37:47 2023

@author: Radhakrishna
"""

# Performing data analysis using pandas

# The data set includes the meter number and the amount which the customer has paid
# on a specific transaction date, in the district of the region


import pandas as pd
import matplotlib.pyplot as plt


# Read the data into excel and create a dataframe
# Also, create index on the data

cols_to_be_used = ['REGION','DISTRICT','TRANSACTION_DATE','AMOUNT','METER_NUMBER','TELCO','METRE_TYPE','PAYMENT_CHANNEL','rechargeSource']
df = pd.read_csv("C:\\programming\\python_programs\\Day8\\1.pandas\\sample_data.csv",usecols=cols_to_be_used)

print(df.head())

#  list out all the columns
print(df.columns.tolist())

# find out the duplicate values in all the columns

print(df.duplicated(keep='first').tolist())

# Check out the missing values

print(df.isna())

# Use the loc function to extract the value based on the particular key
# Here, we will extract the value for the EASTERN REGION.
# Use the loc function to retrieve the column values

# unique function removes the duplicate values 
print(df.loc[:,'REGION'].unique())

# combine two or more columns in the loc function

print(df.loc[:,['REGION','DISTRICT','TRANSACTION_DATE']])


print(df.corr())
