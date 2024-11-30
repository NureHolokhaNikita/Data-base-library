import pyodbc
import json

class Genre:
    def __init__(self, genre_id, name, info):
        self.genre_id = genre_id
        self.name = name
        self.info = info

    def to_dict(self):
        """Метод для преобразования объекта Genre в словарь."""
        return {
            'genre_id': self.genre_id,
            'name': self.name,
            'info': self.info
        }


def getAllGenres(conn):
    query = """SELECT * FROM Genres"""
    cursor = conn.cursor()
    cursor.execute(query)
    records = cursor.fetchall()

    genres = []
    for r in records:
        genre = {
            "genre_id": r.genre_id,
            "name": r.name,
            "info": r.info
        }
        genres.append(genre)

    return genres  # Убедитесь, что возвращается список жанров


# Пример вызова функции:
# conn = pyodbc.connect('ваш строка подключения')
# print(getAllGenres(conn))
