import sqlite3 as sql
import pandas as pd

def line(sym='=', n=20):
    print('\n' + sym*n + '\n')

db = sql.connect('movies_data.db')
print(pd.read_sql("SELECT * FROM movies LIMIT 10", db))
line()
print(pd.read_sql("SELECT * FROM genres", db))
line()
print(pd.read_sql("SELECT * FROM movie_genres LIMIT 10", db))
line()
print(pd.read_sql("SELECT * FROM countries", db))
line()
print(pd.read_sql("SELECT * FROM movie_countries LIMIT 10", db))
line()
print('=== End of Test ===')