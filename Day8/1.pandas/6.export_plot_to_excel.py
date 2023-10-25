# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 14:48:01 2023

@author: Radhakrishna
"""

import pandas as pd
import matplotlib.pyplot as plt

from openpyxl import Workbook
from openpyxl.drawing.image import Image

%matplotlib inline

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

# Scatter plot
plt.scatter(df_updated['stock'], df_updated['price'])
plt.savefig('scatter_plot.png')
plt.show(block=True)

# Bar plot
plt.bar(df_updated['stock'], height=5, width=1)
plt.savefig('bar_plot.png')
plt.show()

# Histogram
plt.hist(df_updated['stock'])
plt.savefig('histogram_plot.png')
plt.show()

# Export the data to Excel
df.to_excel('output_data.xlsx', index=False)

# You can also save the updated dataframe without non-numeric columns
df_updated.to_excel('updated_data.xlsx', index=False)


# Create a new Excel workbook
workbook = Workbook()
sheet = workbook.active

# Insert scatter plot
scatter_plot = Image('scatter_plot.png')
sheet.add_image(scatter_plot, 'E5')  # Adjust the cell position as needed

# Insert bar plot
bar_plot = Image('bar_plot.png')
sheet.add_image(bar_plot, 'E20')  # Adjust the cell position as needed

# Insert histogram plot
histogram_plot = Image('histogram_plot.png')
sheet.add_image(histogram_plot, 'E35')  # Adjust the cell position as needed

# Save the workbook
workbook.save('plots_in_excel.xlsx')
