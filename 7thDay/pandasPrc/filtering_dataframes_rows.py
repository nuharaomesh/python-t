import pandas as pd

# Filtering rows in data frame

data = {
    'Name': ["Omesh", "Nuhara"],
    'Age': [22, 12],
}

df = pd.DataFrame(data)

# filtering data same as numpy filtering
marks_obj = df[df['Age'] > 18]

# Sorting data
sorted = df.sort_values(by="Age")
# print(sorted)

# Adding a new column 
df['Salary'] = [2222, 2333]
# print(df)

# Adding a new row with `loc`
df.loc[len(df)] = ["Bob", 43, 111]
# print(df)

# Removing a column row
# If axis=0 0 declare for remove a row if it 1 its targeting rows
# inplace=False (default) by default its False, which means get a copy from data frame and remove in that specify column
# If its True inplace=True that means its removing column or row in original data frame
df_dropped = df.drop('Age', axis=1, inplace=False)
print(df_dropped)
print(df)


