from flask import Flask, jsonify, request




app = Flask(__name__)

clientes = [
    {
        'id': 1,
        'Nome': 'Filipe',
        'Sexo': 'Masculino'
    },
    {
        'id': 2,
        'Nome': 'Fabiana',
        'Sexo': 'Feminino '
    },
    {
        'id': 3,
        'Nome': 'Jose',
        'Sexo': 'Masculino'
    },
    {
        'id': 4,
        'Nome': 'Juliana',
        'sexo': 'Feminino'
    },
]

@app.route('/clientes',methods=['GET'])
def mostrar_clientes():
    return jsonify(clientes)


@app.route('/cliente/<int:id>',methods =['GET'])
def obter_carros_por_id(id):
    for carro in clientes:
        if carro.get('id') == id:
            return jsonify(carro)



app.run(port=5000,host='localhost',debug=True)


