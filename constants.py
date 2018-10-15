from sounds import SoundWrapper, Mark, SoundCreator
from soundPlayer import SoundFactory

ENABLED_CHAR = "#"
DISABLED_CHAR = "·"

CHANNELS_READ_KEY = "c"
CHANNELS_WRITE_VALUE = "C,{}\n"

SOUNDS_READ_KEY = "s"
SOUNDS_WRITE_VALUE = "S,{}\n"

TEMPOS_READ_KEY = "t"
TEMPOS_WRITE_VALUE = "T,{}\n"

NOTES_READ_KEY = "n"
NOTES_WRITE_VALUE = "N,"

KEY_VALUE_SEPARATOR = ","
SOUND_VALUES_SEPARATOR = "|"

NUMBER_REGEX = "[0-9]+"
LETTERS_REGEX = "[a-z]+"

SUCCESS = "OK"

TEMPO_MULTIPLICATOR = 0.1

INCORRECT_PARAMS_ERROR = "Error: Incorrect number of params, check help for this command to see required params"
NO_FILE_ERROR = "No file loaded to work on"


FUNCTION_DICTIONARY = {
	"sin": lambda frequency, volume, extra: SoundWrapper(SoundFactory.get_sine_sound(frequency, volume), volume, "SIN"),
	"tria": lambda frequency, volume, extra: SoundWrapper(SoundFactory.get_triangular_sound(frequency, volume), volume, "TRIA"),
	"sq": lambda frequency, volume, extra: SoundWrapper(SoundFactory.get_square_sound(frequency, volume, extra * TEMPO_MULTIPLICATOR), volume, "SQ{}".format(extra))
}

DESERIALIZER_FUNCTIONS_DICT = {
	# as seen here http://p-nand-q.com/python/lambda.html
	CHANNELS_READ_KEY: lambda values_list, value: values_list.__setitem__(0, int(value)),
	SOUNDS_READ_KEY: lambda values_list, value: values_list[1].append(SoundCreator.create_from(value)),
	NOTES_READ_KEY: lambda values_list, value: values_list[2].push(Mark(values_list[3], [char == ENABLED_CHAR for char in value])),
	TEMPOS_READ_KEY: lambda values_list, value: values_list.__setitem__(3, float(value))
}