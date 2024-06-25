import pandas as pd
import sqlite3
import requests
from io import StringIO

# Define the URL of the CSV file
url = "https://www-genesis.destatis.de/genesis/downloads/00/tables/46131-0014_00.csv"

# Download the CSV file
response = requests.get(url)
data = response.content.decode('latin2')  # Ensure correct encoding for German umlauts

# Load the CSV file into a DataFrame
df = pd.read_csv(StringIO(data), skiprows=8, skipfooter=4, engine='python', sep=';')  # Skip metadata and footer

# Select the subset of columns
df_subset = df.iloc[:, list(range(5)) + [45, 46]]

# Rename the columns
df_subset.columns = ['year', 'month', 'goods_id', 'goods_name', 'goods_source', 'abroad', 'total']

# Filter out rows with missing values
df_subset = df_subset.dropna()

# Filter rows by 'goods_id' starting with 'NST7-'
df_subset[df_subset.goods_id.str.contains('^NST7-[0-9A-Z]{3}$')]

# Convert 'abroad' and 'total' to numeric, forcing errors to NaN
df_subset['abroad'] = pd.to_numeric(df_subset['abroad'], errors='coerce')
df_subset['total'] = pd.to_numeric(df_subset['total'], errors='coerce')

# Drop rows with non-positive 'abroad' and 'total' values
df_subset = df_subset[(df_subset['abroad'] > 0) & (df_subset['total'] > 0)]

# Convert 'abroad' and 'total' to integers
df_subset['abroad'] = df_subset['abroad'].astype(int)
df_subset['total'] = df_subset['total'].astype(int)

# Filter rows by german months
german_months = ["Januar" ,"Februar" ,"März" ,"April" ,"Mai" ,"Juni" ,"Juli" ,"August" ,"September" ,"Oktober" ,"November" ,"Dezember"]
df_subset = df_subset[df_subset['month'].apply(lambda x: x in german_months)]

# Define SQLite column types
column_types = {
    'year': 'BIGINT',
    'month': 'TEXT',
    'goods_id': 'TEXT',
    'goods_name': 'TEXT',
    'goods_source': 'TEXT',
    'abroad': 'BIGINT',
    'total': 'BIGINT'
}

# Connect to SQLite database
conn = sqlite3.connect('goodsTransportedByTrain.sqlite')

# Create the 'goods' table
create_table_query = """
CREATE TABLE IF NOT EXISTS goods (
    year BIGINT,
    month TEXT,
    goods_id TEXT,
    goods_name TEXT,
    goods_source TEXT,
    abroad BIGINT,
    total BIGINT
);
"""

conn.execute(create_table_query)
conn.commit()

# Insert data into the 'goods' table
df_subset.to_sql('goods', conn, if_exists='replace')

# Close the connection
conn.close()
