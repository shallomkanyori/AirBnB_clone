#!/usr/bin/python3
"""unittest for user.py"""

import models
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """testing of the class user"""

    def setUp(self):
        self.user = User()

    def test_user_instance(self):
        self.assertIsInstance(self.user, User)
        self.assertTrue(hasattr(self.user, "id"))
        self.assertTrue(hasattr(self.user, "created_at"))
        self.assertTrue(hasattr(self.user, "updated_at"))

    def test_user_attributes(self):
        self.assertTrue(hasattr(self.user, "email"))
        self.assertTrue(hasattr(self.user, "password"))
        self.assertTrue(hasattr(self.user, "first_name"))
        self.assertTrue(hasattr(self.user, "last_name"))

    def test_user_attribute_default_values(self):
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")

    def test_user_to_dict_method(self):
        user_dict = self.user.to_dict()
        self.assertIsInstance(user_dict, dict)
        self.assertEqual(user_dict['__class__'], 'User')
        self.assertEqual(self.user.id, user_dict['id'])
        self.assertEqual(
            self.user.created_at.isoformat(),
            user_dict['created_at']
        )
        self.assertEqual(
            self.user.updated_at.isoformat(),
            user_dict['updated_at']
        )

    def test_user_str_representation(self):
        user_str = str(self.user)
        self.assertEqual(
            user_str,
            "[User] ({}) {}".format(self.user.id, self.user.__dict__)
        )

    def test_user_dict_representation(self):
        user_dict = self.user.to_dict()
        self.assertEqual(user_dict['__class__'], 'User')
        self.assertIsInstance(user_dict['created_at'], str)
        self.assertIsInstance(user_dict['updated_at'], str)
        self.assertEqual(self.user.id, user_dict['id'])

    def test_user_dict_representation_with_attributes(self):
        self.user.email = "test@example.com"
        self.user.password = "password"
        self.user.first_name = "Mark"
        self.user.last_name = "Edward"
        user_dict = self.user.to_dict()
        self.assertEqual(user_dict['email'], "test@example.com")
        self.assertEqual(user_dict['password'], "password")
        self.assertEqual(user_dict['first_name'], "Mark")
        self.assertEqual(user_dict['last_name'], "Edward")

    def test_user_init_with_args(self):
        user = User(
            email="test@example.com",
            password="password",
            first_name="Mark",
            last_name="Edward"
        )
        self.assertEqual(user.email, "test@example.com")
        self.assertEqual(user.password, "password")
        self.assertEqual(user.first_name, "Mark")
        self.assertEqual(user.last_name, "Edward")


if __name__ == '__main__':
    unittest.main()
