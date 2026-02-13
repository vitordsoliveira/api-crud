from model.cpf_modal import banco_cpf

class CpfService:
    def todos_usuarios(self):
        return banco_cpf

    def busca_cpfs(self, cpf):
        for user in banco_cpf:
            if user.get("cpf") == cpf:
                return user
        return None

    def criar_cpf(self, data):
        required_fields = ["nome", "email", "senha", "cpf"]
        if not all(field in data for field in required_fields):
            return {"error": "Campos obrigatórios ausentes"}, 400

        if self.busca_cpfs(data["cpf"]):
            return {"error": f"Usuário com CPF {data['cpf']} já existe"}, 409

        banco_cpf.append(data)
        return data, 201

    def deletar_cpf(self, cpf):
        user = self.busca_cpfs(cpf)
        if not user:
            return {"error": "Usuário não encontrado"}, 404

        banco_cpf.remove(user)
        return {"message": "Usuário deletado com sucesso"}, 200