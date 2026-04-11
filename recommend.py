import pandas as pd

# Load dataset
data = pd.read_csv("data/movies.csv")

# Function to recommend movies
def recommend(movie_name):
    movie_name = movie_name.title()

    # Check if movie exists
    if movie_name not in data['movie'].values:
        print("\n❌ Movie not found in dataset.")
        print("👉 Try another movie.\n")
        return

    # Get selected movie details
    selected_movie = data[data['movie'] == movie_name]
    genre = selected_movie.iloc[0]['genre']
    rating = selected_movie.iloc[0]['rating']

    print(f"\n🎬 You selected: {movie_name}")
    print(f"📂 Genre: {genre} | ⭐ Rating: {rating}")

    # Filter similar movies
    recommendations = data[data['genre'] == genre]

    # Sort by rating (important upgrade)
    recommendations = recommendations.sort_values(by='rating', ascending=False)

    print("\n🔥 Recommended Movies:")

    for m, r in zip(recommendations['movie'], recommendations['rating']):
        if m != movie_name:
            print(f"• {m} (⭐ {r})")


# Main program
print("=== Movie Recommendation System ===")

while True:
    user_input = input("\nEnter a movie name (or type 'exit'): ")

    if user_input.lower() == 'exit':
        print("\n✅ Thank you for using the system!")
        break

    recommend(user_input)