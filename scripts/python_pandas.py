## ------------------------------------------------------------------------
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
# Pandas really shines when working with data in CSV and Excel files.

# You can read files like CSV, Excel, parquet, feather, SQL, JSON, XML, HTML, etc
coffees = pd.read_csv('../data/coffee_sales.csv')

# Saving data to files
coffees.to_csv('../data/coffee_sales.csv', index=False) # index=False prevents from adding a 'Unnamed:0' column

# Preview Data
coffees.head() # preview data, first 5 rows by default
coffees.head(10) # preview first 10 rows
coffees.tail() # preview last 5 rows by default
coffees.sample(10) # preview a random sample, 1 row by default

coffees.info() # column names, column datatypes
coffees.columns # column names
coffees.dtypes # column datatypes
rows, columns = coffees.shape # returns a tuple (rows_count, columns_count)
print(rows, columns)
data_count = coffees.size # number of elements
print(data_count)

coffees.describe() # summary stats of numeric data
coffees['coffees Type'].unique() # list of unique values in a column
coffees['coffees Type'].nunique() # count of unique values in a column
coffees['coffees Type'].unique().tolist() # easier viewing
pd.Series(coffees['coffees Type'].unique()) # easeier viewing

# Access Specific Rows, Columns, Cells
coffees.loc[0] # access specific row by row name
coffees.loc[0, 'coffees Type'] # access specific cells in [#rows, #columns] by name
coffees.loc[0:5, ['coffees Type','Units Sold']] # access cells in multiple rows, columns, allows slicing
coffees.iloc[0] # access specific row by row index
coffees.iloc[0:10,0] # access cells in multiple rows, columns by index, allows slicing

coffees['Day'] # access a column
coffees[['coffees Type', 'Day']] # access multiple columns
coffees.Day # access single_word columns

# Editing Data
print(coffees.loc[0,'Units Sold'])
coffees.loc[0,'Units Sold'] = 20
print(coffees.loc[0,'Units Sold'])

# Sorting Data
coffees.sort_values('Units Sold') # default is ascending
coffees.sort_values('Units Sold', ascending=False)
coffees.sort_values(['Units Sold', 'coffees Type'], ascending=[False, True]) # sort by multiple values, sorts left most parameter first

# Filtering Data
players = pd.read_csv('../data/olympics_players.csv')

tall_players = players.loc[players['height_cm'] > 220]
tall_players.sort_values('height_cm', ascending=False)
tall_players.sort_values('height_cm', ascending=False)[['name', 'height_cm']] # shows only name and height_cm columns

players.loc[players['height_cm'] > 220, ['name','height_cm']] # short hand to specify columns
players.loc[(players['height_cm'] > 200) & (players['height_cm'] < 202) & (players['born_country'] == 'USA')].sort_values('height_cm', ascending=False)

players[players['height_cm'] > 220] # short hand instead of using loc[]

players[players['name'].str.contains('Keith', case=False)]
players[players['name'].str.contains('Keith', case=False)].shape[0]

players.query('born_country=="USA" & born_city=="Seattle"') # not the use of '' and ""

# Add, Remove Columns
coffees = pd.read_csv('../data/coffee_sales.csv')
coffees.head()

coffees['Price'] = 4.99 # adds a new column and sets value to 4.99
coffees.drop(columns='Price', inplace=True)
price_map = {
  'Espresso':3.99,
  'Latte':4.99
}

coffees['Price'] = coffees['Coffee Type'].map(price_map)
coffees['Revenue'] = coffees['Units Sold'] * coffees['Price']
coffees.rename(columns={'Units Sold':'Coffees Sold'}, inplace=True)

coffees.drop(0) # removes by row index, does not modify the dataframe unless inplace=True
coffees = coffees.drop(0) # modifies the dataframe
coffees.drop(columns=['Unnamed: 0'], inplace=True) # modifies the dataframe
coffees.head()

players = pd.read_csv('../data/olympics_players.csv')
players_temp = players.copy()
players_temp.head()

# Reading large excel files takes time
olympics_data_df = pd.read_excel('../data/olympics_data.xlsx')
olympics_data_df.head()

# ------------------------------------------------------------------------
# VISUALIZATION USING MATPLOTLIB
# ------------------------------------------------------------------------