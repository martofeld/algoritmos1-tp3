from sounds import Song, SongFile, SoundCreator, Mark
from LinkedList import LinkedList
import constants


class FileManager():
    """Class that handles the managing of the files"""

    def file_to_song(self, file_name):
        """Parses a plp file to a SongFile class"""
        values_list = [0, [], LinkedList(), 0]
        try:
            with open(file_name, "r") as song_file:
                for line in song_file:
                    key, value = line.strip().split(constants.KEY_VALUE_SEPARATOR)
                    key = key.lower()

                    function = constants.DESERIALIZER_FUNCTIONS_DICT.get(key);
                    if not function:
                        raise KeyError("Unrecognized key '{}'".format(key))
                    function(values_list, value)
        except FileNotFoundError:
            print("File '{}' not found. Creating a new song...".format(file_name))

        return SongFile(values_list[0], values_list[1], values_list[2])

    def song_to_file(self, song, file_name):
        """Writes the SongFile to a plp file"""
        with open(file_name, "w") as file:
            file.write(constants.CHANNELS_WRITE_VALUE.format(song.get_channels()))
            for sound in song.get_sounds():
                file.write(constants.SOUNDS_WRITE_VALUE.format(sound.for_file()))
            current_tempo = 0
            for mark in song.get_marks():
                if mark.get_tempo() != current_tempo:
                    current_tempo = mark.get_tempo()
                    file.write(constants.TEMPOS_WRITE_VALUE.format(current_tempo))
                file.write(constants.NOTES_WRITE_VALUE)
                for note in mark.get_notes():
                    file.write(constants.ENABLED_CHAR if note else constants.DISABLED_CHAR)
                file.write("\n")
