from .pessoa import Pessoa

class Aluno(Pessoa):
    def __init__(self, id, nome, email, telefone, matricula, peso, altura):
        super().__init__(id, nome, email, telefone)
        self.matricula = matricula
        self.peso = peso
        self.altura = altura

    def matricular(self): return f"Aluno {self.nome} matriculado com sucesso."
    def visualizar_treino(self): return f"Visualizando treino de {self.nome}."
    def solicitar_avaliacao(self): return f"Avaliação solicitada por {self.nome}."
