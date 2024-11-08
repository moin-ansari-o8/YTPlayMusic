import random
import webbrowser
import os
from pytube import Search

SONGS_FILE = "GIT_PROJECTS/YTPlayMusic/songs.txt"  # Ensure the path is correct

def load_songs():
    # Loads songs from the file provided
    if os.path.exists(SONGS_FILE):
        songs = {}
        with open(SONGS_FILE, "r") as file:
            for line in file:
                line = line.strip()
                if line:  # Check if line is not empty
                    try:
                        index, song = line.split('|', 1)
                        index = int(index.strip())
                        song = song.strip()
                        songs[index] = song
                    except ValueError:
                        print(f"Skipping invalid line: {line}")
        return songs
    return {}

def save_songs(songs):  # Save songs to the file
    with open(SONGS_FILE, "w") as file:
        for index, song in sorted(songs.items()):
            file.write(f"{index} | {song}\n")  # Always saves new song in new line

# List of initial songs
songs = load_songs() 

def add_song(songs):
    song_name = input("Enter the song name to add: ")
    new_index = max(songs.keys(), default=0) + 1
    songs[new_index] = song_name
    save_songs(songs)
    print(f"'{song_name}' has been added to the library.")

def delete_song(songs):
    if not songs:
        print("No songs available to delete.")
        return songs
    
    view_songs(songs)
    try:
        index_to_delete = int(input("Enter the index of the song to delete: "))
        if index_to_delete in songs:
            removed_song = songs.pop(index_to_delete)
            # Renumber the remaining songs
            renumbered_songs = {i + 1: song for i, song in enumerate(songs.values())}
            save_songs(renumbered_songs)
            print(f"'{removed_song}' has been removed from the library.")
            return renumbered_songs
        else:
            print(f"No song found at index {index_to_delete}.")
            return songs
    except ValueError:
        print("Invalid index. Please enter a number.")
        return songs

def play_random_song(songs):
    if songs:
        song = random.choice(list(songs.values()))
        print(f"Playing a random song: {song}")
        play_song(song)
    else:
        print("The song library is empty. Add some songs first.")

def suggest_song(songs):
    if songs:
        song = random.choice(list(songs.values()))
        print(f"How about listening to: {song}?")
        play_song(song)
    else:
        print("The song library is empty. Add some songs first.")

def view_songs(songs):
    if not songs:
        print("No songs available.")
    else:
        print("\nCurrent song library:")
        for index, song in sorted(songs.items()):
            print(f"{index}: {song}")

def play_song(song):
    search = Search(song)
    video_url = search.results[0].watch_url
    print(f"Playing: {video_url}")
    webbrowser.open(video_url)

def show_menu():
    print("\nMusic Library Menu:")
    print("1. Add a song")
    print("2. Delete a song")
    print("3. Play desired song")
    print("4. Play a random song")
    print("5. Suggest a song")
    print("6. View all songs")
    print("0. Exit")

def main():
    global songs
    while True:
        show_menu()
        choice = input("Choose an option (0-6): ")

        if choice == '1':
            add_song(songs)
        elif choice == '2':
            songs = delete_song(songs)
        elif choice == '3':
            song_name = input("Enter song name: ")
            print(f"Playing '{song_name}'.")
            play_song(song_name)
        elif choice == '4':
            play_random_song(songs)
        elif choice == '5':
            suggest_song(songs)
        elif choice == '6':
            view_songs(songs)
        elif choice == '0':
            print("Exiting the music library.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
