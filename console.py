#!/usr/bin/python3
"""Command interpreter entry module"""

import cmd
class HBNB(cmd.Cmd):
    """This is the actual cmd code"""
    intro = "Command interpreter for AirBnB Project"
    prompt = "(hbnb) "
    def do_EOF(self, line):
        """Handles end of file Character"""
        print()
        return True
    def do_quit(self, line):
        """Exits the program"""
        return True

if __name__ == '__main__':
    HBNB().cmdloop()
