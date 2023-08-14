#!/usr/bin/python3
"""Unittest for the subclass User"""
import models
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """unnitests for city class"""

    def setUp(self):
        self.city = City()

    def test_city_instance(self):
        self.assertIsInstance(self.city, City)
        self.assertTrue(hasattr(self.city, "id"))
        self.assertTrue(hasattr(self.city, "created_at"))
        self.assertTrue(hasattr(self.city, "updated_at"))

    def test_city_attributes(self):
        self.assertTrue(hasattr(self.city, "state_id"))
        self.assertTrue(hasattr(self.city, "name"))

    def test_city_dict_representation(self):
        city_dict = self.city.to_dict()
        self.assertEqual(city_dict['__class__'], 'City')
        self.assertIsInstance(city_dict['created_at'], str)
        self.assertIsInstance(city_dict['updated_at'], str)
        self.assertEqual(self.city.id, city_dict['id'])

    def test_city_to_dict_method(self):
        city_dict = self.city.to_dict()
        self.assertIsInstance(city_dict, dict)
        self.assertEqual(city_dict['__class__'], 'City')
        self.assertEqual(self.city.id, city_dict['id'])
        self.assertEqual(
            self.city.created_at.isoformat(),
            city_dict['created_at']
        )
        self.assertEqual(
            self.city.updated_at.isoformat(),
            city_dict['updated_at']
        )

    def test_city_dict_representation_with_attributes(self):
        self.city.state_id = "123"
        self.city.name = "Test City"
        city_dict = self.city.to_dict()
        self.assertEqual(city_dict['state_id'], "123")
        self.assertEqual(city_dict['name'], "Test City")

    def test_city_init_with_args(self):
        city = City(state_id="123", name="Test City")
        self.assertEqual(city.state_id, "123")
        self.assertEqual(city.name, "Test City")


if __name__ == '__main__':
    unittest.main()
