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

