from abc import ABC, abstractmethod


class Book:
    def __init__(self, author, content: str):
        self.content = content
        self.author = author


class Formatter(ABC):
    @abstractmethod
    def format(self, book: Book):
        ...


class ContentFormatter(Formatter):
    def format(self, book: Book) -> str:
        return book.content


class AuthorFormatter(Formatter):

    def format(self, book: Book):
        return book.author


class Printer:
    def printer(self, book: Book, formatter: Formatter):
        formatted_book = formatter.format(book)
        return formatted_book


b = Book("Bobby", "Some content")
f = ContentFormatter()
a = AuthorFormatter()

p = Printer()
print(p.printer(b, f))
print(p.printer(b, a))

# class Book:
#     def __init__(self, content: str):
#         self.content = content
#
#
# class Formatter:
#     def format(self, book: Book) -> str:
#         return book.content
#
#
# class Printer:
#     def get_book(self, book: Book):
#         formatter = Formatter()
#         formatted_book = formatter.format(book)
#         return formatted_book