# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 12:21:53 2023

@author: Radhakrishna
"""

import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline


# iloc allows to extract the data by providing the index of the location

headers = ['index','ean','stock','price']
df =  pd.read_csv('C:\\programming\\python_programs\\Day8\\1.pandas\\offers_dataset.csv',sep=',')

print(df.describe())

# To check for the duplicate values, duplicated() function
df_dup = df.duplicated()
# print(df_dup.tolist())

# To find the duplicate based on the specific column, provide the column name

df_dup_column = df.duplicated(subset=['stock'])
# print(df_dup_column.tolist())

# Check for missing values 

print(df.isna())

# Drop the missing values
print(df.dropna())

# We can drop specific index or columns
# In our dataset, we do not want to keep non nummeric data
# such as index and ean, Therefore, these two needs to be dropped

df_updated = df.drop(columns=['index','ean'])
print(df_updated.head())


# Plotting the data to identify the relationship
# We will plot the scatter plot, which will describe the relationship
# between the stock and the prices

# plt.bar(df['stock'],10)
# plt.show()
plt.scatter(df['stock'],df['price'])
plt.show(block=True)

# plot the bar plot
# In this, we get the values as the height

plt.bar(df['stock'],height=5,width=1)
plt.show()


# In order to identify the statistical distribution
# we plot the histogram data
plt.hist(df['stock'])
plt.show()