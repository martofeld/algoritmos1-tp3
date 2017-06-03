import cmd
from files import FileManager
from CommandExecutor import CommandExecutor


class Shell(cmd.Cmd):
    def __init__(self):
        super(Shell, self).__init__()
        self.executor = CommandExecutor()

    def do_load(self, params):
        """ NAME
                   load
            SYNOPSIS
                   load <file_name>

            DESCRIPTION
                    If existant, loads the given file so it can be both edited or played"""
        # if not self.validate_params(params):
        #	return;
        # self.executor.load(params)
        self.executor.load("ejemplo2.plp")

    def do_store(self, params):
        if not self.validate_params(params):
            return
        self.executor.save(params)

    def do_step(self, params):
        """ NAME
                   step
            SYNOPSIS
                   step

            DESCRIPTION
                    Steps to the next mark of the song"""
        self.executor.step()

    def do_back(self, params):
        """ NAME
                   back
            SYNOPSIS
                   back

            DESCRIPTION
                    Steps to the previous mark of the song"""
        self.executor.back()

    def do_stepm(self, params):
        """ NAME
                   stepm
            SYNOPSIS
                   stepm <n>

            DESCRIPTION
                    Steps forward n marks of the song"""
        if not self.validate_params(params, int):
            return;
        self.executor.step(int(params))

    def do_backm(self, params):
        """ NAME
                   backm
            SYNOPSIS
                   backm <n>

            DESCRIPTION
                    Steps backwards n marks of the song"""
        if not self.validate_params(params, int):
            return;
        self.executor.back(int(params))

    def do_trackadd(self, params):
        if not self.validate_params(params) or params.count(" ") != 2:
            return;
        params = params.replace(" ", "|")
        self.executor.add_track(params)

    def do_trackdel(self, params):
        if not self.validate_params(params, int):
            return;
        self.executor.delete_track(int(params))

    def do_markadd(self, params):
        if not self.validate_params(params, int):
            return
        self.executor.add_mark(int(params))

    def do_markaddnext(self, params):
        if not self.validate_params(params, int):
            return
        self.executor.add_mark(int(params), 1)

    def do_markaddprev(self, params):
        if not self.validate_params(params, int):
            return
        self.executor.add_mark(int(params), -1)

    def do_trackon(self, params):
        if not self.validate_params(params, int):
            return
        self.executor.toggle_track(True, int(params))

    def do_trackoff(self, params):
        if not self.validate_params(params, int):
            return
        self.executor.toggle_track(False, int(params))

    def do_play(self, params):
        self.executor.play_marks(end=1)

    def do_playall(self, params):
        self.executor.play_marks(start=0)

    def do_playmarks(self, params):
        if not self.validate_params(params, int):
            return;
        self.executor.play_marks(end=int(params))

    def do_playseconds(self, params):
        if not self.validate_params(params, int):
            return;
        self.executor.play_seconds(int(params))

    def validate_params(self, params, expected_type=str):
        if not params:
            print("Params cant be empty")
            return False
        try:
            expected_type(params)
        except:
            print("Expected param of type", expected_type)
            return False
        return True
