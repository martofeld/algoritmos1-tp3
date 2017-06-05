from LinkedList import LinkedList
from soundPlayer import SoundPlayer, SoundFactory
import re as regularExpression
import random
import sys


class _Note:
    """A class that holds the tempo and the Sounds that are enabled"""

    def __init__(self, tempo, sounds):
        self.tempo = tempo
        self.sounds = sounds


class Song:
    """A class that holds a succession of Notes"""

    def __init__(self, channels):
        self.notes = LinkedList()
        self.channels = channels

    def add_note(self, tempo, sounds):
        """Add a new note at the end of this song"""
        note = _Note(tempo, sounds)
        self.notes.push(note)

    def play(self):
        """Play this song"""
        sp = SoundPlayer(self.channels)
        for note in self.notes:
            sp.play_sounds(note.sounds, note.tempo)
        sp.close()


class Mark:
    """A class that holds the tempo and the enabled status of each track"""

    def __init__(self, tempo, notes):
        """Creates a new Mark
        :param tempo: The tempo of this mark
        :param notes: The list of enabled/disabled tracks for this mark"""
        self.tempo = tempo
        self.notes = notes
        # Get a random number from 0 to max value to use as unique id
        self.id = random.randint(0, sys.maxsize)

    def push_note(self, enabled):
        """Add a new note at the end of the current ones with the {enabled} status"""
        self.notes.append(enabled)

    def pop_note(self, track_number):
        """Return and remove the status of the note in the {track_number} position"""
        return self.notes.pop(track_number)

    def toggle_note(self, enabled, track_number):
        """Change the status of the note in the position {track_number} to the new {enabled} status"""
        self.notes[track_number] = enabled

    def __eq__(self, other):
        return self.tempo == other.tempo and self.notes == other.notes and self.id == other.id


class SoundCreator():
    @staticmethod
    def create_from(string_self):
        """Creates a new Sound from the given string"""
        split_sound = string_self.split("|")
        if len(split_sound) != 3:
            raise ValueError("The function {} is invalid".format(string_self))
        func, frequency, volume = "", 0, 0
        try:
            func, frequency, volume = split_sound[0].lower(), float(split_sound[1]), float(split_sound[2])
        except:
            raise ValueError("The function {} is invalid".format(string_self))
        if func == "sin":
            return SoundFactory.get_sine_sound(frequency, volume)
        if func == "tria":
            return SoundFactory.get_triangular_sound(frequency, volume)
        if func.startswith("sq") and func.isalnum():
            duty_cycle = regularExpression.search("[0-9]+", func).group(0)
            return SoundFactory.get_square_sound(frequency, volume, int(duty_cycle) * 0.1)
        raise ValueError("Function {} is not recognized".format(func))


class SongFile():
    """A representation of the song to work with"""

    def __init__(self, channels, notes, marks):
        """Create a new song file
        :param channels: The amount of channels the song has
        :param notes: A list of {Sound}s
        :param marks: A list of {Mark}s """
        self.channels = channels
        self.notes = notes
        self.marks = marks
        self.iterator = iter(marks)

    def show(self):
        """Prints the status of this class in a nice and fancy way"""
        print("Song has", self.channels, "channels")
        print("The sounds for each channel are: ")
        for i, sound in enumerate(self.notes):
            print(i, ":", sound)

        for mark in self.marks:
            print("{}|".format(mark.tempo), end="")
        print("")
        for channel in range(self.channels):
            for mark in self.marks:
                char = "#" if mark.notes[channel] else "·"
                print(" {} |".format(char), end="")
            print("  <-- ", self.notes[channel])

        for mark in self.marks:
            if mark == self.iterator.get_current():
                print(" ^ ")
                break
            else:
                print("    ", end="")

    def step(self, steps=1):
        """Steps to {steps} forward position of the song validating there is a mark. If the end is reached stops 
        moving """
        for i in range(steps):
            if not self.iterator.has_next():
                break
            self.iterator.next()

    def back(self, steps=1):
        """Steps to {steps} backwards position of the song validating there is a mark. If the start is reached stops 
        moving """
        for i in range(steps):
            if not self.iterator.has_previous():
                break
            self.iterator.previous()

    def add_track(self, track):
        """Adds a new track to the song. Disables all marks for the new track"""
        sound = SoundCreator.create_from(track)

        for mark in self.marks:
            mark.push_note(False)
        self.notes.append(sound)
        self.channels += 1

    def delete_track(self, track_number):
        """Deletes the track in the given position. Removes all marks for the track
        :param track_number: The position of the track to delete"""
        if track_number > self.channels - 1:
            raise IndexError

        for mark in self.marks:
            mark.pop_note(track_number)
        self.channels -= 1
        self.notes.pop(track_number)

    def toggle_track(self, turn_on, track_number):
        """Changes the status of the track in the given position on the current mark
        :param turn_on: The status of the track
        :param track_number: The track position to toggle"""
        if track_number > self.channels - 1:
            return IndexError
        current_mark = self.iterator.get_current()
        current_mark.toggle_note(turn_on, track_number)

    def add_mark(self, position, tempo):
        """Adds a new mark with all the tracks disabled. 
            If tempo == 0 the mark will be added in place
            If tempo == 1 the mark will be added next
            If tempo == -1 the mark will be added before
        """
        new_mark = Mark(tempo, [False for i in range(self.channels)])
        if position == 0:
            self.iterator.insert(new_mark)
        elif position == 1:
            self.iterator.insert_next(new_mark)
        elif position == -1:
            self.iterator.insert_previous(new_mark)

    def play_song(self, start=None, end=None):
        """Play the loaded song between the start and end position
        :param start: The start position to play, if none specified the current position is used
        :param end: The end position to play, if none specified the last position is used"""
        if start == None:
            start = self._get_current_position()
        play_marks = self.marks.get_range(start, end)
        SongPlayer(play_marks).play(self.notes)

    def _get_current_position(self):
        """Obtains the current mark we are standing by its index"""
        position = 0
        iterator = iter(self.marks)
        current = self.iterator.get_current()
        while iterator.get_current() != current:
            position += 1
            iterator.next()
        return position

    def play_song_with_length(self, seconds):
        """Plays {seconds} seconds of the loaded song"""
        seconds_sum = 0
        end_position = self._get_current_position()
        tempos_iterator = iter(self.marks)
        for i in range(end_position):
            tempos_iterator.next()
        mark = tempos_iterator.next()
        while tempos_iterator.has_next() and seconds_sum < seconds:
            seconds_sum += mark.tempo
            mark = tempos_iterator.next()
            end_position += 1
        self.play_song(end=end_position)

    def __len__(self):
        return len(self.marks)


class SongPlayer:
    """Class in charge of creating a song and playing it"""

    def __init__(self, marks):
        """ Create a new SongPlayer
        :param marks: iterable of marks that should be played"""
        self.marks = marks

    def play(self, functions):
        """Play a song with the given functions
        :param functions: a list of {Sound}s"""
        channels = len(functions)
        song = Song(channels)

        # For the len of the sounds to be played
        for mark in self.marks:
            enabled_sounds = []
            # For each channel we have
            for channel in range(channels):
                if mark.notes[channel]:
                    enabled_sounds.append(functions[channel])
            song.add_note(mark.tempo, enabled_sounds)
        song.play()
