from unittest import mock
from blog import app
from unittest import TestCase
from unittest.mock import patch

from blog.blog import Blog

class AppTest(TestCase):
        
    def test_menu_prompt(self):
        with patch('builtins.input') as mocked_input:
            app.menu()
            mocked_input.assert_called_with(app.MENU_PROMPT)

    def test_menu_calls_print_blogs(self):
        with patch('blog.app.print_blogs') as mocked_print_blogs:
            with patch('builtins.input', return_value='q'):
                app.menu()
                mocked_print_blogs.assert_called()

    def test_print_blogs(self):
        blog = Blog('test', 'jaafar')
        app.blogs = {'test': blog}
        with patch('builtins.print') as mocked_print:
            app.print_blogs()
            mocked_print.assert_called_with('- test by jaafar (0 post)')
