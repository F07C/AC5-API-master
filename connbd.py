from flask import Flask, jsonify
import json
import requests
import mysql.connector

app = Flask(__name__)


mydb = mysql.connector.connect(host="localhost",user="root",password="password",database="clientes")

@app.route('/v1/cliente', methods=["GET"])
def listar():
    selectAllSql = f"select * from id_clientes"
    cursor = mydb.cursor()
    cursor.execute(selectAllSql)
    resultado = cursor.fetchall()
    if resultado is None:
        api_url = "http://localhost:5000/clientes"
        response = requests.get(api_url)
        retornaApi = response.json()
    else:
        retornaApi = None

    return jsonify(retornaApi)

if __name__ == '__main__':
    app.run(port=5001)
    
 
















