from models.pessoa import Pessoa

class Aluno(Pessoa):

    def __init__(self, nome, email, telefone, matricula, peso, altura):
        super().__init__(nome, email, telefone)

        self.__matricula = matricula
        self.__peso = peso
        self.__altura = altura

    # Getters e Setters
    def get_matricula(self):
            return self.__matricula

    def set_matricula(self, matricula):
            self.__matricula = matricula

    # Métodos
    def calcular_imc(self):
        return self.__peso / (self.__altura ** 2)

    def matricular(self):
        return f"Aluno{self.get_nome()} matriculado com sucesso."

    def visualizar_treino(self):
        return f"Treionos do aluno {self.get_nome()}."