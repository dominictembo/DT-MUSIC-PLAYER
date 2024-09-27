# Import necessary libraries
import tkinter as tk
from tkinter import filedialog, messagebox
from pygame import mixer
import os
import logging

# Define the DTplay class
class DTplay:
    # Initialize the DTplay object
    def __init__(self, root):
        # Set the root window
        self.root = root
        # Set the title of the window
        self.root.title("DTplay")
        # Set the background color of the window
        self.root.configure(background="#333")

        # Initialize the pygame mixer
        mixer.init()

        # Create a label to display the song title
        self.song_title_label = tk.Label(self.root, text="No song selected", bg="#333", fg="#fff", font=("Arial", 12))
        # Pack the label
        self.song_title_label.pack(pady=20)

        # Create buttons for play, pause, stop, open, and playlist
        self.play_button = tk.Button(self.root, text="Play", command=self.play_music, bg="#444", fg="#fff", font=("Arial", 12))
        self.play_button.pack(pady=10)

        self.pause_button = tk.Button(self.root, text="Pause", command=self.pause_music, bg="#444", fg="#fff", font=("Arial", 12))
        self.pause_button.pack(pady=10)

        self.stop_button = tk.Button(self.root, text="Stop", command=self.stop_music, bg="#444", fg="#fff", font=("Arial", 12))
        self.stop_button.pack(pady=10)

        self.open_button = tk.Button(self.root, text="Open", command=self.open_music, bg="#444", fg="#fff", font=("Arial", 12))
        self.open_button.pack(pady=10)

        self.playlist_button = tk.Button(self.root, text="Playlist", command=self.open_playlist, bg="#444", fg="#fff", font=("Arial", 12))
        self.playlist_button.pack(pady=10)

        # Create a volume scale
        self.volume_scale = tk.Scale(self.root, from_=0, to=100, orient="horizontal", command=self.set_volume, bg="#333", fg="#fff", font=("Arial", 12))
        # Set the initial volume to 50
        self.volume_scale.set(50)
        # Pack the volume scale
        self.volume_scale.pack(pady=20)

        # Create a listbox for the playlist
        self.playlist_listbox = tk.Listbox(self.root, width=40, height=10, bg="#333", fg="#fff", font=("Arial", 12))
        # Pack the listbox
        self.playlist_listbox.pack(pady=20)

        # Create buttons for adding to and removing from the playlist
        self.add_to_playlist_button = tk.Button(self.root, text="Add to Playlist", command=self.add_to_playlist, bg="#444", fg="#fff", font=("Arial", 12))
        self.add_to_playlist_button.pack(pady=10)

        self.remove_from_playlist_button = tk.Button(self.root, text="Remove from Playlist", command=self.remove_from_playlist, bg="#444", fg="#fff", font=("Arial", 12))
        self.remove_from_playlist_button.pack(pady=10)

        # Initialize the playlist
        self.playlist = []

        # Request file access permission
        self.request_file_access_permission()

    # Request file access permission
    def request_file_access_permission(self):
        # Import the android module
        import android
        # Request the necessary permissions
        android.request_permissions(['android.permission.READ_EXTERNAL_STORAGE', 'android.permission.WRITE_EXTERNAL_STORAGE'])

    # Play music
    def play_music(self):
        try:
            # Play the music
            mixer.music.play()
        except Exception as e:
            # Log the error
            logging.error("Error playing music: %s", e)
            # Show an error message
            messagebox.showerror("Error", "Error playing music")

    # Pause music
    def pause_music(self):
        try:
            # Pause the music
            mixer.music.pause()
        except Exception as e:
            # Log the error
            logging.error("Error pausing music: %s", e)
            # Show an error message
            messagebox.showerror("Error", "Error pausing music")

    # Stop music
    def stop_music(self):
        try:
            # Stop the music
            mixer.music.stop()
        except Exception as e:
            # Log the error
            logging.error("Error stopping music: %s", e)
            # Show an error message
            messagebox.showerror("Error", "Error stopping music")

    # Open a file dialog
    def open_file_dialog(self, filetypes):
        try:
            # Open the file dialog
            file_path = filedialog.askopenfilename(filetypes=filetypes)
            # Return the file path
            return file_path
        except Exception as e:
            # Log the error
            logging.error("Error opening file dialog: %s", e)
            # Show an error message
            messagebox.showerror("Error", "Error opening file dialog")

    # Open music
    def open_music(self):
        try:
            # Open the music file dialog
            song_path = self.open_file_dialog([("Audio Files", ".mp3 .wav")])
            # Load the music
            mixer.music.load(song_path)
            # Update the song title label
            self.song_title_label.config(text=song_path.split("/")[-1])
        except Exception as e:
            # Log the error
            logging.error("Error opening music: %s", e)
            # Show an error message
            messagebox.showerror("Error", "Error opening music")

    # Open playlist
    def open_playlist(self):
        try:
            # Open the playlist file dialog
            playlist_path = self.open_file_dialog([("Playlist Files", ".m3u .pls")])
            # Load the playlist
            self.load_playlist(playlist_path)
        except Exception as e:
            # Log the error
            logging.error("Error opening playlist: %s", e)
            # Show an error message
            messagebox.showerror("Error", "Error opening playlist")

    # Load playlist
    def load_playlist(self, playlist_path):
        # Initialize the playlist
        self.playlist = []
        try:
            # Open the playlist file
            with open(playlist_path, "r") as f:
                # Read the playlist file
                for line in f:
                    # Add the song to the playlist
                    self.playlist.append(line.strip())
            # Update the playlist listbox
            self.update_playlist_listbox()
        except Exception as e:
            # Log the error
            logging.error("Error loading playlist: %s", e)
            # Show an error message
            messagebox.showerror("Error", "Error loading playlist")

    # Add to playlist
    def add_to_playlist(self):
        try:
            # Open the music file dialog
            song_path = self.open_file_dialog([("Audio Files", ".mp3 .wav")])
            # Add the song to the playlist
            self.playlist.append(song_path)
            # Update the playlist listbox
            self.update_playlist_listbox()
        except Exception as e:
            # Log the error
            logging.error("Error adding to playlist: %s", e)
            # Show an error message
            messagebox.showerror("Error", "Error adding to playlist")

    # Remove from playlist
    def remove_from_playlist(self):
        try:
            # Get the selected index
            selected_index = self.playlist_listbox.curselection()[0]
            # Remove the song from the playlist
            self.playlist.pop(selected_index)
            # Update the playlist listbox
            self.update_playlist_listbox()
        except Exception as e:
            # Log the error
            logging.error("Error removing from playlist: %s", e)
            # Show an error message
            messagebox.showerror("Error", "Error removing from playlist")

    # Update playlist listbox
    def update_playlist_listbox(self):
        # Clear the listbox
        self.playlist_listbox.delete(0, tk.END)
        # Add the songs to the listbox
        for song in self.playlist:
            self.playlist_listbox.insert(tk.END, song.split("/")[-1])

    # Set volume
    def set_volume(self, value):
        try:
            # Check if the volume value is valid
            if 0 <= int(value) <= 100:
                # Set the volume
                mixer.music.set_volume(int(value) / 100)
            else:
                # Log the error
                logging.error("Invalid volume value: %s", value)
                # Show an error message
                messagebox.showerror("Error", "Invalid volume value")
        except Exception as e:
            # Log the error
            logging.error("Error setting volume: %s", e)
            # Show an error message
            messagebox.showerror("Error", "Error setting volume")

# Main function
if __name__ == "__main__":
    # Set up logging
    logging.basicConfig(level=logging.ERROR)
    # Create the root window
    root = tk.Tk()
    # Create the DTplay object
    dtplay = DTplay(root)
    # Start the main loop
    root.mainloop()