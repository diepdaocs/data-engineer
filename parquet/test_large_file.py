import dask.dataframe as dd
import pandas as pd


def run_pandas():
    # Read a large Parquet file into a Pandas DataFrame
    df = pd.read_parquet('large_file_partitioned', columns=['column_name', 'another_column', 'column_mod9'])
    # Perform some operations on the Dask DataFrame
    # For example, compute the mean of a column
    mean_value = df['column_name'].mean()

    print(f'Mean value: {mean_value}')

    # You can also perform other operations like filtering and grouping
    filtered_df = df[df['column_name'] > 10]
    grouped_df = filtered_df.groupby('column_mod9', observed=True).sum()

    print(grouped_df)
    pass


def run_dash():
    # Read a large Parquet file into a Dask DataFrame
    df = dd.read_parquet('large_file_partitioned', columns=['column_name', 'another_column', 'column_mod9'])

    # Perform some operations on the Dask DataFrame
    # For example, compute the mean of a column
    mean_value = df['column_name'].mean().compute()

    print(f'Mean value: {mean_value}')

    # You can also perform other operations like filtering and grouping
    filtered_df = df[df['column_name'] > 10]
    grouped_df = filtered_df.groupby('column_mod9').sum().compute()

    print(grouped_df)


if __name__ == '__main__':
    # run_pandas()
    run_dash()
