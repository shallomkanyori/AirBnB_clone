#!/usr/bin/python3
"""Unittests for base_model.py"""
import time
import uuid
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Unittests for the BaseModel class."""

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
