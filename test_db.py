import sqlite3 as sql
import pandas as pd

def line(sym='=', n=20):
    print('\n' + sym*n + '\n')

db = sql.connect('movies_data.db')
print(pd.read_sql("SELECT * FROM movies", db))
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
print(pd.read_sql("SELECT production_companies FROM movies LIMIT 30", db))
line()
for i in range(19):
    print(pd.read_sql(f"SELECT * from genres WHERE genre_id={i}", db))
    line()