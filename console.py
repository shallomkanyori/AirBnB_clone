#!/usr/bin/python3
"""This module defines the HBNBCommand class."""
import cmd
import models
import re
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
    __dot_methods = ["all", "count", "show", "destroy", "update"]
    __error_msgs = ["** class name missing **", "** class doesn't exist **",
                    "** instance id missing **", "** no instance found **",
                    "** attribute name missing **", "** value missing **"]

    def emptyline(self):
        pass

    def args_split(self, string):
        """Splits a string into a list of strings based on ", ".

        Splits a string by comma and space but not in between double quotes
        or braces.

        Args:
            string(str): the string to split.
        """

        res = []
        buff = []
        in_quotes = False
        in_braces = 0

        for char in string:
            if char == '"':
                in_quotes = not in_quotes
            elif char == '{':
                in_braces += 1
            elif char == '}':
                in_braces -= 1

            if char in ', ' and not in_quotes and in_braces == 0:
                if buff:
                    res.append(''.join(buff).strip())
                    buff = []
            else:
                buff.append(char)

        if buff:
            res.append(''.join(buff).strip())

        return res

    def precmd(self, line):
        """Process dot method version of command."""

        line = line.strip()

        pattern = r'(\w+).(\w+)\((.*?)\)'
        mtch = re.match(pattern, line)

        if mtch:
            cls_name = mtch.group(1)
            method = mtch.group(2)

            if method in self.__dot_methods:
                args = self.args_split(mtch.group(3))

                args = ' '.join(args)

                line = f"{method} {cls_name} {args}"

        return cmd.Cmd.precmd(self, line)

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
        <class name>.show(<id>)
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
        <class name>.destroy(<id>)
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
        <class name>.all()
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
        <class name>.update(<id>, <attribute name> <attribute value>)
        <class name>.update(<id>, {<attribute name>: <attribute value>[, ...]})
        """

        args = self.args_split(line)

        cls_name = args[0] if len(args) > 0 else ""
        inst_id = args[1] if len(args) > 1 else ""

        attrs = {}
        attr_arg = args[2] if len(args) > 2 else ""
        if attr_arg:
            if (attr_arg[0] == '{' and attr_arg[-1] == '}' and
                    type(eval(attr_arg)) is dict):
                attrs = eval(attr_arg)
            else:
                attr_val = args[3] if len(args) > 3 else ""
                if attr_val and attr_val[0] == attr_val[-1] == '"':
                    attr_val = attr_val[1:-1]

                try:
                    attr_val = int(attr_val)
                except ValueError:
                    try:
                        attr_val = float(attr_val)
                    except ValueError:
                        pass
                attrs[attr_arg] = attr_val

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

        elif not attrs:
            print(self.__error_msgs[4])

        else:
            for attr, attr_val in attrs.items():
                if self.is_empty(attr):
                    print(self.__error_msgs[4])
                    break

                elif type(attr_val) is str and self.is_empty(attr_val):
                    print(self.__error_msgs[5])
                    break

                else:
                    setattr(objects[key], attr, attr_val)
                    objects[key].save()

    def do_count(self, line):
        """Print the number of instances of a class.
        <class name>.count()
        """

        if self.is_empty(line):
            print(self.__error_msgs[0])
        elif line not in self.__classes:
            print(self.__error_msgs[1])
        else:
            objects = models.storage.all()
            obj_count = len([obj for obj
                             in objects.values()
                             if obj.__class__.__name__ == line])

            print(obj_count)

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
