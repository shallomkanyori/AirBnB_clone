#!/usr/bin/python3
"""module documentation"""

import module
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """testing of the review class"""
    def setUp(self):
        self.review = Review()

    def test_review_instance(self):
        self.assertIsInstance(self.review, Review)
        self.assertTrue(hasattr(self.review, "id"))
        self.assertTrue(hasattr(self.review, "created_at"))
        self.assertTrue(hasattr(self.review, "updated_at"))

    def test_review_attributes(self):
        self.assertTrue(hasattr(self.review, "place_id"))
        self.assertTrue(hasattr(self.review, "user_id"))
        self.assertTrue(hasattr(self.review, "text"))

    def test_review_attribute_default_values(self):
        self.assertEqual(self.review.place_id, "")
        self.assertEqual(self.review.user_id, "")
        self.assertEqual(self.review.text, "")

    def test_review_to_dict_method(self):
        review_dict = self.review.to_dict()
        self.assertIsInstance(review_dict, dict)
        self.assertEqual(review_dict['__class__'], 'Review')
        self.assertEqual(self.review.id, review_dict['id'])
        self.assertEqual(
            self.review.created_at.isoformat(),
            review_dict['created_at']
        )
        self.assertEqual(
            self.review.updated_at.isoformat(),
            review_dict['updated_at'])

    def test_review_str_representation(self):
        review_str = str(self.review)
        self.assertEqual(
            review_str, "[Review] ({}) {}"
            .format(self.review.id, self.review.__dict__)
        )

    def test_review_dict_representation(self):
        review_dict = self.review.to_dict()
        self.assertEqual(review_dict['__class__'], 'Review')
        self.assertIsInstance(review_dict['created_at'], str)
        self.assertIsInstance(review_dict['updated_at'], str)
        self.assertEqual(self.review.id, review_dict['id'])

    def test_review_dict_representation_with_attributes(self):
        self.review.place_id = "123"
        self.review.user_id = "456"
        self.review.text = "Nice place!"
        review_dict = self.review.to_dict()
        self.assertEqual(review_dict['place_id'], "123")
        self.assertEqual(review_dict['user_id'], "456")
        self.assertEqual(review_dict['text'], "Nice place!")

    def test_review_init_with_args(self):
        review = Review(place_id="123", user_id="456", text="Nice place!")
        self.assertEqual(review.place_id, "123")
        self.assertEqual(review.user_id, "456")
        self.assertEqual(review.text, "Nice place!")


if __name__ == '__main__':
    unittest.main()
