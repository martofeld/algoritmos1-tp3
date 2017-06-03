from files import FileManager


class CommandExecutor():
    """docstring for CommandExecutor"""

    def __init__(self):
        self.song_file = None

    def load(self, song_name):
        file_reader = FileManager(song_name)
        self.song_file = file_reader.file_to_song()
        self.song_file.show()

    def step(self, steps=1):
        self.song_file.step(steps)
        self.song_file.show()

    def back(self, steps=1):
        self.song_file.back(steps)
        self.song_file.show()

    def add_track(self, track):
        self.song_file.add_track(track)
        self.song_file.show()

    def delete_track(self, track_number):
        self.song_file.delete_track(track_number)
        self.song_file.show()

    def toggle_track(self, turn_on, track_number):
        self.song_file.toggle_track(turn_on, track_number)
        self.song_file.show()

    def add_mark(self, tempo, position=0):
        self.song_file.add_mark(position, round(tempo * 0.1, 1))
        self.song_file.show()

    def play_marks(self, start = None, end = None):
        self.song_file.play_song(start, end)
        self.song_file.show()

    def play_seconds(self, seconds):
        self.song_file.play_song_with_length(seconds)
        self.song_file.show()
