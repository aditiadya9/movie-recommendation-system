import pandas as pd
import random

movies = [
    "Avengers", "Inception", "Titanic", "3 Idiots", "Dangal",
    "Interstellar", "The Matrix", "KGF", "John Wick", "Pathaan",
    "La La Land", "The Notebook", "Forrest Gump", "Joker",
    "The Dark Knight", "Avatar", "Gladiator", "Shutter Island",
    "Zindagi Na Milegi Dobara", "Taare Zameen Par"
]

genres = ["Action", "Sci-Fi", "Romance", "Drama", "Comedy", "Horror"]

data = []

for i in range(120):  # 120 rows
    movie = random.choice(movies) + str(i)
    genre = random.choice(genres)
    rating = round(random.uniform(6.0, 9.5), 1)
    year = random.randint(1995, 2023)
    duration = random.randint(90, 180)

    data.append([movie, genre, rating, year, duration])

df = pd.DataFrame(data, columns=["movie", "genre", "rating", "year", "duration"])

import os

# Get correct project path
base_dir = os.path.dirname(os.path.dirname(__file__))
file_path = os.path.join(base_dir, "data", "movies.csv")

df.to_csv(file_path, index=False)

print("✅ Dataset with 120 rows created successfully!")