# Taxi Data ETL Pipeline

This project demonstrates a simple *Data Engineering ETL pipeline* using Python.

The pipeline extracts taxi trip data, cleans it, stores it in Parquet format, and runs analytical queries using DuckDB.

---

## Project Architecture

Data Source (CSV)
        |
        v
   Pandas ETL
(Extract + Clean Data)
        |
        v
 Parquet Storage
(data/processed)
        |
        v
   DuckDB Query Engine
        |
        v
   Analytics Output

---

## Tech Stack

Python  
Pandas  
DuckDB  
Parquet  

---

## Project Structure