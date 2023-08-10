#!/usr/bin/python3
"""unnittest for models/engine/file_storage.py"""
import os
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """testing file storage class"""
    def setUp(self):
        self.storage = FileStorage()

    def tearDown(self):
        """cleaning up"""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_all(self):
        self.assertEqual(type(self.storage.all()), dict)
