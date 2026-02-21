import pandas as pd
import sqlite3 as sql

# Change this if you have different path for the downloaded csv file
csv_path = '/Users/user/.cache/kagglehub/datasets/mohammedalsubaie/movies/versions/1/Movies.csv'
movies = pd.read_csv(csv_path)

#### Genres and production countries are strings splitting with commas
#### Create junction tables for them, then remove them from original table

# Collect all distinct genres
all_genres = sorted(movies['genres'].dropna().str.split(', ').explode().unique())

# Create a genre lookup table
genres_df = pd.DataFrame({'genre_id': range(1, len(all_genres) + 1), 'genre_name': all_genres})

# Create a junction table for movies and genres
genre_junction = movies[['movie_id', 'genres']].copy()
genre_junction['genres'] = genre_junction['genres'].str.split(', ')
genre_junction = genre_junction.explode('genres')
genre_junction = genre_junction.merge(genres_df, left_on='genres', right_on='genre_name')
genre_junction = genre_junction[['movie_id', 'genre_id']] # Keep only the foreign keys

# Collect all distinct countries
all_countries = sorted(movies['production_countries'].dropna().str.split(', ').explode().unique())

# Create a country lookup table
countries_df = pd.DataFrame({'country_id': range(1, len(all_countries) + 1), 'country': all_countries})

# Create a junction table for movies and countries
country_junction = movies[['movie_id', 'production_countries']].copy()
country_junction['production_countries'] = country_junction['production_countries'].str.split(', ')
country_junction = country_junction.explode('production_countries')
country_junction = country_junction.merge(countries_df, left_on='production_countries', right_on='country')
country_junction = country_junction[['movie_id', 'country_id']] # Keep only the foreign keys

#### Keeps other columns only
base_columns = list(movies.columns)
for column in ['genres', 'production_countries']:
    base_columns.remove(column)
movies_base = movies[base_columns]

# Create database
conn = sql.connect('movies_data.db')
cursor = conn.cursor()

# Create base table
movies_base.to_sql('movies', conn, if_exists='replace', index=False)

# Create the genre table and the country table
genres_df.to_sql('genres', conn, if_exists='replace', index=False)
countries_df.to_sql('countries', conn, if_exists='replace', index=False)

# Create junction tables
genre_junction.to_sql('movie_genres', conn, if_exists='replace', index=False)
country_junction.to_sql('movie_countries', conn, if_exists='replace', index=False)

conn.commit()
conn.close()