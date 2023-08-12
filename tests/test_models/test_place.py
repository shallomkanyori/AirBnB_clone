#!/usr/bin/python3
"""unittests for place.py"""

import models
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """tests creating instnces for class place"""

    def setUp(self):
        self.place = Place()

    def test_place_instance(self):
        self.assertIsInstance(self.place, Place)
        self.assertTrue(hasattr(self.place, "id"))
        self.assertTrue(hasattr(self.place, "created_at"))
        self.assertTrue(hasattr(self.place, "updated_at"))

    def test_place_attributes(self):
        self.assertTrue(hasattr(self.place, "city_id"))
        self.assertTrue(hasattr(self.place, "user_id"))
        self.assertTrue(hasattr(self.place, "name"))
        self.assertTrue(hasattr(self.place, "description"))
        self.assertTrue(hasattr(self.place, "number_rooms"))
        self.assertTrue(hasattr(self.place, "number_bathrooms"))
        self.assertTrue(hasattr(self.place, "max_guest"))
        self.assertTrue(hasattr(self.place, "price_by_night"))
        self.assertTrue(hasattr(self.place, "latitude"))
        self.assertTrue(hasattr(self.place, "longitude"))
        self.assertTrue(hasattr(self.place, "amenity_ids"))

    def test_place_attributes_default_values(self):
        self.assertEqual(self.place.city_id, "")
        self.assertEqual(self.place.user_id, "")
        self.assertEqual(self.place.name, "")
        self.assertEqual(self.place.description, "")
        self.assertEqual(self.place.number_rooms, 0)
        self.assertEqual(self.place.number_bathrooms, 0)
        self.assertEqual(self.place.max_guest, 0)
        self.assertEqual(self.place.price_by_night, 0)
        self.assertEqual(self.place.latitude, 0.0)
        self.assertEqual(self.place.longitude, 0.0)
        self.assertEqual(self.place.amenity_ids, [])

    def test_place_dict_representation(self):
        place_dict = self.place.to_dict()
        self.assertEqual(place_dict['__class__'], 'Place')
        self.assertIsInstance(place_dict['created_at'], str)
        self.assertIsInstance(place_dict['updated_at'], str)
        self.assertEqual(self.place.id, place_dict['id'])

    def test_place_dict_representation_with_attributes(self):
        self.place.city_id = "123"
        self.place.user_id = "456"
        self.place.name = "Test Place"
        place_dict = self.place.to_dict()
        self.assertEqual(place_dict['city_id'], "123")
        self.assertEqual(place_dict['user_id'], "456")
        self.assertEqual(place_dict['name'], "Test Place")

    def test_place_init_with_args(self):
        place = Place(city_id="123", user_id="456", name="Test Place")
        self.assertEqual(place.city_id, "123")
        self.assertEqual(place.user_id, "456")
        self.assertEqual(place.name, "Test Place")


if __name__ == '__main__':
    unittest.main()
