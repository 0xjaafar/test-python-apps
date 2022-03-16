class Post:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content

    def __repr__(self) -> str:
        return "post's title: {}".format(self.title)

    def json(self):
        return {
            "title": self.title,
            "content": self.content,
        }
