import pyodbc
import json
from datetime import date

class Book:
    def __init__(self, book_id, title, author, writing_date, name):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.writing_date = writing_date  
        self.name = name  

    def to_dict(self):
        """Метод для перетворення об'єкта Book в словник."""
        return {
            'book_id': self.book_id,
            'title': self.title,
            'author': self.author,
            'writing_date': self.writing_date.strftime('%Y-%m-%d') if isinstance(self.writing_date, date) else str(self.writing_date),
            'genre': self.name
        }


def getAllBooks(conn):
    query = """SELECT Books.*, Genres.name FROM Books JOIN Genres ON Books.genre_id = Genres.genre_Id"""
    cursor = conn.cursor()
    cursor.execute(query)
    records = cursor.fetchall()
    
    books = []
    for r in records:
        book = {
            "book_id": r.book_id,
            "title": r.title,
            "author": r.author,
            "writing_date": r.writing_date,
            "genre": r.name
        }
        books.append(book)

    return books