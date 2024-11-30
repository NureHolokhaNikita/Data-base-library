import pyodbc
import json
from datetime import date

class Client:
    def __init__(self, client_id, first_name, last_name, birth_date, registration_date):
        self.client_id = client_id
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.registration_date = registration_date

    def to_dict(self):
        """Метод для преобразования объекта Client в словарь."""
        return {
            'client_id': self.client_id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'birth_date': self.birth_date.strftime('%Y-%m-%d') if isinstance(self.birth_date, date) else str(self.birth_date),
            'registration_date': self.registration_date.strftime('%Y-%m-%d') if isinstance(self.registration_date, date) else str(self.registration_date),
        }


def getAllClients(conn):
    query = """SELECT * FROM Clients"""
    cursor = conn.cursor()
    cursor.execute(query)
    records = cursor.fetchall()

    clients = []
    for r in records:
        client = {
            "client_id": r.client_id,
            "first_name": r.first_name,
            "last_name": r.last_name,
            "birth_date": r.birth_date,
            "registration_date": r.registration_date
        }
        clients.append(client)

    return clients  # Убедитесь, что возвращается список клиентов


# Пример вызова функции:
# conn = pyodbc.connect('ваш строка подключения')
# print(getAllClients(conn))
