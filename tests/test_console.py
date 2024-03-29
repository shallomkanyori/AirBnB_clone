#!/usr/bin/python3
"""Unittests for console.py."""
from console import HBNBCommand
from io import StringIO
import models
import os
import sys
import unittest
from unittest.mock import patch
import uuid

from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class TestConsoleBase(unittest.TestCase):
    """Base class for unittests for the console."""

    error_msgs = ["** class name missing **", "** class doesn't exist **",
                  "** instance id missing **", "** no instance found **",
                  "** attribute name missing **", "** value missing **",
                  "*** Unknown syntax: "]

    def tearDown(self):
        """Delete any created files and clear objects dictionary."""

        objects = models.storage.all()
        keys = [k for k in objects.keys()]
        for key in keys:
            del objects[key]

        try:
            os.remove("file.json")
        except OSError:
            pass

    def get_output(self, cmd):
        """Returns the output of running a command on the console.

        Args:
            cmd: the command to run.
        """

        res = ""

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(cmd)
            res = f.getvalue().strip()

        return res


class TestConsole_help(TestConsoleBase):
    """Unit tests for the help command of the console."""

    def assert_output_help(self, cmd):
        """Tests the output of the help command.

        Args:
            cmd: the command argument to the help command.
        """

        cmd = f"help {cmd}"
        res = self.get_output(cmd)
        self.assertNotEqual(res, "")

    def test_help(self):
        """Tests the help command."""

        no_arg_res = self.get_output("help")
        self.assertNotEqual(no_arg_res, "")

        self.assert_output_help("help")
        self.assert_output_help("quit")
        self.assert_output_help("EOF")
        self.assert_output_help("create")
        self.assert_output_help("show")
        self.assert_output_help("destroy")
        self.assert_output_help("all")
        self.assert_output_help("update")


class TestConsole_other(TestConsoleBase):
    """Unit tests for miscellaneous commands of the console.

    Unittests for the quit commands and the handling of empty lines.
    """

    def test_quit(self):
        """Tests the quit command."""

        with patch('sys.stdout', new=StringIO()) as f:
            res_val = HBNBCommand().onecmd("quit")
            self.assertTrue(res_val)
            res = f.getvalue().strip()
            self.assertEqual(res, "")

        with patch('sys.stdout', new=StringIO()) as f:
            res_val = HBNBCommand().onecmd("quit other arguments")
            self.assertTrue(res_val)
            res = f.getvalue().strip()
            self.assertEqual(res, "")

    def test_EOF(self):
        """Tests the EOF (^D) command."""

        with patch('sys.stdout', new=StringIO()) as f:
            res_val = HBNBCommand().onecmd("EOF")
            self.assertTrue(res_val)
            res = f.getvalue().strip()
            self.assertEqual(res, "")

        with patch('sys.stdout', new=StringIO()) as f:
            res_val = HBNBCommand().onecmd("EOF other arguments")
            self.assertTrue(res_val)
            res = f.getvalue().strip()
            self.assertEqual(res, "")

    def test_emptyline(self):
        """Tests the handling of empty command lines."""

        res = self.get_output("")
        self.assertEqual(res, "")

        res = self.get_output("     ")
        self.assertEqual(res, "")

        res = self.get_output("\t")
        self.assertEqual(res, "")


class TestConsole_create(TestConsoleBase):
    """Unit tests for the create command of the console."""

    def assert_output_create(self, cls):
        """Tests the output of the create command.

        Args:
            cls: the name of the class to create an instance of.
        """

        cmd = f"create {cls}"

        res = self.get_output(cmd)
        self.assertIsNotNone(res)
        self.assertIsInstance(uuid.UUID(res), uuid.UUID)
        key = f"{cls}.{res}"
        self.assertIn(key, models.storage.all())

    def test_create(self):
        """Tests the create command."""

        self.assert_output_create("BaseModel")
        self.assert_output_create("User")
        self.assert_output_create("State")
        self.assert_output_create("City")
        self.assert_output_create("Amenity")
        self.assert_output_create("Place")
        self.assert_output_create("Review")

    def test_create_errors(self):
        """Makes sure the correct errors are displayed for create command."""

        res = self.get_output("create")
        self.assertEqual(res, self.error_msgs[0])

        res = self.get_output("create MyModel")
        self.assertEqual(res, self.error_msgs[1])


class TestConsole_count(TestConsoleBase):
    """Unit tests for the .count() command."""

    def test_count(self):
        """Tets the .count() method."""

        res = self.get_output("BaseModel.count()")
        self.assertEqual(res, "0")
        b1 = BaseModel()
        res = self.get_output("BaseModel.count()")
        self.assertEqual(res, "1")

        res = self.get_output("User.count()")
        self.assertEqual(res, "0")
        u1 = User()
        u2 = User()
        res = self.get_output("User.count()")
        self.assertEqual(res, "2")

        res = self.get_output("State.count()")
        self.assertEqual(res, "0")
        s1 = State()
        s2 = State()
        s3 = State()
        res = self.get_output("State.count()")
        self.assertEqual(res, "3")

        res = self.get_output("City.count()")
        self.assertEqual(res, "0")
        c1 = City()
        res = self.get_output("City.count()")
        self.assertEqual(res, "1")

        res = self.get_output("Amenity.count()")
        self.assertEqual(res, "0")
        a1 = Amenity()
        a2 = Amenity()
        res = self.get_output("Amenity.count()")
        self.assertEqual(res, "2")

        res = self.get_output("Place.count()")
        self.assertEqual(res, "0")
        p1 = Place()
        res = self.get_output("Place.count()")
        self.assertEqual(res, "1")

        res = self.get_output("Review.count()")
        self.assertEqual(res, "0")
        r1 = Review()
        r2 = Review()
        res = self.get_output("Review.count()")
        self.assertEqual(res, "2")


class TestConsole_show(TestConsoleBase):
    """Unit tests for the show command of the console."""

    def get_output_show(self, cls, inst_id):
        """Returns the output of the show command.

        Args:
            cls: the name of the class of the the instance to show.
            inst_id: the id of the instance to show.
        """

        cmd = f"show {cls} {inst_id}"
        res = self.get_output(cmd)
        return res

    def assert_output_show(self, cls):
        """Tests the output of the show command.

        Args:
            cls: the name of the class of the instance to show.
        """

        inst = eval(cls)()
        res = self.get_output_show(cls, inst.id)
        self.assertEqual(res, str(inst))

    def test_show(self):
        """Tests the show command."""

        self.assert_output_show("BaseModel")
        self.assert_output_show("User")
        self.assert_output_show("State")
        self.assert_output_show("City")
        self.assert_output_show("Amenity")
        self.assert_output_show("Place")
        self.assert_output_show("Review")

    def test_show_errors(self):
        """Make sure correct errors are displayed for the show command."""

        res = self.get_output("show")
        self.assertEqual(res, self.error_msgs[0])

        res = self.get_output("show MyModel")
        self.assertEqual(res, self.error_msgs[1])

        res = self.get_output("show BaseModel")
        self.assertEqual(res, self.error_msgs[2])

        res = self.get_output("show BaseModel 123")
        self.assertEqual(res, self.error_msgs[3])

    def test_show_extra_args(self):
        """Make sure any other arguments to the show command are ignored."""

        b = BaseModel()

        cmd = f"show BaseModel {b.id} other arguments"
        res = self.get_output(cmd)
        self.assertEqual(res, str(b))

    def assert_output_show_dot(self, cls):
        """Tests the output of the .show() command.

        Args:
            cls: the name of the class of the instance to show.
        """

        inst = eval(cls)()
        show_res = self.get_output_show(cls, inst.id)

        cmd = f"{cls}.show({inst.id})"
        res = self.get_output(cmd)
        self.assertEqual(res, show_res)
        self.assertEqual(res, str(inst))

    def test_show_dot(self):
        """Tests the .show() command"""

        self.assert_output_show_dot("BaseModel")
        self.assert_output_show_dot("User")
        self.assert_output_show_dot("State")
        self.assert_output_show_dot("City")
        self.assert_output_show_dot("Amenity")
        self.assert_output_show_dot("Place")
        self.assert_output_show_dot("Review")

    def test_show_dot_errors(self):
        """Make sure correct errors are displayed for the .show() command."""

        res = self.get_output(".show()")
        self.assertEqual(res, self.error_msgs[6] + ".show()")

        res = self.get_output("MyModel.show()")
        self.assertEqual(res, self.error_msgs[1])

        res = self.get_output("BaseModel.show()")
        self.assertEqual(res, self.error_msgs[2])

        res = self.get_output("BaseModel.show(123)")
        self.assertEqual(res, self.error_msgs[3])

    def test_show_dot_extra_args(self):
        """Make sure any other arguments to the .show() command are ignored."""

        b = BaseModel()

        cmd_str = f"BaseModel.show({b.id}, other, arguments)"
        res = self.get_output(cmd_str)
        self.assertEqual(res, str(b))


class TestConsole_destroy(TestConsoleBase):
    """Unit tests for the destroy command of the console."""

    def assert_output_destroy(self, cls):
        """Tests the output of the destroy command.

        Args:
            cls: the name of the class of the instance to destroy.
        """

        inst = eval(cls)()

        cmd = f"destroy {cls} {inst.id}"
        res = self.get_output(cmd)
        self.assertEqual(res, "")
        key = f"{cls}.{inst.id}"
        self.assertNotIn(key, models.storage.all())

    def test_destroy(self):
        """Tests the destroy command."""

        self.assert_output_destroy("BaseModel")
        self.assert_output_destroy("User")
        self.assert_output_destroy("State")
        self.assert_output_destroy("City")
        self.assert_output_destroy("Amenity")
        self.assert_output_destroy("Place")
        self.assert_output_destroy("Review")

    def test_destroy_errors(self):
        """Make sure correct errors are displayed for the destroy command."""

        res = self.get_output("destroy")
        self.assertEqual(res, self.error_msgs[0])

        res = self.get_output("destroy MyModel")
        self.assertEqual(res, self.error_msgs[1])

        res = self.get_output("destroy BaseModel")
        self.assertEqual(res, self.error_msgs[2])

        res = self.get_output("destroy BaseModel 123")
        self.assertEqual(res, self.error_msgs[3])

    def test_destroy_extra_args(self):
        """Make sure any other arguments to the destroy command are ignored."""

        b = BaseModel()

        cmd = f"destroy BaseModel {b.id} other arguments"
        res = self.get_output(cmd)
        self.assertEqual(res, "")
        key = f"BaseModel.{b.id}"
        self.assertNotIn(key, models.storage.all())

    def assert_output_destroy_dot(self, cls):
        """Tests the output of the .destroy() command.

        Args:
            cls: the name of the class of the instance to destroy.
        """

        inst = eval(cls)()

        cmd = f"{cls}.destroy({inst.id})"
        res = self.get_output(cmd)
        self.assertEqual(res, "")
        key = f"{cls}.{inst.id}"
        self.assertNotIn(key, models.storage.all())

    def test_destroy_dot(self):
        """Tests the .destroy() command"""

        self.assert_output_destroy_dot("BaseModel")
        self.assert_output_destroy_dot("User")
        self.assert_output_destroy_dot("State")
        self.assert_output_destroy_dot("City")
        self.assert_output_destroy_dot("Amenity")
        self.assert_output_destroy_dot("Place")
        self.assert_output_destroy_dot("Review")

    def test_destroy_dot_errors(self):
        """Test errors for the .destroy() command.

        Make sure correct errors are displayed for the .destroy() command.
        """

        res = self.get_output(".destroy()")
        self.assertEqual(res, self.error_msgs[6] + ".destroy()")

        res = self.get_output("MyModel.destroy()")
        self.assertEqual(res, self.error_msgs[1])

        res = self.get_output("BaseModel.destroy()")
        self.assertEqual(res, self.error_msgs[2])

        res = self.get_output("BaseModel.destroy(123)")
        self.assertEqual(res, self.error_msgs[3])

    def test_destroy_dot_extra_args(self):
        """Test other arguments to the .destroy() command.
        Make sure any other arguments to the .destroy() command are ignored.
        """

        b = BaseModel()

        cmd = f"BaseModel.destroy({b.id}, other, arguments)"
        res = self.get_output(cmd)
        self.assertEqual(res, "")
        key = f"BaseModel.{b.id}"
        self.assertNotIn(key, models.storage.all())


class TestConsole_all(TestConsoleBase):
    """Unit tests for the all command of the console."""

    def assert_output_all(self, cls):
        """Tests the output of the all command..

        Args:
            cls: the name of the class to print all instances of.
        """

        objects = models.storage.all()
        obj_ids = [obj.id for obj in objects.values()
                   if obj.__class__.__name__ == cls]

        cmd = f"all {cls}"
        res = self.get_output(cmd)

        for inst_id in obj_ids:
            self.assertIn(inst_id, res)

    def test_all(self):
        """Tests the all command."""

        no_arg_res = self.get_output("all")
        self.assertEqual(no_arg_res, "[]")

        self.assertEqual(self.get_output("all BaseModel"), "[]")
        b1 = BaseModel()
        b2 = BaseModel()
        self.assert_output_all("BaseModel")

        self.assertEqual(self.get_output("all User"), "[]")
        u1 = User()
        self.assert_output_all("User")

        self.assertEqual(self.get_output("all State"), "[]")
        s1 = State()
        s2 = State()
        s3 = State()
        self.assert_output_all("State")

        self.assertEqual(self.get_output("all City"), "[]")
        c1 = City()
        self.assert_output_all("City")

        self.assertEqual(self.get_output("all Amenity"), "[]")
        a1 = Amenity()
        self.assert_output_all("Amenity")

        self.assertEqual(self.get_output("all Place"), "[]")
        p1 = Place()
        self.assert_output_all("Place")

        self.assertEqual(self.get_output("all Review"), "[]")
        r1 = Review()
        self.assert_output_all("Review")

        no_arg_res = self.get_output("all")
        self.assertIn(b1.id, no_arg_res)
        self.assertIn(b2.id, no_arg_res)
        self.assertIn(u1.id, no_arg_res)
        self.assertIn(s1.id, no_arg_res)
        self.assertIn(s2.id, no_arg_res)
        self.assertIn(s3.id, no_arg_res)
        self.assertIn(c1.id, no_arg_res)
        self.assertIn(a1.id, no_arg_res)
        self.assertIn(p1.id, no_arg_res)
        self.assertIn(r1.id, no_arg_res)

    def test_all_errors(self):
        """Make sure correct errors are displayed for the all command."""

        res = self.get_output("all MyModel")
        self.assertEqual(res, self.error_msgs[1])

        res = self.get_output("all BaseModel other arguments")
        self.assertEqual(res, self.error_msgs[1])

    def assert_output_all_dot_one(self, cls):
        """Tests the output of the .all() command with one instance of a class.

        Args:
            cls: the name of the class of the instance to all.
        """

        inst = eval(cls)()

        res = self.get_output(f"{cls}.all()")
        self.assertIn(inst.id, res)

    def test_all_dot(self):
        """Tests the .all() command"""

        self.assert_output_all_dot_one("BaseModel")
        self.assert_output_all_dot_one("User")
        self.assert_output_all_dot_one("State")
        self.assert_output_all_dot_one("City")
        self.assert_output_all_dot_one("Amenity")
        self.assert_output_all_dot_one("Place")
        self.assert_output_all_dot_one("Review")

    def test_all_dot_errors(self):
        """Test errors for the .all() command.

        Make sure correct errors are displayed for the .all() command.
        """

        res = self.get_output(".all()")
        self.assertEqual(res, self.error_msgs[6] + ".all()")

        res = self.get_output("MyModel.all()")
        self.assertEqual(res, self.error_msgs[1])

        res = self.get_output("BaseModel.all(other, arguments)")
        self.assertEqual(res, self.error_msgs[1])


class TestConsole_update(TestConsoleBase):
    """Unit tests for the update command of the console."""

    def assert_output_update_attrs(self, cls, inst_id, attr_name, attr_val,
                                   string):
        """Tests the output of the update command with attibutes.

        Args:
            cls: the name of the class of the instance to update
            inst_id: the id of the instance to update
            attr_name: the name of the attribute to add or update.
            attr_val: the new value of the attribute.
            string: whether the value is a string or not.
        """

        cmd = f'update {cls} {inst_id} {attr_name} '
        cmd += f'"{attr_val}"' if type(attr_val) is str else f'{attr_val}'
        res = self.get_output(cmd)
        self.assertEqual(res, "")

        key = f"{cls}.{inst_id}"
        objects = models.storage.all()
        self.assertIn(key, objects)

        obj = objects[key]
        self.assertTrue(hasattr(obj, attr_name))
        obj_attr = getattr(obj, attr_name)
        if string or type(attr_val) is not str:
            self.assertTrue(obj_attr == attr_val)
        else:
            self.assertTrue(obj_attr == eval(attr_val))

    def assert_output_update(self, cls):
        """Tests the output of the update command.

        Args:
            cls: the name of the class of the the instance to update
        """
        inst = eval(cls)()

        attr_name = "string_arg"
        attr_val = "string"
        self.assert_output_update_attrs(cls, inst.id, attr_name, attr_val,
                                        True)

        attr_name = "int_arg"
        attr_val = 89
        self.assert_output_update_attrs(cls, inst.id, attr_name, attr_val,
                                        False)

        attr_name = "float_arg"
        attr_val = 12.7
        self.assert_output_update_attrs(cls, inst.id, attr_name, attr_val,
                                        False)

        attr_name = "space_string_arg"
        attr_val = "one two"
        self.assert_output_update_attrs(cls, inst.id, attr_name, attr_val,
                                        True)

        attr_name = "string_int_arg"
        attr_val = "90"
        self.assert_output_update_attrs(cls, inst.id, attr_name, attr_val,
                                        False)

        attr_name = "string_float_arg"
        attr_val = "5.4"
        self.assert_output_update_attrs(cls, inst.id, attr_name, attr_val,
                                        False)

    def test_update(self):
        """Tests the update command."""

        self.assert_output_update("BaseModel")
        self.assert_output_update("User")
        self.assert_output_update("State")
        self.assert_output_update("City")
        self.assert_output_update("Amenity")
        self.assert_output_update("Place")
        self.assert_output_update("Review")

    def test_update_errors(self):
        """Make sure correct errors are displayed for the update command."""

        res = self.get_output("update")
        self.assertEqual(res, self.error_msgs[0])

        res = self.get_output("update MyModel")
        self.assertEqual(res, self.error_msgs[1])

        res = self.get_output("update BaseModel")
        self.assertEqual(res, self.error_msgs[2])

        res = self.get_output("update BaseModel 123")
        self.assertEqual(res, self.error_msgs[3])

        b = BaseModel()
        cmd = f"update BaseModel {b.id}"
        res = self.get_output(cmd)
        self.assertEqual(res, self.error_msgs[4])

        cmd = f"update BaseModel {b.id} attr"
        res = self.get_output(cmd)
        self.assertEqual(res, self.error_msgs[5])

    def test_update_extra_args(self):
        """Make sure any other arguments to the update command are ignored."""

        b = BaseModel()

        attr = "attr"
        attr_val = 89

        cmd = f"update BaseModel {b.id} {attr} {attr_val} other arguments"
        res = self.get_output(cmd)
        self.assertEqual(res, "")

        key = f"BaseModel.{b.id}"
        objects = models.storage.all()
        self.assertIn(key, models.storage.all())

        obj = objects[key]
        self.assertTrue(hasattr(obj, attr))
        self.assertTrue(getattr(obj, attr) == attr_val)

    def assert_output_update_dot_atts(self, cls, inst_id, attr_name, attr_val,
                                      string):
        """Tests the output of the .update() command with attibutes.

        Args:
            cls: the name of the class of the the instance to update
            inst_id: the id of the instance to update
            attr_name: the name of the attribute to add or update.
            attr_val: the new value of the attribute.
            string: whether or not the attribute value is a string
        """

        cmd = f'{cls}.update({inst_id}, {attr_name}, '
        cmd += f'"{attr_val}")' if type(attr_val) is str else f'{attr_val})'
        res = self.get_output(cmd)
        self.assertEqual(res, "")

        key = f"{cls}.{inst_id}"
        objects = models.storage.all()
        self.assertIn(key, objects)

        obj = objects[key]
        self.assertTrue(hasattr(obj, attr_name))
        obj_attr = getattr(obj, attr_name)
        if string or type(attr_val) is not str:
            self.assertTrue(obj_attr == attr_val)
        else:
            self.assertTrue(obj_attr == eval(attr_val))

    def assert_output_update_dot(self, cls):
        """Tests the output of the .update() command.

        Args:
            cls: the name of the class of the the instance to update
        """
        inst = eval(cls)()

        attr_name = "string_arg"
        attr_val = "string"
        self.assert_output_update_dot_atts(cls, inst.id, attr_name, attr_val,
                                           True)

        attr_name = "int_arg"
        attr_val = 89
        self.assert_output_update_dot_atts(cls, inst.id, attr_name, attr_val,
                                           False)

        attr_name = "float_arg"
        attr_val = 12.7
        self.assert_output_update_dot_atts(cls, inst.id, attr_name, attr_val,
                                           False)

        attr_name = "space_string_arg"
        attr_val = "one two"
        self.assert_output_update_dot_atts(cls, inst.id, attr_name, attr_val,
                                           True)

        attr_name = "string_int_arg"
        attr_val = "90"
        self.assert_output_update_dot_atts(cls, inst.id, attr_name, attr_val,
                                           False)

        attr_name = "string_float_arg"
        attr_val = "5.4"
        self.assert_output_update_dot_atts(cls, inst.id, attr_name, attr_val,
                                           False)

    def test_update_dot(self):
        """Tests the .update() command."""

        self.assert_output_update_dot("BaseModel")
        self.assert_output_update_dot("User")
        self.assert_output_update_dot("State")
        self.assert_output_update_dot("City")
        self.assert_output_update_dot("Amenity")
        self.assert_output_update_dot("Place")
        self.assert_output_update_dot("Review")

    def test_update_dot_errors(self):
        """Make sure correct errors are displayed for the .update() command."""

        res = self.get_output(".update()")
        self.assertEqual(res, self.error_msgs[6] + ".update()")

        res = self.get_output("MyModel.update()")
        self.assertEqual(res, self.error_msgs[1])

        res = self.get_output("BaseModel.update()")
        self.assertEqual(res, self.error_msgs[2])

        res = self.get_output("BaseModel.update(123)")
        self.assertEqual(res, self.error_msgs[3])

        b = BaseModel()
        cmd = f"BaseModel.update({b.id})"
        res = self.get_output(cmd)
        self.assertEqual(res, self.error_msgs[4])

        cmd = f"BaseModel.update({b.id}, attr)"
        res = self.get_output(cmd)
        self.assertEqual(res, self.error_msgs[5])

    def test_update_dot_extra_args(self):
        """Make sure any other arguments to the .update() command are ignored.
        """

        b = BaseModel()

        attr = "attr"
        attr_val = 89

        cmd = f"BaseModel.update({b.id}, {attr}, {attr_val}, other, arguments)"
        res = self.get_output(cmd)
        self.assertEqual(res, "")

        key = f"BaseModel.{b.id}"
        objects = models.storage.all()
        self.assertIn(key, models.storage.all())

        obj = objects[key]
        self.assertTrue(hasattr(obj, attr))
        self.assertTrue(getattr(obj, attr) == attr_val)


if __name__ == "__main__":
    unittest.main()
