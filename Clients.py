import pyodbc
import json
from datetime import date

class Client:
    def __init__(self, client_id, first_name, last_name, birth_date, registration_date, days_since_request):
        self.client_id = client_id
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.registration_date = registration_date
        self.days_since_request = days_since_request

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
    query = """
SELECT C.*, 
       DATEDIFF(DAY, 
                (SELECT TOP 1 B.request_date 
                 FROM BookRequests AS B 
                 WHERE B.client_id = C.client_id 
                 ORDER BY B.request_date DESC), 
                GETDATE()) AS days_without_request
FROM Clients AS C
JOIN BookRequests AS B ON C.client_id = B.client_id;
"""
    cursor = conn.cursor()
    cursor.execute(query)
    records = cursor.fetchall()
    print(records)
    clients = []
    for r in records:
        client = {
            "client_id": r.client_id,
            "first_name": r.first_name,
            "last_name": r.last_name,
            "birth_date": r.birth_date,
            "registration_date": r.registration_date,
            "days_since_request": r.days_without_request
        }
        clients.append(client)

    return clients

def deleteOldClients(conn, days):
    try:
        days = int(days)
    except ValueError:
        raise ValueError("The days parameter must be a valid integer.")

    query = """EXEC DeleteInactiveClients @days = ?"""
    conn.execute(query, (days,))
