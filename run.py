from flask import Flask, jsonify, request
from service.cpf_service import CpfService

app = Flask(__name__)
user_service = CpfService()

@app.route("/users", methods=["POST"])
def criar_usuario():
    data = request.get_json()
    result, status_code = user_service.criar_cpf(data)
    return jsonify(result), status_code

@app.route("/users/lista", methods=["GET"])
def lista_usuarios():
    users = user_service.todos_usuarios()
    return jsonify(users), 200

@app.route("/users/<string:cpf>", methods=["GET"])
def busca_usuario_cpf(cpf):
    user = user_service.busca_cpfs(cpf)
    if user:
        return jsonify(user), 200
    return jsonify({"error": "Usuário não encontrado"}), 404

@app.route("/users/deletar/<string:cpf>", methods=["DELETE"])
def deleta_usuario_cpf(cpf):
    result, status_code = user_service.deletar_cpf(cpf)
    return jsonify(result), status_code

if __name__ == "__main__":
    app.run()
