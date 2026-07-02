from models.pessoa import Pessoa

class Instrutor(Pessoa):
    def __init__(self, nome, email, telefone, cref, especialidade):
        super().__init__(nome, email, telefone)

        self.__cref = cref
        self.__especialidade = especialidade

    # Getters e Setters
    def get_cref(self):
        return self.__cref

    def set_cref(self, cref):
        self.__cref = cref

    def get_especialidade(self):
        return self.__especialidade

    def set_especialidade(self, especialidade):
        self.__especialidade = especialidade

    # Métodos
    def criar_treino(self, aluno):
        return f"Treino criado para o aluno {aluno}."

    def realizar_avalicao(self, aluno):
        return f"Avaliação realizada para o aluno {aluno}."

    def consultar_agenda(self):
        return f"Agenda do instrutor exibida com sucesso."