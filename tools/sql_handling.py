import pandas as pd
import sqlite3 as sql

__all__ = [
  'my_sql',
    'line'
]

db = sql.connect('movies_data.db')

def my_sql(query, db=db):
  '''A shorthand for pd.read_sql
  Taking our database as default'''
  return pd.read_sql(query, db)

def line(sym='=', n=20):
  print('\n' + sym*n + '\n')
