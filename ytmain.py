import webbrowser
import random
from pytube import YouTube, Search

# List of initial songs
songs = [
    "Shape of You",
    "Blinding Lights",
    "Dance Monkey",
    "Someone You Loved",
    "Sunflower"
]

def add_song():
    song_name = input("Enter the song name to add: ")
    songs.append(song_name)
    print(f"'{song_name}' has been added to the library.")

def play_random_song():
    song = random.choice(songs)
    print(f"Playing a random song: {song}")
    play_song(song)

def suggest_song():
    song = random.choice(songs)
    print(f"How about listening to: {song}?")
    play_song(song)

def play_song(song):
    search = Search(song)
    video_url = search.results[0].watch_url
    print(f"Playing: {video_url}")
    webbrowser.open(video_url)

def play_desired():
    song = input("Enter song name : ")
    print(f"Playing a random song: {song}")
    play_song(song)

def menu():
    while True:
        print("\nMusic Library Menu:")
        print("1. Add a song")
        print("2. Play desired song")
        print("3. Play a random song")
        print("4. Suggest a song")
        print("0. Exit")
        
        choice = input("Choose an option (1-4): ")
        
        if choice == '1':
            add_song()
        elif choice == '2':
            play_desired()
        elif choice == '3':
            play_random_song()
        elif choice == '4':
            suggest_song()

        elif choice == '0':
            print("Exiting the music library.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    menu()
