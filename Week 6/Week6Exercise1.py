# Step 1: Create data structures
songs = []
genre_count = {}

print("Welcome to Music Library Manager!\n")

# Step 2: Collect 5 songs
for i in range(1, 6):
    # Everything inside this loop is indented once
    print(f"Enter Song {i}:")
    song_name = input(" Song name: ")
    genre = input(" Genre: ")
    print() # Blank line for readability
    
    # Store song as tuple
    song_tuple = (song_name, genre)
    songs.append(song_tuple)
    
    # Count genres using the .get() method to avoid errors
    genre_count[genre] = genre_count.get(genre, 0) + 1

# Step 3: Display library
print("=== YOUR MUSIC LIBRARY ===")
for index, (name, genre) in enumerate(songs, 1):
    # This print is inside the display loop
    print(f"{index}. {name} ({genre})")

# Step 4: Display statistics
print("\n=== GENRE STATISTICS ===")
for genre, count in genre_count.items():
    # This print is inside the statistics loop
    print(f"{genre}: {count} songs")

# Find and display most popular genre
if genre_count:
    most_popular = max(genre_count, key=genre_count.get)
    print(f"\nMost popular genre: {most_popular}")