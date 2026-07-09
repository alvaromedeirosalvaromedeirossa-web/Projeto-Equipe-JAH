from models.exercicio import Exercicio

class Treino:
    def __init__(self, id_treino, aluno, instrutor, objetivo):
        self.__id_treino = id_treino
        self.__aluno = aluno
        self.__instrutor = instrutor
        self.__objetivo = objetivo
        self.__exercicios = []

    # Getters
    def get_id_treino(self):
        return self.__id_treino

    def get_aluno(self):
        return self.__aluno

    def get_instrutor(self):
        return self.__instrutor

    def get_objetivo(self):
        return self.__objetivo

    def get_exercicios(self):
        return self.__exercicios

    # Setters
    def set_aluno(self, aluno):
        self.__aluno = aluno

    def set_instrutor(self, instrutor):
        self.__instrutor = instrutor

    def set_objetivo(self, objetivo):
        self.__objetivo = objetivo

    # Métodos
    def adicionar_exercicio(self, exercicio):
        if isinstance(exercicio, Exercicio):
            self.__exercicios.append(exercicio)
        else:
            raise TypeError("O objeto informado não é um Exercício.")

    def remover_exercicio(self, exercicio):
        if exercicio in self.__exercicios:
            self.__exercicios.remove(exercicio)

    def listar_exercicios(self):
        return self.__exercicios

    def quantidade_exercicios(self):
        return len(self.__exercicios)

    def exibir_informacoes(self):
        return {
            "ID": self.__id_treino,
            "Aluno": self.__aluno,
            "Instrutor": self.__instrutor,
            "Objetivo": self.__objetivo,
            "Quantidade de Exercícios": len(self.__exercicios)
        }

    def __str__(self):
        return (
            f"Treino {self.__id_treino} | "
            f"Aluno: {self.__aluno} | "
            f"Objetivo: {self.__objetivo}"
        )