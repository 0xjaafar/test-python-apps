from blog.blog import Blog
from unittest import TestCase


class BlogTest(TestCase):

    def test_create_blog(self):
        b = Blog('my-blog', 'jaafar')
        self.assertEqual('my-blog', b.title)
        self.assertEqual('jaafar', b.author)
        self.assertListEqual([], b.posts)