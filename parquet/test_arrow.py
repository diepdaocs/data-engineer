import pyarrow as pa

# Create a PyArrow Table
data = {
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35],
    'city': ['New York', 'Los Angeles', 'Chicago']
}
table = pa.table(data)

# Print the table
print(table)

# Convert the table to a Pandas DataFrame
df = table.to_pandas()
print(df)
