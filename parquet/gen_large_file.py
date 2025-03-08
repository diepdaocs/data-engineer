import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

# Generate a large DataFrame
data = {
    'column_name': range(100000000),  # 100 million rows
    'column_mod99': [i % 99 for i in range(100000000)],
    'another_column': range(100000000, 200000000)
}
df = pd.DataFrame(data)

# Convert the DataFrame to a PyArrow Table
table = pa.Table.from_pandas(df)

# Write the table to a Parquet file with partitioning on 'column_mod9'
pq.write_to_dataset(table, root_path='large_file_partitioned', partition_cols=['column_mod99'], compression='snappy')
