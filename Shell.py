import cmd
from files import FileManager
from CommandExecutor import CommandExecutor

class Shell(cmd.Cmd):

	def __init__(self):
		super(Shell, self).__init__()
		self.executor = CommandExecutor()

	def do_load(self, params):
		if not self.validate_params(params):
			return;
		self.executor.load(params)

	def do_store(self, params):
		#TODO
		raise NotImplementedError("Command store is not yet implemented")

	def do_step(self, params):
		self.executor.step()

	def do_back(self, params):
		self.executor.back()

	def do_stepm(self, params):
		if not self.validate_params(params, int):
			return;
		self.executor.step(int(params))

	def do_backm(self, params):
		if not self.validate_params(params, int):
			return;
		self.executor.back(int(params))

	def do_trackadd(self, params):
		#TODO
		raise NotImplementedError("Command trackadd is not yet implemented")

	def do_trackdel(self, params):
		#TODO
		raise NotImplementedError("Command trackdel is not yet implemented")

	def do_markadd(self, params):
		#TODO
		raise NotImplementedError("Command markadd is not yet implemented")

	def do_markaddnext(self, params):
		#TODO
		raise NotImplementedError("Command markaddnext is not yet implemented")

	def do_markaddprev(self, params):
		#TODO
		raise NotImplementedError("Command markaddprev is not yet implemented")

	def do_trackon(self, params):
		#TODO
		raise NotImplementedError("Command trackon is not yet implemented")

	def do_trackoff(self, params):
		#TODO
		raise NotImplementedError("Command trackoff is not yet implemented")

	def do_play(self, params):
		#TODO
		raise NotImplementedError("Command play is not yet implemented")

	def do_playall(self, params):
		#TODO
		raise NotImplementedError("Command playall is not yet implemented")

	def do_playmarks(self, params):
		#TODO
		raise NotImplementedError("Command playmarks is not yet implemented")

	def do_playseconds(self, params):
		#TODO
		raise NotImplementedError("Command playseconds is not yet implemented")

	def validate_params(self, params, expected_type = str):
		if not params:
			print("Params cant be empty")
			return False
		try:
			expected_type(params)
		except:
			print("Expected param of type", expected_type)
			return False
		return True
