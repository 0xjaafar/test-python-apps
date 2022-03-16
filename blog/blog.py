from typing import List


from typing import List


class Blog:
    
    def __init__(self, title: str, author: str) -> None:
        self.title = title
        self.author = author
        self.posts: List = []
