class Pessoa:

    def __init__(self, nome, email, telefone):
        self.__nome = nome
        self.__email = email
        self._telefone = telefone

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email

    def get_telefone(self):
        return self._telefone

    def set_telefone(self, telefone):
        self._telefone = telefone

    def exibir_dados(self):
        return {
            "nome": self.__nome,
            "email": self.__email,
            "telefone": self._telefone
        }