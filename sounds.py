from LinkedList import LinkedList
from soundPlayer import SoundPlayer

class _Note():
	"""docstring for Note"""
	def __init__(self, tempo, sounds):
		self.tempo = tempo
		self.sounds = sounds

class Song():
	def __init__(self):
		self.notes = LinkedList()

	def add_note(self, tempo, sounds):
		note = _Note(tempo, sounds)
		self.notes.push(note)

	def play(self):
		sp = SoundPlayer(7)
		for note in self.notes:
			sp.play_sounds(note.sounds, note.tempo)

class SongFile():
	"""docstring for SongFile"""
	def __init__(self, channels, notes, tracks, tempos):
		super(SongFile, self).__init__()
		self.channels = channels
		self.notes = notes
		self.tracks = tracks
		self.tempos = tempos
		self.position = 0

	def show(self):
		print("Song has", self.channels, "channels")
		print("The sounds for each channel are: ")
		for i,sound in enumerate(self.notes):
			print(i,":", sound)

		print("|".join(self.tempos))
		for channel in range(self.channels):
			for note in self.tracks[channel]:
				print(" {} |".format(note), end="")

			print("  <-- ",self.notes[channel])
		
		for position in range(self.position + 1):
			if position == self.position:
				print(" ^ ")
			else:
				print("    ", end="")

	def step(self, steps = 1):
		self.position += steps

	def back(self, steps = 1):
		self.position -= steps

	def add_track(self, track):
		self.notes.append(track)
		self.channels += 1
		marks = len(self.tracks[0])
		track = []
		for i in range(marks):
			track.append(".")
		self.tracks.append(track)

	def delete_track(self, track_number):
		self.notes.pop(track_number)
		self.channels -= 1
		self.tracks.pop(track_number)

