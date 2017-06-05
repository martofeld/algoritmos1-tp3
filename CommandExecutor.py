from files import FileManager


class CommandExecutor():
    """Class that wraps the implementation of the particular methods so the caller doesn't have to bother with the 
    details """

    def __init__(self):
        """Creates a new instance"""
        self.song_file = None

    def load(self, song_name):
        """Loads a new file in memory to work on"""
        try:
            file_reader = FileManager(song_name)
            self.song_file = file_reader.file_to_song()
            self.song_file.show()
        except FileNotFoundError as e:
            return "Error: {} {}".format(e.args[1], song_name)
        return "OK"

    def step(self, steps=1):
        """Steps to {steps} forward position of the song"""
        self.song_file.step(steps)
        self.song_file.show()
        return "OK"

    def back(self, steps=1):
        """Steps to {steps} backward position of the song"""
        self.song_file.back(steps)
        self.song_file.show()
        return "OK"

    def add_track(self, track):
        """Adds a new track to the song"""
        try:
            self.song_file.add_track(track)
        except ValueError as e:
            return "Error: {}".format(e.args[0])
        self.song_file.show()
        return "OK"


    def delete_track(self, track_number):
        """Deletes the {track_number} track from the song"""
        try:
            self.song_file.delete_track(track_number)
        except IndexError:
            return "Error: no such track"
        self.song_file.show()
        return "OK"

    def toggle_track(self, turn_on, track_number):
        """Toggles the {track_number} track of the current mark based on the {turn_on} value"""
        try:
            self.song_file.toggle_track(turn_on, track_number)
        except IndexError:
            return "Error: no such track"
        self.song_file.show()
        return "OK"

    def add_mark(self, tempo, position=0):
        """Adds a new mark in the given position"""
        self.song_file.add_mark(position, round(tempo * 0.1, 1))
        self.song_file.show()
        return "OK"

    def play_marks(self, start=None, end=None):
        """Plays the marks between start and none"""
        self.song_file.play_song(start, end)
        self.song_file.show()
        return "OK"

    def play_seconds(self, seconds):
        """Plays the {seconds} seconds of the song"""
        self.song_file.play_song_with_length(seconds)
        self.song_file.show()
        return "OK"
