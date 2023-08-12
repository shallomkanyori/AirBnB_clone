#!/usr/bin/python3
"""unittest for state"""

import models
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """testing of the State class"""
    def setUp(self):
        self.state = State()

    def test_state_instance(self):
        self.assertIsInstance(self.state, State)
        self.assertTrue(hasattr(self.state, "id"))
        self.assertTrue(hasattr(self.state, "created_at"))
        self.assertTrue(hasattr(self.state, "updated_at"))

    def test_state_attributes(self):
        self.assertTrue(hasattr(self.state, "name"))

    def test_state_attribute_default_values(self):
        self.assertEqual(self.state.name, "")

    def test_state_to_dict_method(self):
        state_dict = self.state.to_dict()
        self.assertIsInstance(state_dict, dict)
        self.assertEqual(state_dict['__class__'], 'State')
        self.assertEqual(self.state.id, state_dict['id'])
        self.assertEqual(
            self.state.created_at.isoformat(),
            state_dict['created_at']
        )
        self.assertEqual(
            self.state.updated_at.isoformat(),
            state_dict['updated_at']
        )

    def test_state_dict_representation(self):
        state_dict = self.state.to_dict()
        self.assertEqual(state_dict['__class__'], 'State')
        self.assertIsInstance(state_dict['created_at'], str)
        self.assertIsInstance(state_dict['updated_at'], str)
        self.assertEqual(self.state.id, state_dict['id'])

    def test_state_dict_representation_with_attributes(self):
        self.state.name = "Test State"
        state_dict = self.state.to_dict()
        self.assertEqual(state_dict['name'], "Test State")

    def test_state_init_with_args(self):
        state = State(name="Test State")
        self.assertEqual(state.name, "Test State")


if __name__ == '__main__':
    unittest.main()
