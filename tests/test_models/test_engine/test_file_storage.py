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
        self.storage = FileStorage()

    def tearDown(self):
        """cleaning up"""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_all(self):
        self.assertEqual(type(self.storage.all()), dict)

    def test_objects_dict_initialization(self):
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
        models.storage.new(B)
        models.storage.new(U)
        models.storage.new(P)
        models.storage.new(S)
        models.storage.new(C)
        models.storage.new(A)
        models.storage.new(R)
        self.assertIn("BaseModel." + B.id, models.storage.all().keys())
        self.assertIn(B, models.storage.all().values())
        self.assertIn("User." + U.id, models.storage.all().keys())
        self.assertIn(U, models.storage.all().values())
        self.assertIn("Place." + P.id, models.storage.all().keys())
        self.assertIn(P, models.storage.all().values())
        self.assertIn("State." + S.id, models.storage.all().keys())
        self.assertIn(S, models.storage.all().values())
        self.assertIn("City." + C.id, models.storage.all().keys())
        self.assertIn(C, models.storage.all().values())
        self.assertIn("Amenity." + A.id, models.storage.all().keys())
        self.assertIn(A, models.storage.all().values())
        self.assertIn("Review." + R.id, models.storage.all().keys())
        self.assertIn(R, models.storage.all().values())

    def test_save(self):
        B = BaseModel()
        U = User()
        P = Place()
        S = state()
        C = City()
        A = Amenity()
        R = Review()
        models.storage.new(B)
        models.storage.new(U)
        models.storage.new(P)
        models.storage.new(S)
        models.storage.new(C)
        models.storage.new(A)
        models.storage.new(R)
        models.torage.save()
        text_saved = ""
        with open("file.json", "r") as f:
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
        models.storage.new(B)
        models.storage.new(U)
        models.storage.new(P)
        models.storage.new(S)
        models.storage.new(C)
        models.storage.new(A)
        models.storage.new(R)
        models.torage.save()
        models.storage.reload()
        obj = FileStorage.__FileStorae__objects
        self.assertIn("BaseModel." + B.id, obj)
        self.assertIn("User." + U.id, obj)
        self.assertIn("Place." + P.id, obj)
        self.assertIn("State." + S.id, obj)
        self.assertIn("City." + C.id, obj)
        self.assertIn("Amenity." + A.id, obj)
        self.assertIn("Review." + R.id, obj)


if __name__ == "__main__":
    unittest.main()
