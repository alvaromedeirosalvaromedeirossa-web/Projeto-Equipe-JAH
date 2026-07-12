class Pessoa:
    def __init__(self, id, nome, email, telefone):
        self.id = id
        self.nome = nome
        self.email = email
        self.telefone = telefone

    def exibir_dados(self):
        return {"id": self.id, "nome": self.nome, "email": self.email, "telefone": self.telefone}
