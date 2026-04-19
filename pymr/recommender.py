import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(BASE_DIR, "movies.csv")

df = pd.read_csv(file_path)

# Fill missing values (just in case)
df.fillna('', inplace=True)

# Combine features into one column
df['combined'] = df['genres'] + " " + df['keywords']

# Convert text into numbers
vectorizer = CountVectorizer()
matrix = vectorizer.fit_transform(df['combined'])

# Compute similarity between all movies
similarity = cosine_similarity(matrix)


def recommend(movie_title, num_recommendations=5):
    # Check if movie exists
    if movie_title not in df['title'].values:
        return ["Movie not found in database."]

    # Get index of the movie
    idx = df[df['title'] == movie_title].index[0]

    # Get similarity scores
    scores = list(enumerate(similarity[idx]))

    # Sort by similarity (highest first)
    scores = sorted(scores, key=lambda x: x[1], reverse=True)

    # Get top recommendations (skip itself)
    top_movies = scores[1:num_recommendations+1]

    # Return movie titles
    recommendations = [df.iloc[i[0]]['title'] for i in top_movies]

    return recommendations
