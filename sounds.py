from LinkedList import LinkedList
from soundPlayer import SoundPlayer, SoundFactory

class _Note():
	"""docstring for Note"""
	def __init__(self, tempo, sounds):
		self.tempo = tempo
		self.sounds = sounds

	def __str__(self):
		return "Tempo: {}, Sounds: {}".format(self.tempo, str(self.sounds))

class Song():
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

		for tempo in self.tempos:
			print("{}|".format(tempo), end="")
		print("")
		for channel in range(self.channels):
			for note in self.tracks[channel]:
				print(" {} |".format(note), end="")

			print("  <-- ", self.notes[channel])
		
		for position in range(self.position + 1):
			if position == self.position:
				print(" ^ ")
			else:
				print("    ", end="")

	def step(self, steps = 1):
		if self.position < len(self) - 1:
			self.position += steps

	def back(self, steps = 1):
		if self.position > 0:
			self.position -= steps

	def add_track(self, track):
		self.notes.append(track)
		self.channels += 1
		marks = len(self.tracks[0])
		track = LinkedList()
		for i in range(marks):
			track.push("·")
		self.tracks.append(track)

	def delete_track(self, track_number):
		self.notes.pop(track_number)
		self.channels -= 1
		self.tracks.pop(track_number)

	def toggle_track(self, turn_on, track_number):
		current_value = "#" if turn_on else "·"
		self.tracks[track_number].replace(current_value, self.position)

	def add_mark(self, position, tempo):
		insert_position = self.position + position

		if insert_position < 0:
			insert_position = 0

		if position == -1:
			self.position += 1
			insert_position += 1

		self.tempos.insert(tempo, insert_position)
		for channel in range(self.channels):
			self.tracks[channel].insert("·", insert_position)

	def get_song(self, start = None, end = None):
		if start is None or start < 0:
			start = self.position
		if end is None or end > len(self) - 1:
			end = len(self) - 1

		song = Song(self.channels)
		# Get sound str as a proper sound
		sounds = []
		for sound in self.notes:
			sounds.append(SoundFactory.get_sound(sound))
		
		# Get the tracks that should be played
		tracks = []
		for channel in range(self.channels):
			tracks.append(self.tracks[channel].get_range(start, end))

		# Get the tempos for the chosen notes
		tempos = self.tempos.get_range(start, end)
		# For the len of the sounds to be played
		for track_postition in range(len(tracks[0])):
			enabled_sounds = []
			# For each channel we have
			for channel in range(self.channels):
				char = tracks[channel].get(track_postition)
				if char == "#":
					enabled_sounds.append(sounds[channel])
			song.add_note(tempos.get(track_postition), enabled_sounds)
		return song

	def __len__(self):
		return len(self.tracks[0])
