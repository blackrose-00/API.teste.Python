from flask import Flask, jsonify, request

app = Flask(__name__)

discos = [
    {
        "id": 1, 
        "título": "Mais do Mesmo", 
        "autor": "Legião Urbana", 
        "ano": 1998
    },
    {
        "id": 2, 
        "título": "Acústico MTV", 
        "autor": "Cássia Eller", 
        "ano": 2001
    },
    {
        "id": 3, 
        "título": "Nevermind", 
        "autor": "Nirvana", 
        "ano": 1991
    },
]


@app.route("/discos", methods=["GET"])
def obter_discos():
    return jsonify(discos)


@app.route("/discos/<int:id>", methods={"GET"})
def obter_disco_por_id(id):
    for disco in discos:
        if disco.get("id") == id:
            return jsonify(disco)



@app.route("/discos/<int:id>", methods=["PUT"])
def editar_disco_por_id(id):
    disco_alterado = request.get_json()
    for indice, disco in enumerate(discos):
        if disco.get("id") == id:
            discos[indice].update(disco_alterado)
            return jsonify(discos[indice])



@app.route("/discos", methods=["POST"])
def incluir_novo_disco():
    novo_disco = request.get_json()
    discos.append(novo_disco)

    return jsonify(discos)



@app.route("/discos/<int:id>", methods=["DELETE"])
def excluir_disco(id):
    for indice, disco in enumerate(discos):
        if disco.get("id") == id:
            del discos[indice]

        return jsonify(discos)


app.run(port=5000, host="localhost", debug=True)
