class Usuario:

    def __init__(self, login, senha, tipo):
        self.__login = login
        self.__senha = senha
        self.__tipo = tipo

    # Getters e Setters
    def get_login(self):
        return self.__login

    def set_login(self, login):
        self.__login = login

    def get_senha(self):
        return self.__senha

    def set_senha(self, senha):
        self.__senha = senha

    def get_tipo(self):
        return self.__tipo

    def set_tipo(self, tipo):
        self.__tipo = tipo

    # Metódos
    def autenticar(self):
        return "Usuário autenticado."
        
    def logout(self):
        return "Layout realizado."