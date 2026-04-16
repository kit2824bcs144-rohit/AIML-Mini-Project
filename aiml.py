
songs = [
    {"title": "Blinding Lights", "artist": "The Weeknd", "genre": "Pop", "mood": "Happy"},
    {"title": "Shape of You", "artist": "Ed Sheeran", "genre": "Pop", "mood": "Romantic"},
    {"title": "Believer", "artist": "Imagine Dragons", "genre": "Rock", "mood": "Energetic"},
    {"title": "Let Her Go", "artist": "Passenger", "genre": "Folk", "mood": "Sad"},
    {"title": "Thunder", "artist": "Imagine Dragons", "genre": "Rock", "mood": "Energetic"},
    {"title": "Perfect", "artist": "Ed Sheeran", "genre": "Pop", "mood": "Romantic"},
]


def normalize(text):
    return text.strip().lower()
history = {}
print("Enter songs you listened to (type 'exit' to stop):")

while True:
    song_name = input("> ")
    if normalize(song_name) == "exit":
        break

    song_name = normalize(song_name)
    history[song_name] = history.get(song_name, 0) + 1

genre_count = {}

for song in songs:
    title = normalize(song["title"])
    if title in history:
        genre = song["genre"]
        genre_count[genre] = genre_count.get(genre, 0) + history[title]


preferred_genre = "Pop"
if genre_count:
    preferred_genre = max(genre_count, key=genre_count.get)

mood_choice = input("Enter mood (Happy/Sad/Energetic/Romantic or 'none'): ")
mood_choice = normalize(mood_choice)

if mood_choice == "none":
    mood_choice = ""

print("\n🎧 Recommended Playlist:")

found = False
for song in songs:
    if song["genre"] == preferred_genre:
        if mood_choice == "" or normalize(song["mood"]) == mood_choice:
            print(f"- {song['title']} by {song['artist']}")
            found = True

if not found:
    print("No songs found for your mood. Try another mood!")