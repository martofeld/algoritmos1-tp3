from LinkedList import LinkedList
from soundPlayer import SoundPlayer, SoundFactory
import re as regularExpression
import random
import sys


class _Note:
    """docstring for Note"""

    def __init__(self, tempo, sounds):
        self.tempo = tempo
        self.sounds = sounds

class Song:
    def __init__(self, channels):
        self.notes = LinkedList()
        self.channels = channels

    def add_note(self, tempo, sounds):
        note = _Note(tempo, sounds)
        self.notes.push(note)

    def play(self):
        sp = SoundPlayer(self.channels)
        for note in self.notes:
            sp.play_sounds(note.sounds, note.tempo)
        sp.close()


class Mark:
    def __init__(self, tempo, notes):
        self.tempo = tempo
        self.notes = notes
        # Get a random number from 0 to max value to use as unique id
        self.id = random.randint(0, sys.maxsize)

    def push_note(self, enabled):
        self.notes.append(enabled)

    def pop_note(self, track_number):
        return self.notes.pop(track_number)

    def toggle_note(self, enabled, track_number):
        self.notes[track_number] = enabled

    def __eq__(self, other):
        return self.tempo == other.tempo and self.notes == other.notes and self.id == other.id


class SoundCreator():
    @staticmethod
    def create_from(string_self):
        print("creating with", string_self)
        split_sound = string_self.split("|")
        if len(split_sound) != 3:
            raise ValueError("The function {} is invalid".format(string_self))
        func, frequency, volume = split_sound[0].lower(), float(split_sound[1]), float(split_sound[2])
        if func == "sin":
            return SoundFactory.get_sine_sound(frequency, volume)
        if func == "tria":
            return SoundFactory.get_triangular_sound(frequency, volume)
        if func.startswith("sq") and func.isalnum():
            duty_cycle = regularExpression.search("[0-9]+", func).group(0)
            return SoundFactory.get_square_sound(frequency, volume, int(duty_cycle) * 0.1)
        raise ValueError("Function {} is not recognized".format(func))


class SongFile():
    """docstring for SongFile"""

    def __init__(self, channels, notes, marks):
        super(SongFile, self).__init__()
        self.channels = channels
        self.notes = notes
        self.marks = marks
        self.iterator = iter(marks)

    def show(self):
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
        for i in range(steps):
            if self.iterator.has_next():
                self.iterator.next()

    def back(self, steps=1):
        for i in range(steps):
            if self.iterator.has_previous():
                self.iterator.previous()

    def add_track(self, track):
        sound = None
        try:
            sound = SoundCreator.create_from(track)
        except ValueError as e:
            print("The function {} is not valid".format(track))
            return

        for mark in self.marks:
            mark.push_note(False)
        self.notes.append(sound)
        self.channels += 1

    def delete_track(self, track_number):
        for mark in self.marks:
            mark.pop_note(track_number)
        self.channels -= 1
        self.notes.pop(track_number)

    def toggle_track(self, turn_on, track_number):
        current_mark = self.iterator.get_current()
        current_mark.toggle_note(turn_on, track_number)

    def add_mark(self, position, tempo):
        new_mark = Mark(tempo, [False for i in range(self.channels)])
        if position == 0:
            self.iterator.insert(new_mark)
        elif position == 1:
            self.iterator.insert_next(new_mark)
        elif position == -1:
            self.iterator.insert_previous(new_mark)

    def __len__(self):
        return len(self.marks)