from unittest import mock
from blog import app
from unittest import TestCase
from unittest.mock import patch
from blog.blog import Blog
from blog.post import Post
from blog.app import POST_TEMPLATE


class AppTest(TestCase):

    def test_menu_prompt(self):
        with patch("builtins.input") as mocked_input:
            app.menu()
            mocked_input.assert_called_with(app.MENU_PROMPT)

    def test_menu_calls_print_blogs(self):
        with patch("blog.app.ask_print_blogs") as mocked_ask_print_blogs:
            with patch("builtins.input", return_value="q"):
                app.menu()
                mocked_ask_print_blogs.assert_called()

    def test_ask_print_blogs(self):
        blog = Blog("test", "jaafar")
        app.blogs = {"test": blog}
        with patch("builtins.print") as mocked_print:
            app.ask_print_blogs()
            mocked_print.assert_called_with("- test by jaafar (0 post)")

    def test_ask_create_blog(self):
        with patch("builtins.input") as mocked_input:
            mocked_input.side_effect = ("Test", "Jaafar")
            app.ask_create_blog()
            self.assertIsNotNone(app.blogs.get("Test"))

    def test_ask_read_blog(self):
        with patch("builtins.input", return_value="Test"):
            blog = Blog("Test", "jaafar")
            app.blogs = {"Test": blog}
            with patch("blog.app.print_posts") as mocked_print_posts:
                app.ask_read_blog()
                mocked_print_posts.assert_called_with(blog)

    def test_print_posts(self):
        p = Post("Test", "My content")
        with patch("blog.app.print_post") as mocked_print_post:
            app.print_post(p)
            mocked_print_post.assert_called_with(p)

    def test_ask_create_post(self):
        with patch("builtins.input") as mocked_input:
            b = Blog("MyBlogName", "jaafar")
            app.blogs["MyBlogName"] = b
            mocked_input.side_effect = ('MyBlogName', 'MyPostTitle','MyContent')
            app.ask_create_post()
            self.assertEqual('MyPostTitle', app.blogs['MyBlogName'].posts[0].title)
            self.assertEqual('MyContent', app.blogs['MyBlogName'].posts[0].content)
