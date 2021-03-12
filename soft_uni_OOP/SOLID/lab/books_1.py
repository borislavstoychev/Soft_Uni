class Book:

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __repr__(self):
        return f"Author: {self.author}, Tittle: {self.title}, Pages: {self.pages} "


class Library:

    def __init__(self):
        self.books = []

    def find_book(self, title):
        searching_book = [book for book in self.books if book.title == title]
        if searching_book:
            return searching_book[0]
        return "Not available"

    def add_book(self, book: Book):
        self.books.append(book)



b = Book("criminal", "Bobby", 999)
l = Library()
l.add_book(b)
print(l.find_book("criminal"))





