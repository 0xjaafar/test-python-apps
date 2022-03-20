from blog.blog import Blog
from blog.post import Post
from unittest import TestCase


class BlogTest(TestCase):
    def test_create_post_in_blog(self):
        b = Blog("my-blog", "jaafar")
        b.create_post('test', 'my test content')

        self.assertEqual(1, len(b.posts))
        self.assertEqual('test', b.posts[0].title)
        self.assertEqual('my test content', b.posts[0].content)
        