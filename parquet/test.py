import pandas as pd
import pyarrow as pa

# Create a sample DataFrame
data = {
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35],
    'city': ['New York', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)

# Write the DataFrame to a Parquet file
df.to_parquet('sample.parquet')

# Read the Parquet file back into a DataFrame
df_read = pd.read_parquet('sample.parquet')

print(df_read)
