from datetime import datetime

class Pagamento:
    def __init__(self, id_pagamento, aluno, plano, valor, data=None, status="Pendente"):
        self.__id_pagamento = id_pagamento
        self.__aluno = aluno
        self.__plano = plano
        self.__valor = valor
        self.__data = data if data else datetime.now().strftime("%d/%m/%Y")
        self.__status = status

    # Getters
    def get_id_pagamento(self):
        return self.__id_pagamento

    def get_aluno(self):
        return self.__aluno

    def get_plano(self):
        return self.__plano

    def get_valor(self):
        return self.__valor

    def get_data(self):
        return self.__data

    def get_status(self):
        return self.__status

    # Setters
    def set_aluno(self, aluno):
        self.__aluno = aluno

    def set_plano(self, plano):
        self.__plano = plano

    def set_valor(self, valor):
        if valor >= 0:
            self.__valor = valor
        else:
            raise ValueError("O valor deve ser maior ou igual a zero.")

    def set_status(self, status):
        self.__status = status

    # Métodos
    def confirmar_pagamento(self):
        self.__status = "Pago"

    def cancelar_pagamento(self):
        self.__status = "Cancelado"

    def esta_pago(self):
        return self.__status == "Pago"

    def exibir_informacoes(self):
        return {
            "ID": self.__id_pagamento,
            "Aluno": self.__aluno,
            "Plano": self.__plano,
            "Valor": self.__valor,
            "Data": self.__data,
            "Status": self.__status
        }

    def __str__(self):
        return (
            f"Pagamento #{self.__id_pagamento} | "
            f"Aluno: {self.__aluno} | "
            f"Valor: R$ {self.__valor:.2f} | "
            f"Status: {self.__status}"
        )