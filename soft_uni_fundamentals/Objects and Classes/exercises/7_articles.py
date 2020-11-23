class Article:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def edit(self, new_content):
        result = self.content = new_content
        return result

    def change_author(self, new_author):
        result = self.author = new_author
        return result

    def rename(self, new_title):
        result = self.title = new_title

    def __repr__(self):
        return f"{self.title} - {self.content}: {self.author}"
