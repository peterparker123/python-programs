# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 11:41:45 2023

@author: Radhakrishna
"""

import pandas as pd

# iloc allows to extract the data by providing the index of the location

headers = ['index','ean','stock','price']
df =  pd.read_csv('C:\\programming\\python_programs\\Day8\\1.pandas\\offers_dataset.csv',sep=',')

# We are specifying index 1
df_loc = df.iloc[1]
print(df_loc)

# specify the index of the column
df_loc_column = df.iloc[:,2]
print(df_loc_column)