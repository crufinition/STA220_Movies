import pandas as pd
import sqlite3 as sql
import kagglehub


# Download latest version
path = kagglehub.dataset_download("mohammedalsubaie/movies")
print("Path to dataset files:", path)

# Try this if you have different path for the downloaded csv file
#path = '/Users/user/.cache/kagglehub/datasets/mohammedalsubaie/movies/versions/1/Movies.csv'

movies = pd.read_csv(path)

def junction(col_name, id_label, id_name, movies=movies, show_junction_items=False):
  # Collect all distinct items
  distinct_item = sorted(movies[col_name].dropna().str.split(', ').explode().unique())

  # Create a lookup table
  item_df = pd.DataFrame({id_label: range(1, len(distinct_item) + 1), id_name: distinct_item})

  # Create a junction table
  junction = movies[['movie_id', col_name]].copy()
  junction[id_label] = junction[col_name].str.split(', ')
  junction = junction.explode(id_label)
  junction = junction.merge(item_df, left_on=id_label, right_on=id_name)
  junction = junction[['movie_id', id_label+'_y']] # Keep only the foreign keys
  junction.columns = ['movie_id', id_label]

  return item_df, junction

genres, movie_genres = junction('genres', 'genre_id', 'genre')
countries, movie_countries = junction('production_countries', 'country_id', 'country')
companies, movie_companies = junction('production_companies', 'company_id', 'company')

## Remove columns to simplify
#movies_columns = movies.columns.tolist()
#for col in ['genres', 'production_countries', 'production_companies']:
#  movies_columns.remove(col)
#movies = movies[movies_columns]

conn = sql.connect('movies_data.db')
movies.to_sql('movies', conn, if_exists='replace', index=False)
genres.to_sql('genres', conn, if_exists='replace', index=False)
countries.to_sql('countries', conn, if_exists='replace', index=False)
companies.to_sql('companies', conn, if_exists='replace', index=False)

movie_genres.to_sql('movie_genres', conn, if_exists='replace', index=False)
movie_countries.to_sql('movie_countries', conn, if_exists='replace', index=False)
movie_companies.to_sql('movie_companies', conn, if_exists='replace', index=False)

conn.commit()
conn.close()
