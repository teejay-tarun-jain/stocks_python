# Creates import table data in pandas

import sqlite3
import pandas as pd


# Read sqlite query results into a pandas DataFrame
con = sqlite3.connect("pythonsqlite.db")
df = pd.read_sql_query("SELECT * from test", con)
# Verify that result of SQL query is stored in the dataframe
print(df.head())

con.close()

