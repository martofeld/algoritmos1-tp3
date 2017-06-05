from sounds import Song, SongFile, SoundCreator, Mark
from LinkedList import LinkedList


class FileManager():
    """Class that handles the managing of the files"""

    def __init__(self, file_name):
        """Creates a new file manager for the file with the name"""
        self.file_name = file_name

    def open_file(self, mode="r"):
        """Opens the file this instance is managing"""
        return open(self.file_name, mode)

    def file_to_song(self):
        """Parses the given file to a SongFile"""
        channels = 0
        functions = []
        marks = LinkedList()
        current_tempo = 0
        with self.open_file() as song_file:
            for line in song_file:
                key, value = line.strip().split(",")
                key = key.lower()

                if key == "c":
                    channels = int(value)
                elif key == "s":
                    functions.append(SoundCreator.create_from(value))
                elif key == "t":
                    current_tempo = float(value)
                elif key == "n":
                    marks.push(Mark(current_tempo, [char == "#" for char in value]))

        return SongFile(channels, functions, marks)