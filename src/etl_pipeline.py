import pandas as pd
import duckdb

print("Loading dataset...")

df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/taxis.csv")

print("Dataset preview:")
print(df.head())

# Clean the data
df = df.dropna()

print("Rows after cleaning:", len(df))

# Save as Parquet file
df.to_parquet("data/processed/clean_taxis.parquet")

print("Saved cleaned data as Parquet")

# Query using DuckDB
con = duckdb.connect()

result = con.execute("""
SELECT payment, COUNT(*) as total_trips
FROM 'data/processed/clean_taxis.parquet'
GROUP BY payment
""").fetchdf()

print("Trip summary by payment type:")
print(result)