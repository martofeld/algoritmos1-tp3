from files import FileManager
import constants

class CommandExecutor():
    """Class that wraps the implementation of the particular methods so the caller doesn't have to bother with the 
    details """

    def __init__(self):
        """Creates a new instance"""
        self.song_file = None
        self.file_manager = FileManager()

    def load(self, song_name):
        """Loads a new file in memory to work on"""
        try:
            self.song_file = self.file_manager.file_to_song(song_name)
        except KeyError as e:
            return "Error: {}".format(e.args[0])
        self.song_file.show()
        return constants.SUCCESS

    def save(self, song_name):
        if self.song_file == None:
            return constants.NO_FILE_ERROR
        self.file_manager.song_to_file(self.song_file, song_name)
        self.song_file.show()
        return constants.SUCCESS

    def step(self, steps=1):
        """Steps to {steps} forward position of the song"""
        if self.song_file == None:
            return constants.NO_FILE_ERROR
        self.song_file.step(steps)
        self.song_file.show()
        return constants.SUCCESS

    def back(self, steps=1):
        """Steps to {steps} backward position of the song"""
        if self.song_file == None:
            return constants.NO_FILE_ERROR
        self.song_file.back(steps)
        self.song_file.show()
        return constants.SUCCESS

    def add_track(self, track):
        """Adds a new track to the song"""
        if self.song_file == None:
            return constants.NO_FILE_ERROR
        try:
            self.song_file.add_track(track)
        except ValueError as e:
            return "Error: {}".format(e.args[0])
        self.song_file.show()
        return constants.SUCCESS


    def delete_track(self, track_number):
        """Deletes the {track_number} track from the song"""
        if self.song_file == None:
            return constants.NO_FILE_ERROR
        try:
            self.song_file.delete_track(track_number)
        except IndexError:
            return "Error: no such track"
        self.song_file.show()
        return constants.SUCCESS

    def toggle_track(self, turn_on, track_number):
        """Toggles the {track_number} track of the current mark based on the {turn_on} value"""
        if self.song_file == None:
            return constants.NO_FILE_ERROR
        try:
            self.song_file.toggle_track(turn_on, track_number)
        except IndexError:
            return "Error: no such track"
        self.song_file.show()
        return constants.SUCCESS

    def add_mark(self, tempo, position=0):
        """Adds a new mark in the given position"""
        if self.song_file == None:
            return constants.NO_FILE_ERROR
        self.song_file.add_mark(position, round(tempo * constants.TEMPO_MULTIPLICATOR, 1))
        self.song_file.show()
        return constants.SUCCESS

    def play_marks(self, start=None, end=None):
        """Plays the marks between start and none"""
        if self.song_file == None:
            return constants.NO_FILE_ERROR
        self.song_file.play_song(start, end)
        self.song_file.show()
        return constants.SUCCESS

    def play_seconds(self, seconds):
        """Plays the {seconds} seconds of the song"""
        if self.song_file == None:
            return constants.NO_FILE_ERROR
        self.song_file.play_song_with_length(seconds)
        self.song_file.show()
        return constants.SUCCESS