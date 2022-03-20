from blog.post import Post
from unittest import TestCase


class PostTest(TestCase):
    def test_create_post(self):
        p = Post("test", "test content")
        self.assertEqual("test", p.title)
        self.assertEqual("test content", p.content)

    def test_json(self):
        p = Post("test", "test content")
        expected_json = {
            "title": "test",
            "content": "test content",
        }
        self.assertDictEqual(expected_json, p.json())

    def test_repr(self):
        p = Post("test", "test content")
        expected_repr = "post's title: test"
        self.assertEqual(expected_repr, p.__repr__())