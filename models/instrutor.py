from .pessoa import Pessoa

class Instrutor(Pessoa):
    def __init__(self, id, nome, email, telefone, cref, especialidade):
        super().__init__(id, nome, email, telefone)
        self.cref = cref
        self.especialidade = especialidade

    def criar_treino(self, aluno=None): return "Treino criado." if aluno is None else f"Treino criado para {aluno}."
    def realizar_avaliacao(self, aluno=None): return "Avaliação realizada." if aluno is None else f"Avaliação realizada para {aluno}."
    def consultar_agenda(self): return "Agenda exibida com sucesso."
