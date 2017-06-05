from files import FileManager


class CommandExecutor():
    """Class that wraps the implementation of the particular methods so the caller doesn't have to bother with the 
    details """

    def __init__(self):
        """Creates a new instance"""
        self.song_file = None

    def load(self, song_name):
        """Loads a new file in memory to work on"""
        file_reader = FileManager(song_name)
        self.song_file = file_reader.file_to_song()
        self.song_file.show()

    def step(self, steps=1):
        """Steps to {steps} forward position of the song"""
        self.song_file.step(steps)
        self.song_file.show()

    def back(self, steps=1):
        """Steps to {steps} backward position of the song"""
        self.song_file.back(steps)
        self.song_file.show()

    def add_track(self, track):
        """Adds a new track to the song"""
        self.song_file.add_track(track)
        self.song_file.show()

    def delete_track(self, track_number):
        """Deletes the {track_number} track from the song"""
        self.song_file.delete_track(track_number)
        self.song_file.show()

    def toggle_track(self, turn_on, track_number):
        """Toggles the {track_number} track of the current mark based on the {turn_on} value"""
        self.song_file.toggle_track(turn_on, track_number)
        self.song_file.show()

    def add_mark(self, tempo, position=0):
        """Adds a new mark in the given position"""
        self.song_file.add_mark(position, round(tempo * 0.1, 1))
        self.song_file.show()
