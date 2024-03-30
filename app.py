from flask import Flask, jsonify, route
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World Daya!'

livros = [
    {
        "id": 0,
        "nome" : "Titulo 1",
        "autor" : "Anne"
    },
    {
        "id": 1,
        "nome" : "Titulo 2",
        "autor" : "Sakura"
    },
    {
        "id": 2,
        "nome" : "Titulo 3",
        "autor" : "Solar"
    },
    {
        "id": 3,
        "nome" : "Titulo 4",
        "autor" : "Daya"
    },
]

@app.route('/livros')
def get_livros():
    return jsonify(livros)
