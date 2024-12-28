import pandas as pd

data = {
    "Name": ['Alice', 'Bob', 'Charlie'],
    "Age": [21, 22, 2]
}

df = pd.DataFrame(data)
print(df) 

# Also for working with data frame cells we can accessing them with loc, iloc key words
# loc[] this (label based) which means we can accessing cells with declaring row_label and column label
print(df.loc[0, "Name"])
# In iloc[] keyword (index based) we can accessing cells by declaring index numbers row_index and column_index    
print(df.iloc[1, 0])

# When give a one value to the loc key word it return data value that given row_index it gets that single number as row index
print(df.loc[0])

# We can named that row indexes
df = pd.DataFrame(data, index=["person_1", "person_2", "person_3"])
print(df) 

# Now we can access rows by that we given index value
print(df.loc["person_2"])

# Accessing columns by column name
age_column = df['Age']
print(age_column)

# Attributes 
# Shape attribute define the dimensions of the data frame
print(df.shape)

# Column attribute define the all the column names that hold in data frame
print(df.columns)
print(list(df.columns))

# dtype attribute show data types in the row values by column
print(df.dtypes)

# This attribute define the how much values in the data frame rows * column
print(df.size)

# With using this values attribute it return the data frame as numpy array, btw so cool ;)
print(type(df.values))

# Useful functions in pd
# Return the number of rows that in the data frame
print(len(df))

# Return the mean value of every column, for use this every columns values need to be numerical value
print(df.mean())

# Returning the sum of all column
print(df.sum())

# this df.describe() func describes the all summary of statistics for only numerical columns
print(df.describe())
