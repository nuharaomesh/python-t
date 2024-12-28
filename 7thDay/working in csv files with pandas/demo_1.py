import pandas as pd

file_path = '7thDay/working in csv files with pandas/customers-1000.csv'
df = pd.read_csv(file_path)

filtered = df[df['Country'] == 'Japan']
print(filtered)

# Inserting that filtered data to csv
filtered.to_csv('7thDay/working in csv files with pandas/newCus.csv', index=False)
