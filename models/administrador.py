from models.usuario import Usuario

class Administrador(Usuario):

    def __init__(self, login, senha):
        super().__init__(login, senha, "Administrador")

    # Métodos
    def cadastrar_instrutor(self):
        return "Instrutor cadastrado com sucesso."

    def remover_instrutor(self):
        return "Instrutor removido com sucesso."

    def cadastrar_aluno(self):
        return "Aluno cadastrado com sucesso."

    def remover_aluno(self):
        return "Aluno removido com sucesso."

    def cadastrar_exercicio(self):
        return "Exercício cadastrado com sucesso."

    def cadastrar_treino(self):
        return "Treino cadastrado com sucesso."

    def gerenciar_sistema(self):
        return "Acesso liberado ao painel administrativo."

    def visualizar_relatorio(self):
        return "Relatórios exibidos com sucesso."