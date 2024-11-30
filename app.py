import pyodbc
from flask import Flask, jsonify  # Импортируем jsonify для формата JSON
from flask_cors import CORS  # Импортируем CORS для решения проблемы с кросс-доменными запросами
from BookRequests import getAllBookRequests
from Clients import getAllClients
from books import getAllBooks
from genres import getAllGenres  # Убедитесь, что getAllBooks возвращает данные в формате JSON

# Connection string
connect_str = "DRIVER={ODBC Driver 17 for SQL Server}; SERVER=localhost; DATABASE=Library; Trusted_Connection=yes;"

# Database connection
conn = pyodbc.connect(connect_str)

app = Flask(__name__)
CORS(app)  # Включаем CORS для всего приложения

@app.route('/Books')
def display_books():
    # Получаем данные о книгах и возвращаем их в формате JSON
    return jsonify(getAllBooks(conn))

@app.route('/BookRequests/<client_id>')
def display_bookRequests(client_id):
    # Получаем данные о книгах и возвращаем их в формате JSON
    return jsonify(getAllBookRequests(conn, client_id))

@app.route('/Clients')
def display_Clients():
    # Получаем данные о книгах и возвращаем их в формате JSON
    return jsonify(getAllClients(conn))

@app.route('/Genres')
def display_Genres():
    # Получаем данные о книгах и возвращаем их в формате JSON
    return jsonify(getAllGenres(conn))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)  # Задайте адрес и порт для запуска
