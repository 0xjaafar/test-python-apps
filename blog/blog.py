from blog.post import Post
from typing import List


class Blog:
    def __init__(self, title: str, author: str) -> None:
        self.title = title
        self.author = author
        self.posts: List = []

    def __repr__(self) -> str:
        return "{} by {} ({} post{})".format(
            self.title, self.author, len(self.posts), "s" if len(self.posts) > 1 else ""
        )

    def json(self):
        return {
            "title": self.title,
            "author": self.author,
            "posts": [post.json() for post in self.posts],
        }
    
    def create_post(self, title: str, content: str):
        self.posts.append(Post(title, content))

    
