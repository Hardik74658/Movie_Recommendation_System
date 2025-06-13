import pickle
import pandas as pd

# Load the current movie list
print("Loading movie list...")
try:
    movies_df = pickle.load(open('movie_list (1).pkl', 'rb'))
    print(f"Successfully loaded movie list with {len(movies_df)} movies.")
    
    # Print information about the movies to remove
    movies_to_remove = [
        "Let Her Kill You",
        "A Female Boss with Big Tits and Her Cherry Boy Colleague Stay in the Same Room on a Business Trip - She Seduces Him for Fun and Makes Him Cum 10 Times - Yua Mikami"
    ]
    
    # Check if these movies exist in the dataset
    for movie in movies_to_remove:
        if movie in movies_df['title'].values:
            print(f"Found movie: '{movie}'")
        else:
            print(f"Movie not found: '{movie}'")
    
    # Remove the movies
    original_count = len(movies_df)
    movies_df = movies_df[~movies_df['title'].isin(movies_to_remove)]
    removed_count = original_count - len(movies_df)
    
    print(f"Removed {removed_count} movies.")
    
    # Save the updated movie list
    pickle.dump(movies_df, open('movie_list_clean.pkl', 'wb'))
    print("Saved cleaned movie list as 'movie_list_clean.pkl'")
    
except Exception as e:
    print(f"Error: {e}")
