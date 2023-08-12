#!/usr/bin/python3
"""unittest for amenity.py"""
import models
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """testing of the class amenity"""
    def setUp(self):
        self.amenity = Amenity()

    def test_amenity_instance(self):
        self.assertIsInstance(self.amenity, Amenity)
        self.assertTrue(hasattr(self.amenity, "id"))
        self.assertTrue(hasattr(self.amenity, "created_at"))
        self.assertTrue(hasattr(self.amenity, "updated_at"))

    def test_amenity_attributes(self):
        self.assertTrue(hasattr(self.amenity, "name"))

    def test_amenity_attribute_default_values(self):
        self.assertEqual(self.amenity.name, "")

    def test_amenity_to_dict_method(self):
        amenity_dict = self.amenity.to_dict()
        self.assertIsInstance(amenity_dict, dict)
        self.assertEqual(amenity_dict['__class__'], 'Amenity')
        self.assertEqual(self.amenity.id, amenity_dict['id'])
        self.assertEqual(
            self.amenity.created_at.isoformat(),
            amenity_dict['created_at']
        )
        self.assertEqual(
            self.amenity.updated_at.isoformat(),
            amenity_dict['updated_at']
        )

    def test_amenity_str_representation(self):
        amenity_str = str(self.amenity)
        self.assertEqual(
            amenity_str, "[Amenity] ({}) {}"
            .format(self.amenity.id, self.amenity.__dict__)
        )

    def test_amenity_dict_representation(self):
        amenity_dict = self.amenity.to_dict()
        self.assertEqual(amenity_dict['__class__'], 'Amenity')
        self.assertIsInstance(amenity_dict['created_at'], str)
        self.assertIsInstance(amenity_dict['updated_at'], str)
        self.assertEqual(self.amenity.id, amenity_dict['id'])

    def test_amenity_dict_representation_with_attributes(self):
        self.amenity.name = "Swimming Pool"
        amenity_dict = self.amenity.to_dict()
        self.assertEqual(amenity_dict['name'], "Swimming Pool")

    def test_amenity_init_with_args(self):
        amenity = Amenity(name="Swimming Pool")
        self.assertEqual(amenity.name, "Swimming Pool")


if __name__ == '__main__':
    unittest.main()
