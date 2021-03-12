from abc import ABC, abstractmethod


class Book:

    def __init__(self, title, author, page=0):
        self.title = title
        self.author = author
        self.page = page

    def __repr__(self):
        return f"Author: {self.author}, Tittle: {self.title}"


class Library:

    def __init__(self, location):
        self.location = location
        self.books = []

    def find_book(self, title):
        searching_book = [book for book in self.books if book.title == title]
        if searching_book:
            return searching_book[0]
        return "Not available"

    def add_book(self, book: Book):
        self.books.append(book)


class Reader(ABC):

    def __init__(self, name, surname, book: Book):
        self.name = name
        self.surname = surname
        self.book = book

    @abstractmethod
    def __repr__(self):
        ...


class Reading(Reader):

    def turn_page(self, page):
        self.book.page = page

    def __repr__(self):
        return f"{self.name} {self.surname} reading page {self.book.page} '{self.book}'"



b = Book("criminal", "Bobby")
l = Library("Petrich")
l.add_book(b)
r = Reading("Borkata", "Stoychev", l.find_book("criminal"))
r.turn_page(254)
print(r)


