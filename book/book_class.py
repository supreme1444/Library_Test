# book.py

class Book:
    def __init__(self, id_book: str, title: str, author: str, year: int, status: str):
        self.id_book = id_book
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def dict(self):
        return {
            "id_book": self.id_book,
            "author": self.author,
            "title": self.title,
            "year": self.year,
            "status": self.status,
        }