from datetime import datetime

class AvaliacaoFisica:
    def __init__(self, id_avaliacao, aluno, instrutor, peso, altura,
                 percentual_gordura, massa_muscular, observacoes=""):
        self.__id_avaliacao = id_avaliacao
        self.__aluno = aluno
        self.__instrutor = instrutor
        self.__peso = peso
        self.__altura = altura
        self.__percentual_gordura = percentual_gordura
        self.__massa_muscular = massa_muscular
        self.__observacoes = observacoes
        self.__data = datetime.now().strftime("%d/%m/%Y")

    # Getters
    def get_id_avaliacao(self):
        return self.__id_avaliacao

    def get_aluno(self):
        return self.__aluno

    def get_instrutor(self):
        return self.__instrutor

    def get_peso(self):
        return self.__peso

    def get_altura(self):
        return self.__altura

    def get_percentual_gordura(self):
        return self.__percentual_gordura

    def get_massa_muscular(self):
        return self.__massa_muscular

    def get_observacoes(self):
        return self.__observacoes

    def get_data(self):
        return self.__data

    # Setters
    def set_peso(self, peso):
        if peso > 0:
            self.__peso = peso
        else:
            raise ValueError("Peso inválido.")

    def set_altura(self, altura):
        if altura > 0:
            self.__altura = altura
        else:
            raise ValueError("Altura inválida.")

    def set_percentual_gordura(self, percentual):
        self.__percentual_gordura = percentual

    def set_massa_muscular(self, massa):
        self.__massa_muscular = massa

    def set_observacoes(self, observacoes):
        self.__observacoes = observacoes

    # Métodos
    def calcular_imc(self):
        return round(self.__peso / (self.__altura ** 2), 2)

    def atualizar_medidas(self, peso, altura):
        self.set_peso(peso)
        self.set_altura(altura)

    def exibir_informacoes(self):
        return {
            "ID": self.__id_avaliacao,
            "Aluno": self.__aluno,
            "Instrutor": self.__instrutor,
            "Peso": self.__peso,
            "Altura": self.__altura,
            "IMC": self.calcular_imc(),
            "Percentual de Gordura": self.__percentual_gordura,
            "Massa Muscular": self.__massa_muscular,
            "Observações": self.__observacoes,
            "Data": self.__data
        }

    def __str__(self):
        return (
            f"Avaliação #{self.__id_avaliacao} | "
            f"Aluno: {self.__aluno} | "
            f"IMC: {self.calcular_imc()}"
        )