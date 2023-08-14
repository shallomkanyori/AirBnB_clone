#!/usr/bin/python3
"""Unittests for base_model.py"""
import os
import time
import uuid
import unittest
from datetime import datetime
import models
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Unittests for the BaseModel class."""

    def tearDown(self):
        """Delete any created files and clear objects dictionary."""

        objects = models.storage.all()
        keys = [k for k in objects.keys()]
        for key in keys:
            del objects[key]

        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_uuid(self):
        """Tests the uuid public instance attribute."""

        b1 = BaseModel()

        self.assertIsInstance(b1, BaseModel)
        self.assertTrue(hasattr(b1, "id"))

        self.assertIsInstance(b1.id, str)
        self.assertIsInstance(uuid.UUID(b1.id), uuid.UUID)

        b2 = BaseModel()
        self.assertNotEqual(b1.id, b2.id)

    def test_datetime(self):
        """Tests the created_at and updated_at public instance attributes."""

        b1 = BaseModel()
        self.assertTrue(hasattr(b1, "created_at"))
        self.assertTrue(hasattr(b1, "updated_at"))

        self.assertIsInstance(b1.created_at, datetime)
        self.assertIsInstance(b1.updated_at, datetime)

        self.assertLess(b1.created_at, b1.updated_at)

        time.sleep(0.001)
        b2 = BaseModel()
        self.assertLess(b1.created_at, b2.created_at)

    def test_from_dict(self):
        """Tests initializing an instance from a dictionary."""

        b1 = BaseModel(None)
        b1.name = "First"
        b1.number = 50

        b1_dict = b1.to_dict()

        b2 = BaseModel(**b1_dict)

        self.assertIsInstance(b2, BaseModel)
        self.assertIsInstance(b2.id, str)
        self.assertIsInstance(uuid.UUID(b2.id), uuid.UUID)
        self.assertIsInstance(b2.created_at, datetime)
        self.assertIsInstance(b2.updated_at, datetime)

        self.assertDictEqual(b1.__dict__, b2.__dict__)
        self.assertDictEqual(b1_dict, b2.to_dict())
        self.assertIsNot(b1, b2)
        self.assertNotEqual(b1, b2)

    def test_from_dict_args_given(self):
        """Make sure *args are ignored with dict instantiation."""

        b1 = BaseModel()
        b1_dict = b1.to_dict()

        b2 = BaseModel("one", 2, 9.5, [1, 2, 3], **b1_dict)

        self.assertIsInstance(b2, BaseModel)

        self.assertDictEqual(b1.__dict__, b2.__dict__)
        self.assertDictEqual(b1_dict, b2.to_dict())
        self.assertIsNot(b1, b2)
        self.assertNotEqual(b1, b2)

    def test_from_dict_missing_attrs(self):
        """Make sure AttributeErrors are raised for missing needed attributes.

            A BaseModel instance should have the id, created_at and updated_at
            attributes at least but no validation is performed to ensure this.
            Trying to access them raises an AttributeError.
        """
        d = {"other": None}
        b1 = BaseModel(**d)
        self.assertIsInstance(b1, BaseModel)

        with self.assertRaises(AttributeError):
            b1.id

        with self.assertRaises(AttributeError):
            b1.created_at

        with self.assertRaises(AttributeError):
            b1.updated_at

    def test_from_dict_invalid_attrs(self):
        """Make sure errors are raised for invalid attributes in dict.

            No validation is performed to ensure that the values of the three
            required attributes (id, created_at, updated_at) are the correct
            types. The created_at and updated_at attributes are converted to
            datetime objects and raise TypeErrors for non-string types and
            ValueErrors for invalid format strings.

        """
        with self.assertRaises(TypeError):
            d = {"created_at": None}
            b1 = BaseModel(**d)

        with self.assertRaises(TypeError):
            d = {"updated_at": 12}
            b1 = BaseModel(**d)

        with self.assertRaises(ValueError):
            d = {"created_at": "hello"}
            b1 = BaseModel(**d)

        with self.assertRaises(ValueError):
            d = {"updated_at": "Mon 12 Jan 2023"}
            b1 = BaseModel(**d)

        # id is assumed to be a valid UUID string but is not validated
        d = {"id": 17}
        b1 = BaseModel(**d)
        self.assertIsInstance(b1, BaseModel)

    def test_str(self):
        """Tests the string representation of an instance."""

        b1 = BaseModel()
        expected = f"[BaseModel] ({b1.id}) {b1.__dict__}"

        self.assertEqual(len(str(b1)), len(expected))

    def test_save(self):
        """Tests the save method."""

        b1 = BaseModel()
        updated_at = b1.updated_at

        time.sleep(0.001)
        b1.save()

        self.assertIsInstance(b1.updated_at, datetime)
        self.assertGreater(b1.updated_at, updated_at)

        self.assertTrue(os.path.exists("file.json"))
        with open("file.json", encoding="utf-8") as f:
            self.assertIn(b1.id, f.read())

    def test_to_dict(self):
        """Tests the to_dict method."""

        b1 = BaseModel()

        expected = {"id": b1.id,
                    "created_at": datetime.isoformat(b1.created_at),
                    "updated_at": datetime.isoformat(b1.updated_at),
                    "__class__": "BaseModel"}
        actual = b1.to_dict()

        self.assertDictEqual(actual, expected)

        self.assertIsInstance(actual["created_at"], str)
        self.assertIsInstance(actual["updated_at"], str)

        created_at_from_dict = datetime.fromisoformat(actual["created_at"])
        updated_at_from_dict = datetime.fromisoformat(actual["updated_at"])

        self.assertIsInstance(created_at_from_dict, datetime)
        self.assertIsInstance(updated_at_from_dict, datetime)

        self.assertEqual(created_at_from_dict, b1.created_at)
        self.assertEqual(updated_at_from_dict, b1.updated_at)

        b1.number = 89
        b1.name = "First model"

        expected["name"] = "First model"
        expected["number"] = 89

        self.assertDictEqual(b1.to_dict(), expected)


if __name__ == "__main__":
    unittest.main()
