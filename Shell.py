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
        if not self.validate_params(params):
            print("Error: Incorrect number of params, check help for this command to see required params")
            return
        print(self.executor.load(params))

    def do_store(self, params):
        """ NAME
                   store
            SYNOPSIS
                   store <file_name>

            DESCRIPTION
                    Stores the current song to the given file"""
        # TODO
        raise NotImplementedError("Command store is not yet implemented")

    def do_step(self, params):
        """ NAME
                   step
            SYNOPSIS
                   step

            DESCRIPTION
                    Steps to the next mark of the song"""
        print(self.executor.step())

    def do_back(self, params):
        """ NAME
                   back
            SYNOPSIS
                   back

            DESCRIPTION
                    Steps to the previous mark of the song"""
        print(self.executor.back())

    def do_stepm(self, params):
        """ NAME
                   stepm
            SYNOPSIS
                   stepm <n>

            DESCRIPTION
                    Steps forward n marks of the song"""
        if not self.validate_params(params, int):
            print("Error: Incorrect number of params, check help for this command to see required params")
            return
        print(self.executor.step(int(params)))

    def do_backm(self, params):
        """ NAME
                   backm
            SYNOPSIS
                   backm <n>

            DESCRIPTION
                    Steps backwards n marks of the song"""
        if not self.validate_params(params, int):
            print("Error: Incorrect number of params, check help for this command to see required params")
            return
        print(self.executor.back(int(params)))

    def do_trackadd(self, params):
        """ NAME
                   trackadd
            SYNOPSIS
                   trackadd <function> <frequency> <volume>

            DESCRIPTION
                    Adds a track to the current song, by default all marks will be off.
            NOTE
                    function can be one of [SIN, TRIA or SQ{0-9}+]
                    frequency can be any number
                    volume is expected to be a number from 0 to 1
            """
        if not self.validate_params(params) or params.count(" ") != 2:
            print("Error: Incorrect number of params, check help for this command to see required params")
            return
        params = params.replace(" ", "|")
        print(self.executor.add_track(params))

    def do_trackdel(self, params):
        """ NAME
                   trackdel
            SYNOPSIS
                   trackdel <n>
    
            DESCRIPTION
                    Deletes the track in the given position
            NOTE
                    If there is no track in the given position the song will remain unmodified
            """
        if not self.validate_params(params, int):
            print("Error: Incorrect number of params, check help for this command to see required params")
            return
        print(self.executor.delete_track(int(params)))

    def do_markadd(self, params):
        """ NAME
                   markadd
            SYNOPSIS
                   markadd <tempo>

            DESCRIPTION
                    Adds a new mark in the current position with the given tempo, by default all tracks are off.
            """
        if not self.validate_params(params, int):
            print("Error: Incorrect number of params, check help for this command to see required params")
            return
        print(self.executor.add_mark(int(params)))

    def do_markaddnext(self, params):
        """ NAME
                   markaddnext
            SYNOPSIS
                   markaddnext <tempo>
    
            DESCRIPTION
                    Adds a new mark in the next position with the given tempo, by default all tracks are off.
            """
        if not self.validate_params(params, int):
            print("Error: Incorrect number of params, check help for this command to see required params")
            return
        print(self.executor.add_mark(int(params), 1))

    def do_markaddprev(self, params):
        """ NAME
                   markaddprev
            SYNOPSIS
                   markaddprev <tempo>

            DESCRIPTION
                    Adds a new mark in the previous position with the given tempo, by default all tracks are off.
            """
        if not self.validate_params(params, int):
            print("Error: Incorrect number of params, check help for this command to see required params")
            return
        print(self.executor.add_mark(int(params), -1))

    def do_trackon(self, params):
        """ NAME
                   trackon
            SYNOPSIS
                   trackon <n>

            DESCRIPTION
                    Turns on the track in the given position on the current mark.
            NOTE
                    If the position doesn't exist the song will remain unchanged
            """
        if not self.validate_params(params, int):
            print("Error: Incorrect number of params, check help for this command to see required params")
            return
        print(self.executor.toggle_track(True, int(params)))

    def do_trackoff(self, params):
        """ NAME
                   trackoff
            SYNOPSIS
                   trackoff <n>
    
            DESCRIPTION
                    Turns off the track in the given position on the current mark.
            NOTE
                    If the position doesn't exist the song will remain unchanged
            """
        if not self.validate_params(params, int):
            print("Error: Incorrect number of params, check help for this command to see required params")
            return
        print(self.executor.toggle_track(False, int(params)))

    def do_play(self, params):
        """ NAME
                           play
                    SYNOPSIS
                           play

                    DESCRIPTION
                            Plays the current mark"""
        print(self.executor.play_marks(end=1))

    def do_playall(self, params):
        """ NAME
                   playall
            SYNOPSIS
                   playall

            DESCRIPTION
                    Plays the whole song"""
        print(self.executor.play_marks(start=0))

    def do_playmarks(self, params):
        """ NAME
                   playmarks
            SYNOPSIS
                   playmarks <n>

            DESCRIPTION
                    Plays n marks of the song from the current position
            NOTE
                    If the requested marks are more than the remaining the song will be played till the end"""
        if not self.validate_params(params, int):
            print("Error: Incorrect number of params, check help for this command to see required params")
            return
        print(self.executor.play_marks(end=int(params)))

    def do_playseconds(self, params):
        """ NAME
                   playseconds
            SYNOPSIS
                   playseconds <n>

            DESCRIPTION
                    Plays n seconds of the song from the current position
            NOTE
                    If the requested seconds are more than the remaining the song will be played till the end"""
        if not self.validate_params(params, int):
            print("Error: Incorrect number of params, check help for this command to see required params")
            return
        print(self.executor.play_seconds(int(params)))

    def validate_params(self, params, expected_type=str):
        """Validates that the params are not empty and are of the expected type"""
        if not params:
            return False
        try:
            expected_type(params)
        except ValueError:
            str_type = str(expected_type)
            str_type = str_type[str_type.find("'") + 1:str_type.rfind("'")]
            print("Expected param of type", str_type)
            return False
        return True
