# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 10:55:38 2023

@author: Radhakrishna
"""

# Pandas is a library which allows us to create dataframe
# and using dataframe, we can perform Exploratory Data analysis
# using the combination of numpy libraries

import pandas as pd
import numpy as np


# Read the dataset
# When we read the csv file, the pandas library
# creates a dataframe
# Dataframes are similar to SQL tables, which will have
# rows and columns
headers = ['index','ean','stock','price']
df =  pd.read_csv('C:\\programming\\python_programs\\Day8\\1.pandas\\offers_dataset.csv',sep=',')

print(df)

# check the type of the dataframe
print(type(df))

# See the top 5 row
# Pandas provides us with the function called head()
# which displays the top 5 rows

print(df.head())

# Display the last 5 rows
# tail() function displays the last 5 rows of the dataframe
print(df.tail())

# Extract the elements using the index
# In pandas, the elements are extract by using the loc function

# Display the column names
print(df.columns.tolist())
print(df.keys)
df_loc =  df.loc[:,'stock']
print(df_loc)
# print(df_loc)