# ------------------------------------------------------------------------
# PYTHON - PANDAS LIBRARY
# ------------------------------------------------------------------------
# References:
# Complete Python Pandas Data Science Tutorial: https://www.youtube.com/watch?v=2uvysYbKdjM&t=300s
# Real-world Dataset Cleaning https://www.youtube.com/live/oad9tVEsfI0
# Solving 100 Python Pandas Problems https://www.youtube.com/watch?v=i7v2m-ebXB4&t=47s

# Pandas is a Python library for data manipulation & analyis
# Pandas is build on top of NumPy library
# Pandas provides two main data structures: Series and DataFrame

import pandas as pd

# ------------------------------------------------------------------------
# SERIES
# ------------------------------------------------------------------------
# Series is like an Excel column, a 1-dimensional vertical labeled array of data
# Series syntax: pd.Series(data_list, index), where index adds the label for each row item
# Series uses index to define labels, DataFrame uses index and columns
series = pd.Series([10,20,30,40,50], index=['a','b','c','d','e'])
print(series)

# Do not confuse 'index' of Series to the 'index' of a List
# Series behaves similar to a Dictionary, where items are accessed using 'dictionary keys', not like 'list indexes'
print(series['a'])
print(series[0]) # Throws warning

# ------------------------------------------------------------------------
# DATAFRAME
# ------------------------------------------------------------------------
# Dataframe is like an Excel spreadsheet, a 2-dimensional labled matrix of data
# Dataframe automatically adds indexes (i.e. row numbers, column numbers) for rows and columns
#
# dataframe syntax is dataframe(data_rows_in_2D_list, columns=column_header_list)
# dataframe syntax can also be a dictionary where keys becomes the column headers, eg: dataframe(dict_data)

# Creating Dataframe
# by default, row and column indexes are added
df = pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]])
print(df)
# you can specify keys for rows and columns
df = pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]], index=['row1','row2','row3'], columns=['a','b','c'])
print(df)

# Using a dictionary to create a dataframe
# dictionary keys become the column headers
# row indexes are added by default
data = {
  'Name': ['Alice', 'Bob', 'Charlie'],
  'Age': [25, 30, 35],
  'City': ['London', 'Paris', 'New York']
}
df = pd.DataFrame(data)
print(df)

# Access Columns
df['Name'] # Access columns using keys
df[['Name','Age']] # Accessing multiple columns. Note the double []

# Access Rows
df = pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]], index=['row1','row2','row3'], columns=['a','b','c'])
print(df)
df[0] # Throws KeyError. You cannot access rows using row indexes like in a list. Use iloc[]
df.iloc[0] # Access row using index
df.loc['row1'] # Access row using label

# Getting column headers and row headers
df = pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]], columns=['a','b','c'])
df.columns # columns is an attribute, not a method
df.index # index is an attribute, not a method
df = pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]], index=['row1','row2','row3'], columns=['a','b','c'])
df.index

# Dataframe Common Methods
df = pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]], columns=['a','b','c'])
df.info()
df.shape # shape is not a method
df.describe()
df['a'].unique()

# Previewing data
df = pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]], columns=['a','b','c'])
df.head() # shows first 5 rows
df.head(2) # shows first 2 rows
df.tail() # shows last 5 rows
df.tail(2) # shows last 2 rows

# ------------------------------------------------------------------------
# FILES - CSV, EXCEL
# ------------------------------------------------------------------------

# ------------------------------------------------------------------------
# VISUALIZATION USING MATPLOTLIB
# ------------------------------------------------------------------------