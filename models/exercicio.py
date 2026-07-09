class Exercicio:
    def __init__(self, id_exercicio, nome, grupo_muscular, series, repeticoes, carga):
        self.__id_exercicio = id_exercicio
        self.__nome = nome
        self.__grupo_muscular = grupo_muscular
        self.__series = series
        self.__repeticoes = repeticoes
        self.__carga = carga

    # Getters
    def get_id_exercicio(self):
        return self.__id_exercicio

    def get_nome(self):
        return self.__nome

    def get_grupo_muscular(self):
        return self.__grupo_muscular

    def get_series(self):
        return self.__series

    def get_repeticoes(self):
        return self.__repeticoes

    def get_carga(self):
        return self.__carga

    # Setters
    def set_nome(self, nome):
        self.__nome = nome

    def set_grupo_muscular(self, grupo_muscular):
        self.__grupo_muscular = grupo_muscular

    def set_series(self, series):
        if series > 0:
            self.__series = series
        else:
            raise ValueError("O número de séries deve ser maior que zero.")

    def set_repeticoes(self, repeticoes):
        if repeticoes > 0:
            self.__repeticoes = repeticoes
        else:
            raise ValueError("O número de repetições deve ser maior que zero.")

    def set_carga(self, carga):
        if carga >= 0:
            self.__carga = carga
        else:
            raise ValueError("A carga não pode ser negativa.")

    # Métodos
    def atualizar_carga(self, nova_carga):
        self.set_carga(nova_carga)

    def exibir_informacoes(self):
        return {
            "ID": self.__id_exercicio,
            "Nome": self.__nome,
            "Grupo Muscular": self.__grupo_muscular,
            "Séries": self.__series,
            "Repetições": self.__repeticoes,
            "Carga": self.__carga
        }

    def __str__(self):
        return (
            f"{self.__nome} | "
            f"{self.__series}x{self.__repeticoes} | "
            f"{self.__carga} kg"
        )