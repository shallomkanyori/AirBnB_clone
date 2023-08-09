#!/usr/bin/python3
"""unnittest for models/engine/file_storage.py"""
import os
import models
import json
import unittest
from datetime import datetime
from from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """testing file storage class"""
    def setUp(self):
        self.storage = Filestorage()
        self.my_model = BaseModel()

    def tearDown(self):
        """cleaning up"""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

     def test_all(self):
         self.assertEqual(dict, type(models.storage.all()))
