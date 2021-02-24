from user import User


class Library:

    def __init__(self, ):
        self.user_records = []
        self.books_available = {}
        self.rented_books = {}

    def add_user(self, user: User):
