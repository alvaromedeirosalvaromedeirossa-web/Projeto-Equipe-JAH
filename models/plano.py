class Plano:
    def __init__(self, id_plano, nome, descricao, duracao, valor):
        self.__id_plano = id_plano
        self.__nome = nome
        self.__descricao = descricao
        self.__duracao = duracao
        self.__valor = valor

    # Getters
    def get_id_plano(self):
        return self.__id_plano

    def get_nome(self):
        return self.__nome

    def get_descricao(self):
        return self.__descricao

    def get_duracao(self):
        return self.__duracao

    def get_valor(self):
        return self.__valor

    # Setters
    def set_nome(self, nome):
        self.__nome = nome

    def set_descricao(self, descricao):
        self.__descricao = descricao

    def set_duracao(self, duracao):
        self.__duracao = duracao

    def set_valor(self, valor):
        if valor >= 0:
            self.__valor = valor
        else:
            raise ValueError("O valor do plano deve ser positivo.")

    # Métodos
    def alterar_valor(self, novo_valor):
        self.set_valor(novo_valor)

    def exibir_informacoes(self):
        return {
            "ID": self.__id_plano,
            "Nome": self.__nome,
            "Descrição": self.__descricao,
            "Duração": self.__duracao,
            "Valor": self.__valor
        }

    def __str__(self):
        return f"{self.__nome} - R$ {self.__valor:.2f} ({self.__duracao})"