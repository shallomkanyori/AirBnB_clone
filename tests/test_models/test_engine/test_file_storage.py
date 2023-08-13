#!/usr/bin/python3
"""unnittest for models/engine/file_storage.py"""
import models
import os
import json
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review


class TestFileStorage(unittest.TestCase):
    """testing file storage class"""
    def setUp(self):
        models.storage._FileStorage__objects = {}
        self.storage = models.storage

    def tearDown(self):
        """cleaning up"""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_objectsects_dict_initialization(self):
        self.assertIsInstance(self.storage._FileStorage__objects, dict)

    def test_all_method_returns_dict(self):
        result = self.storage.all()
        self.assertIsInstance(result, dict)

    def test_new(self):
        B = BaseModel()
        U = User()
        P = Place()
        S = State()
        C = City()
        A = Amenity()
        R = Review()
        objects = self.storage.all()
        self.assertIn("BaseModel." + B.id, objects.keys())
        self.assertIn(B, objects.values())
        self.assertIn("User." + U.id, objects.keys())
        self.assertIn(U, objects.values())
        self.assertIn("Place." + P.id, objects.keys())
        self.assertIn(P, objects.values())
        self.assertIn("State." + S.id, objects.keys())
        self.assertIn(S, objects.values())
        self.assertIn("City." + C.id, objects.keys())
        self.assertIn(C, objects.values())
        self.assertIn("Amenity." + A.id, objects.keys())
        self.assertIn(A, objects.values())
        self.assertIn("Review." + R.id, objects.keys())
        self.assertIn(R, objects.values())

    def test_save(self):
        B = BaseModel()
        U = User()
        P = Place()
        S = State()
        C = City()
        A = Amenity()
        R = Review()
        models.storage.save()
        text_saved = ""
        with open("file.json", "r", encoding="utf-8") as f:
            text_saved = f.read()
            self.assertIn("BaseModel." + B.id, text_saved)
            self.assertIn("User." + U.id, text_saved)
            self.assertIn("Place." + P.id, text_saved)
            self.assertIn("State." + S.id, text_saved)
            self.assertIn("City." + C.id, text_saved)
            self.assertIn("Amenity." + A.id, text_saved)
            self.assertIn("Review." + R.id, text_saved)

    def test_reload(self):
        B = BaseModel()
        U = User()
        P = Place()
        S = State()
        C = City()
        A = Amenity()
        R = Review()
        models.storage.save()
        models.storage.reload()
        objects = self.storage.all()
        self.assertIn("BaseModel." + B.id, objects)
        self.assertIn("User." + U.id, objects)
        self.assertIn("Place." + P.id, objects)
        self.assertIn("State." + S.id, objects)
        self.assertIn("City." + C.id, objects)
        self.assertIn("Amenity." + A.id, objects)
        self.assertIn("Review." + R.id, objects)


if __name__ == "__main__":
    unittest.main()
