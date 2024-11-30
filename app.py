import pyodbc
from flask import Flask, jsonify
from flask_cors import CORS 
from BookRequests import getAllBookRequests
from Clients import getAllClients, deleteOldClients
from books import getAllBooks
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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True) 
