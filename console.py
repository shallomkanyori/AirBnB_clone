#!/usr/bin/python3
"""This module defines the HBNBCommand class."""
import cmd
import sys


class HBNBCommand(cmd.Cmd):
    """Command interpreter for AirBnb."""

    prompt = "(hbnb) "

    def emptyline(self):
        pass

    def do_quit(self, line):
        """Quit command to exit the program
        """
        return True

    do_EOF = do_quit


if __name__ == '__main__':
    HBNBCommand().cmdloop()
