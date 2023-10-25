# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 11:44:30 2023

@author: Radhakrishna
"""

# Pandas has exploratory data analysis function, which allows us to
# identify about the structure of the data
# For e.g using describe() provides with all the information of the data

import pandas as pd

# iloc allows to extract the data by providing the index of the location

headers = ['index','ean','stock','price']
df =  pd.read_csv('C:\\programming\\python_programs\\Day8\\1.pandas\\offers_dataset.csv',sep=',')

print(df.describe())

# To check for the duplicate values, duplicated() function
df_dup = df.duplicated()
print(df_dup.tolist())

# To find the duplicate based on the specific column, provide the column name

df_dup_column = df.duplicated(subset=['stock'])
print(df_dup_column.tolist())

# Check for missing values 

print(df.isna())

# Drop the missing values
print(df.dropna())

# We can drop specific index or columns
# In our dataset, we do not want to keep non nummeric data
# such as index and ean, Therefore, these two needs to be dropped

df_updated = df.drop(columns=['index','ean'])
print(df_updated.head())

# We can perform a statistical analysis on the numerical columns
# for e.g, we can identify the mean of the stock

print('Mean of the stock values: ', df_updated['stock'].mean())
print('Mean of the prices: ',df_updated['price'].mean())


# Get the maximum values of the stocks and the prices

print('Maximum stock value: ',df_updated['stock'].max())
print('Maximum price: ',df_updated['price'].max())


# Identify the standard deviation
print('Standard deviation of the stock is :', df_updated['stock'].std())
print('Standard deviation of the price is :', df_updated['price'].std())


# Get the variance of the stock and the price
# Identify the standard deviation
print('Variance of the stock is :', df_updated['stock'].var())
print('Variance of the price is :', df_updated['price'].var())

# Identify the correlation of the two columns
# the df.corr() method computes the pearson correlation by default

print('Stock and price are correlated as: \n')
print(df_updated.corr())



# by using df.cov() funciton, we can obtain the covariance of the columns
# For e,g if the stock vary, how much variation would there be in the price also?

print('The covariance of Stock and Price is :\n')
print(df_updated.cov())


