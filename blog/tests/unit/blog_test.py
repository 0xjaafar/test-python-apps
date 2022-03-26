from blog.blog import Blog
from blog.post import Post
from unittest import TestCase


class BlogTest(TestCase):
    def test_create_blog(self):
        b = Blog("my-blog", "jaafar")
        self.assertEqual("my-blog", b.title)
        self.assertEqual("jaafar", b.author)
        self.assertListEqual([], b.posts)

    def test_json(self):
        b = Blog("my-blog", "jaafar")
        expected_json = {"title": "my-blog", "author": "jaafar", "posts": []}
        self.assertDictEqual(expected_json, b.json())

    def test_repr(self):
        b = Blog("my-blog", "jaafar")
        expected_repr = "my-blog by jaafar (0 post)"
        self.assertEqual(expected_repr, b.__repr__())

    def test_repr_multi_posts(self):
        p = Post("test", "my test content")
        b = Blog("my-blog", "jaafar")
        b.posts.append(p)
        b.posts.append(p)
        expected_repr = "my-blog by jaafar (2 posts)"
        self.assertEqual(expected_repr, b.__repr__())
