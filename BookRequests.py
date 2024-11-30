import pyodbc
import json
from datetime import date

class BookRequest:
    def __init__(self, request_id, client_id, book_id, request_date, request_duration, is_satisfied, Book_Title, Name):
        self.request_id = request_id
        self.client_id = client_id
        self.book_id = book_id
        self.request_date = request_date  
        self.request_duration = request_duration  
        self.is_satisfied = is_satisfied  
        self.Book_Title = Book_Title  
        self.Name = Name

    def to_dict(self):
        """Метод для перетворення об'єкта BookRequest в словник."""
        return {
            'Book_Title': self.Book_Title,
            'Name': self.Name,
            'book_id': self.book_id,
            'request_id': self.request_id,
            'client_id': self.client_id,
            'request_duration': self.request_duration,
            'is_satisfied': self.is_satisfied,
            'request_date': self.request_date.strftime('%Y-%m-%d') if isinstance(self.request_date, date) else str(self.request_date),
        }


def getAllBookRequests(conn, client_id):
    query = """
SELECT BR.*, B.title AS Book_Title, C.first_name + ' ' + C.last_name AS Name
FROM BookRequests AS BR
JOIN Clients AS C ON BR.client_id = C.client_id
JOIN Books AS B ON BR.book_id = B.book_id
WHERE BR.client_id = ?
"""
    cursor = conn.cursor()
    cursor.execute(query, (client_id,))
    records = cursor.fetchall()

    bookRequests = []
    for r in records:
        book = {
            "Book_Title": r.Book_Title,
            "Name": r.Name,
            "book_id": r.book_id,
            "request_id": r.request_id,
            "client_id": r.client_id,
            "request_duration": r.request_duration,
            "is_satisfied": r.is_satisfied,
            "request_date": r.request_date
        }
        bookRequests.append(book)

    return bookRequests