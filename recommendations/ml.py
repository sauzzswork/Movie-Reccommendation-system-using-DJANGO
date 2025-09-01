# recommendations/ml.py
from sklearn.neighbors import NearestNeighbors
import pandas as pd

def recommend_by_genre(movies, genre):
    filtered = movies[movies['genre'] == genre]
    return filtered[['title', 'genre', 'rating']].to_dict(orient='records')
