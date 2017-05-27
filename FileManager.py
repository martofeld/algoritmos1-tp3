from soundPlayer import SoundFactory
from sounds import Song
import re as regularExpression

class FileManager():
	"""docstring for FileManager"""
	def __init__(self, file_name):
		self.file_name = file_name

	def open_file(self, mode = "r"):
		return open(self.file_name, mode)

class FileReader():
	def __init__(self, file_name):
		self.file_manager = FileManager(file_name)

	def file_to_song(self):
		file = None
		try:
			file = self.file_manager.open_file()
		except FileNotFoundError:
			raise FileNotFoundError("The file could not be found, please check the file name")

		song = Song()
		channels = 0
		sounds = []
		current_tempo = None
		for line in file:
			key,value = line.split(",")
			key = key.lower()

			if key == "c":
				channels = int(value)
			elif key == "s":
				sounds.append(self._get_sound(value, sounds))
			elif key == "t":
				current_tempo = float(value)
			elif key == "n":
				enabled_sounds = []
				for i,char in enumerate(value):
					if char == "#":
						enabled_sounds.append(sounds[i])
				song.add_note(current_tempo, enabled_sounds)
		return song

	def _get_sound(self, sound, sounds):
		split_sound = sound.split("|")
		function,frequency,volume = split_sound[0].lower(),float(split_sound[1]),float(split_sound[2])
		if function == "sin":
			return SoundFactory.get_sine_sound(frequency, volume)
		if function == "tria":
			return SoundFactory.get_triangular_sound(frequency, volume)
		if function.startswith("sq") and function.isalnum():
			duty_cycle = regularExpression.search("[0-9]+", function).group(0)
			return SoundFactory.get_square_sound(frequency, volume, int(duty_cycle))
		raise ValueError("Function {} is not recognized".format(function))




