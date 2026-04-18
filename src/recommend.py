import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import MinMaxScaler, LabelEncoder
import os

# Load dataset safely
base_dir = os.path.dirname(os.path.dirname(__file__))
file_path = os.path.join(base_dir, "data", "movies.csv")

data = pd.read_csv(file_path)

# Encode genre (text → number)
le = LabelEncoder()
data['genre_encoded'] = le.fit_transform(data['genre'])

# Normalize numerical features
scaler = MinMaxScaler()
data[['rating', 'year', 'duration']] = scaler.fit_transform(
    data[['rating', 'year', 'duration']]
)

# Feature matrix
features = data[['genre_encoded', 'rating', 'year', 'duration']]

# Compute similarity
similarity = cosine_similarity(features)

def recommend(movie_name):
    movie_name = movie_name.strip().lower()
    data['movie'] = data['movie'].str.lower()

    matches = data[data['movie'].str.contains(movie_name)]

    if matches.empty:
        print("\n❌ Movie not found. Try another.")
        return

# Take first match
    idx = matches.index[0]
    movie_name = data.iloc[idx]['movie']

    idx = data[data['movie'] == movie_name].index[0]

    scores = list(enumerate(similarity[idx]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)

    print(f"\n🎬 You selected: {movie_name}")
    print("\n🔥 Top 5 Recommendations:")

    for i in scores[1:6]:
        movie = data.iloc[i[0]]['movie']
        rating = round(data.iloc[i[0]]['rating'], 2)
        print(f"• {movie} (⭐ {rating})")

# Run system
print("=== Movie Recommendation System ===")
print("\nAvailable movies (sample):")
print(data['movie'].head(10).to_list())

while True:
    user_input = input("\nEnter movie name (or 'exit'): ")

    if user_input.lower() == 'exit':
        print("\n✅ Exiting...")
        break

    recommend(user_input)