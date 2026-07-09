from models.pessoa import Pessoa


class Aluno(Pessoa):
    def __init__(self, nome, email, telefone, matricula, peso, altura):
        super().__init__(nome, email, telefone)
        self.__matricula = matricula
        self.__peso = peso
        self.__altura = altura

    # ===== GETTERS =====

    def get_matricula(self):
        return self.__matricula

    def get_peso(self):
        return self.__peso

    def get_altura(self):
        return self.__altura

    # ===== SETTERS =====

    def set_matricula(self, matricula):
        self.__matricula = matricula

    def set_peso(self, peso):
        if peso > 0:
            self.__peso = peso
        else:
            raise ValueError("O peso deve ser maior que zero.")

    def set_altura(self, altura):
        if altura > 0:
            self.__altura = altura
        else:
            raise ValueError("A altura deve ser maior que zero.")

    # ===== MÉTODOS =====

    def matricular(self):
        return f"Aluno {self.get_nome()} matriculado com sucesso."

    def visualizar_treino(self):
        return f"Treinos do aluno {self.get_nome()}."

    def visualizar_pagamentos(self):
        return f"Pagamentos do aluno {self.get_nome()}."

    def calcular_imc(self):
        return round(self.__peso / (self.__altura ** 2), 2)

    def exibir_dados(self):
        dados = super().exibir_dados()
        dados.update({
            "Matrícula": self.__matricula,
            "Peso": self.__peso,
            "Altura": self.__altura,
            "IMC": self.calcular_imc()
        })
        return dados

    def __str__(self):
        return f"Aluno: {self.get_nome()} - Matrícula: {self.__matricula}"