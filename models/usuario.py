from .pessoa import Pessoa

class Usuario(Pessoa):
    def __init__(self, id, nome, email, telefone, usuario, senha):
        super().__init__(id, nome, email, telefone)
        self.usuario = usuario
        self.senha = senha
    def autenticar(self, usuario, senha): return self.usuario == usuario and self.senha == senha
    def alterar_senha(self, nova_senha): self.senha = nova_senha
