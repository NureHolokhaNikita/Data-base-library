import logging
import pyodbc
import json
from datetime import date



logging.basicConfig(level=logging.INFO)
pyodbc.pooling = False
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

def getLongestOrders(conn, book_title):
    query = "SELECT * FROM dbo.GetLongest(?)"
    book_title = book_title.strip('"')
    # Выполнение запроса с параметром
    cursor = conn.cursor()
    cursor.execute(query, (book_title,))
    records = cursor.fetchall()
    
    if not records:
        return {
            "message": f"Відсутні незадоволені запити для книги «{book_title}»"
        }
    
    longest_orders = []
    for r in records:
        order = {
            "client_name": r[0],
            "book_title": r[1],
            "request_date": r[2],
            "request_duration": r[3],
        }
        longest_orders.append(order)
    
    return longest_orders




def getLongestOrderSummary(conn, book_title):
    # SQL для вызова скалярной функции
    query = "SELECT dbo.GetLongest2(?)"
    book_title = book_title.strip('"')
    # Выполнение запроса
    cursor = conn.cursor()
    cursor.execute(query, (book_title,))
    result = cursor.fetchone()
    
    # Обработка результата
    if result and result[0]:
        return result[0]
    else:
        return f"Відсутні незадоволені запити для книги «{book_title}»"
