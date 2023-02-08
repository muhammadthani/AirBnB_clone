#!/usr/bin/python3
"""Command interpreter entry module"""
from models.base_model import BaseModel
import cmd


class HBNBCommand(cmd.Cmd):
    """This is the actual cmd code"""
    intro = "Command interpreter for AirBnB Project"
    prompt = "(hbnb) "

    def do_create(self, line):
        """Creates a new instance"""
        if line == "" or line is None:
            print(" ** class name missing ** ")
        elif line not in storage.classes():
            print(" ** class doesn't exist ** ")

    def do_show(self, line):
        """Prints the representation of an instance"""
        if line == "" or line is None:
            print(" ** class name missing ** ")
        elif nline not in storage.classes():
            print(" ** class doesn't exist **")

    def do_EOF(self, line):
        """Handles end of file Character"""
        print()
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
