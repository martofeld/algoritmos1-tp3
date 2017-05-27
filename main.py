from FileManager import FileReader

fileReader = FileReader("ejemplo2.plp")
song = fileReader.file_to_song()

song.play()
print(song)
