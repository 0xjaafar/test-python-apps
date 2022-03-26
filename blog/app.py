from typing import Dict
from blog.post import Post
from blog.blog import Blog


blogs: Dict = dict()  # blog name -> blog object

MENU_PROMPT = "Enter 'c' to create a blog, 'l' top list blogs, 'r' to read one, 'p' to create a post, or 'q' to quit."
POST_TEMPLATE = """
    ---{}---
    {}
"""


def menu():
    # show the user available blog
    # let the user make choice
    # do something with the choice
    # eventually exit
    ask_print_blogs()
    selection = input(MENU_PROMPT)


def ask_print_blogs():
    # print the available blogs
    for key, blog in blogs.items():
        print("- {}".format(blog))

def ask_create_blog():
    title = input("Enter blog title: ")
    author = input("Enter blog author: ")
    blogs[title] = Blog(title, author)

def ask_read_blog():
    title = input("Enter the blog title you want to read: ")
    print_posts(blogs[title])

def print_posts(blog: Blog):
    for post in blog.posts:
        print_post(post)

def print_post(post: Post):
    print(POST_TEMPLATE.format(post.title, post.content))

def ask_create_post():
    blog_name = input("Enter the blog name")
    title = input("Enter your post's title: ")
    content = input("Enter the content of the post: ")
    blogs[blog_name].posts.append(Post(title, content))