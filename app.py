import pyodbc
from flask import Flask, jsonify, request
from flask_cors import CORS 
from BookRequests import getAllBookRequests
from Clients import getAllClients, deleteOldClients
from books import getAllBooks, getLongestOrders, getLongestOrderSummary
from genres import UpdateGenresInfo, ResetGenresInfo, getAllGenres 

connect_str = "DRIVER={ODBC Driver 17 for SQL Server}; SERVER=localhost; DATABASE=Library; Trusted_Connection=yes;"

conn = pyodbc.connect(connect_str)

app = Flask(__name__)
CORS(app)

@app.route('/Books')
def display_books():
    return jsonify(getAllBooks(conn))

@app.route('/Genres/UpdateGenresInfo')
def updateGenres():
    UpdateGenresInfo(conn)

@app.route('/Genres/ResetGenresInfo')
def resetGenres():
    ResetGenresInfo(conn)

@app.route('/BookRequests/<client_id>')
def display_bookRequests(client_id):
    return jsonify(getAllBookRequests(conn, client_id))

@app.route('/Clients')
def display_Clients():
    return jsonify(getAllClients(conn))

@app.route('/Clients/DeleteOldClients/<days>')
def Execute_deleteOldClients(days):
    deleteOldClients(conn, days)

@app.route('/Genres')
def display_Genres():
    return jsonify(getAllGenres(conn))

@app.route('/getLongestOrders', methods=['GET'])
def get_longest_orders_route():
    # Получаем название книги из параметров запроса
    book_title = request.args.get('book_title')
    if not book_title:
        return jsonify({"error": "Parameter 'book_title' is required"}), 400

    # Получаем данные из функции
    result = getLongestOrders(conn, book_title)

    # Проверяем, если это сообщение об отсутствии данных
    if "message" in result:
        return jsonify(result), 404

    # Если данные найдены
    return jsonify(result), 200

@app.route('/getLongestOrderSummary', methods=['GET'])
def get_longest_orders_summary_route():
    # Получаем название книги из параметров запроса
    book_title = request.args.get('book_title')
    if not book_title:
        return jsonify({"error": "Parameter 'book_title' is required"}), 400

    # Получаем данные из функции
    result = getLongestOrderSummary(conn, book_title)

    # Проверяем, если это сообщение об отсутствии данных
    if "message" in result:
        return jsonify(result), 404

    # Если данные найдены
    return jsonify(result), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True) 
