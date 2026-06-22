import pandas as pd

movies = pd.read_csv('tmdb_5000_movies.csv')

print("Movie Recommendation System")

movie_name = input("Enter movie name: ")

results = movies[movies['title'].str.contains(
    movie_name,
    case=False,
    na=False
)]

print(results[['title']].head(10))