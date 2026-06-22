import pandas as pd
import sqlite3

df_alls = pd.read_parquet("data/processed/df_alls_cleaned.parquet")

conn = sqlite3.connect("electricity.db")

df_alls["year"] = df_alls.index.year
df_alls["month"] = df_alls.index.month
df_alls["day"] = df_alls.index.day
df_alls["hour"] = df_alls.index.hour

df_alls.to_sql(
    "electricity",
    conn,
    if_exists= "replace",
    index = False
)

cursor = conn.cursor()

cursor.execute(
    "SELECT COUNT(*) FROM electricity"
)

print(cursor.fetchone())

conn.close()

print("Database created successfully.")