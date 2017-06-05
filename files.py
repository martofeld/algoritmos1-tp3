from soundPlayer import SoundFactory
from sounds import Song, SongFile, SoundCreator, Mark
from LinkedList import LinkedList
import re as regularExpression


class FileManager():
    """docstring for FileManager"""

    def __init__(self, file_name):
        self.file_name = file_name

    def open_file(self, mode="r"):
        return open(self.file_name, mode)

    def write_file(self, mode="w"):#agregar
        return open(self.file_name, mode)

    def file_to_song(self):
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

    def file_to_write(self):
        channels = 0
        functions = []
        marks = LinkedList()
        current_tempo = 0
        with self.write_file() as song_file:
            for line in song_file:
                key, value = line.strip().split(",")
                key = key.lower()
                if key == "c":
                    channels = int(value)
                    song_file.write(channels+"\n")
                elif key == "s":
                    song_file.write(functions.append(SoundCreator.create_from(value))+"\n")
                elif key == "t":
                    current_tempo = float(value)
                    song_file.write(current_tempo+"\n")
                elif key == "n":
                    song_file.write(marks.push(Mark(current_tempo, [char == "#" for char in value]))+"\n")

class FileReader():
    def __init__(self, file_name):
        self.file_manager = FileManager(file_name)

    def to_song(self):
        try:
            with self.file_manager.open_file() as file:
                return self.file_to_song(file)
        except FileNotFoundError:
            raise FileNotFoundError("The file could not be found, please check the file name")

    def file_to_song(self, file):
        song = Song()
        channels = 0
        sounds = []
        current_tempo = None
        for line in file:
            key, value = line.split(",")
            key = key.lower()

            if key == "c":
                channels = int(value)
            elif key == "s":
                sounds.append(self._get_sound(value, sounds))
            elif key == "t":
                current_tempo = float(value)
            elif key == "n":
                enabled_sounds = []
                for i, char in enumerate(value):
                    if char == "#":
                        enabled_sounds.append(sounds[i])
                song.add_note(current_tempo, enabled_sounds)

        return song

    def _get_sound(self, sound, sounds):
        split_sound = sound.split("|")
        function, frequency, volume = split_sound[0].lower(), float(split_sound[1]), float(split_sound[2])
        if function == "sin":
            return SoundFactory.get_sine_sound(frequency, volume)
        if function == "tria":
            return SoundFactory.get_triangular_sound(frequency, volume)
        if function.startswith("sq") and function.isalnum():
            duty_cycle = regularExpression.search("[0-9]+", function).group(0)
            return SoundFactory.get_square_sound(frequency, volume, int(duty_cycle) * 0.1)
        raise ValueError("Function {} is not recognized".format(function))


class FileLoader():
    def __init__(self, file_name):
        self.file_manager = FileManager(file_name)

    def print_file(self):
        channels = 0
        sounds = []
        tracks = []
        tempos = []
        current_tempo = 0
        for line in self.file_manager.open_file():
            key, value = line.split(",")
            key = key.lower()
            value = value.strip()

            if key == "c":
                channels = int(value)
                for channel in range(channels):
                    tracks.append([])
            elif key == "s":
                sounds.append(value)
            elif key == "t":
                current_tempo = value
            elif key == "n":
                tempos.append(current_tempo)
                for i, char in enumerate(value):
                    tracks[i].append(char)
        return SongFile(channels, sounds, tracks, tempos)
