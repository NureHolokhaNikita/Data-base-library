import pyodbc
from flask import Flask, jsonify  # Импортируем jsonify для формата JSON
from flask_cors import CORS  # Импортируем CORS для решения проблемы с кросс-доменными запросами
from books import getAllBooks  # Убедитесь, что getAllBooks возвращает данные в формате JSON

# Connection string
connect_str = "DRIVER={ODBC Driver 17 for SQL Server}; SERVER=localhost; DATABASE=Library; Trusted_Connection=yes;"

# Database connection
conn = pyodbc.connect(connect_str)

app = Flask(__name__)
CORS(app)  # Включаем CORS для всего приложения

@app.route('/books')
def display_books():
    # Получаем данные о книгах и возвращаем их в формате JSON
    return jsonify(getAllBooks(conn))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)  # Задайте адрес и порт для запуска
