#!/usr/bin/python3
"""This module defines the HBNBCommand class."""
import cmd
import models
import shlex

from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class HBNBCommand(cmd.Cmd):
    """Command interpreter for AirBnb."""

    prompt = "(hbnb) "
    __classes = ["BaseModel", "User", "State", "City", "Amenity", "Place",
                 "Review"]
    __error_msgs = ["** class name missing **", "** class doesn't exist **",
                    "** instance id missing **", "** no instance found **",
                    "** attribute name missing **", "** value missing **"]

    def emptyline(self):
        pass

    def is_empty(self, string):
        """Returns true if the string is empty or only spaces.

        Args:
            string (str): the string to check.
        """
        return not string or string.isspace()

    def do_create(self, line):
        """Creates a new BaseModel instance, saves it and prints the id.
        create <class name>
        """

        if self.is_empty(line):
            print(self.__error_msgs[0])

        elif line not in self.__classes:
            print(self.__error_msgs[1])

        else:
            cls = eval(line)
            new = cls()
            new.save()
            print(new.id)

    def do_show(self, line):
        """Prints the string representation of an instance.
        show <class name> <id>
        """

        args = line.split(" ")
        cls_name = args[0] if len(args) > 0 else ""
        inst_id = args[1] if len(args) > 1 else ""

        key = f"{cls_name}.{inst_id}"
        objects = models.storage.all()

        if self.is_empty(cls_name):
            print(self.__error_msgs[0])

        elif cls_name not in self.__classes:
            print(self.__error_msgs[1])

        elif self.is_empty(inst_id):
            print(self.__error_msgs[2])

        elif key not in objects:
            print(self.__error_msgs[3])

        else:
            print(objects[key])

    def do_destroy(self, line):
        """Delete an instance based on class name and id.
        destroy <class name> <id>
        """

        args = line.split(" ")
        cls_name = args[0] if len(args) > 0 else ""
        inst_id = args[1] if len(args) > 1 else ""

        key = f"{cls_name}.{inst_id}"
        objects = models.storage.all()

        if self.is_empty(cls_name):
            print(self.__error_msgs[0])

        elif cls_name not in self.__classes:
            print(self.__error_msgs[1])

        elif self.is_empty(inst_id):
            print(self.__error_msgs[2])

        elif key not in objects:
            print(self.__error_msgs[3])

        else:
            del objects[key]
            models.storage.save()

    def do_all(self, line):
        """Prints the string representation of all instances based on or not on
        the class name.
        all [<class name>]
        """

        objects = models.storage.all()

        if not self.is_empty(line):
            if line not in self.__classes:
                print(self.__error_msgs[1])
            else:
                filtered = [str(obj) for obj
                            in objects.values()
                            if obj.__class__.__name__ == line]
                print(filtered)
        else:
            res = [str(obj) for obj in objects.values()]
            print(res)

    def do_update(self, line):
        """Updates or adds an instance's attribute.
        update <class name> <id> <attribute name> "<attribute value>"
        """

        args = shlex.split(line)

        cls_name = args[0] if len(args) > 0 else ""
        inst_id = args[1] if len(args) > 1 else ""
        attr = args[2] if len(args) > 2 else ""
        attr_val = args[3] if len(args) > 3 else ""

        key = f"{cls_name}.{inst_id}"

        objects = models.storage.all()

        if self.is_empty(cls_name):
            print(self.__error_msgs[0])

        elif cls_name not in self.__classes:
            print(self.__error_msgs[1])

        elif self.is_empty(inst_id):
            print(self.__error_msgs[2])

        elif key not in objects:
            print(self.__error_msgs[3])

        elif self.is_empty(attr):
            print(self.__error_msgs[4])

        elif self.is_empty(attr_val):
            print(self.__error_msgs[5])

        else:
            try:
                attr_val = int(attr_val)
            except ValueError:
                try:
                    attr_val = float(attr_val)
                except ValueError:
                    pass

            setattr(objects[key], attr, attr_val)
            objects[key].save()

    def do_quit(self, line):
        """Quit command to exit the program
        """

        return True

    def do_EOF(self, line):
        """Exit the program.
        """

        print("")
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
