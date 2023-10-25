# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 11:32:11 2023

@author: Radhakrishna
"""

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

#print(df)

# check the type of the dataframe
print(type(df))
print(df.head())

# By using the loc function, we can access the data element of the specific row

# For e.g. providing loc = 1 would fetch the data for the row which corresponds to index 1

df_loc = df.loc[1,:]
print(df_loc)

df_loc = df.loc[669,:]
print(df_loc)

# In order to access the elements column wise
# WE need to provide the row as : and the name of the column

df_loc_col = df.loc[:,'stock']
print(df_loc_col)