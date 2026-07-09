from models.horario import Horario

class Agendamento:
    def __init__(self, id_agendamento, aluno, instrutor, horario, status="Agendado"):
        self.__id_agendamento = id_agendamento
        self.__aluno = aluno
        self.__instrutor = instrutor

        if isinstance(horario, Horario):
            self.__horario = horario
        else:
            raise TypeError("O horário deve ser um objeto da classe Horario.")

        self.__status = status

    # Getters
    def get_id_agendamento(self):
        return self.__id_agendamento

    def get_aluno(self):
        return self.__aluno

    def get_instrutor(self):
        return self.__instrutor

    def get_horario(self):
        return self.__horario

    def get_status(self):
        return self.__status

    # Setters
    def set_aluno(self, aluno):
        self.__aluno = aluno

    def set_instrutor(self, instrutor):
        self.__instrutor = instrutor

    def set_horario(self, horario):
        if isinstance(horario, Horario):
            self.__horario = horario
        else:
            raise TypeError("O horário deve ser um objeto da classe Horario.")

    def set_status(self, status):
        self.__status = status

    # Métodos
    def confirmar(self):
        self.__status = "Confirmado"
        self.__horario.reservar()

    def cancelar(self):
        self.__status = "Cancelado"
        self.__horario.liberar()

    def concluir(self):
        self.__status = "Concluído"

    def exibir_informacoes(self):
        return {
            "ID": self.__id_agendamento,
            "Aluno": self.__aluno,
            "Instrutor": self.__instrutor,
            "Horário": str(self.__horario),
            "Status": self.__status
        }

    def __str__(self):
        return (
            f"Agendamento {self.__id_agendamento} | "
            f"Aluno: {self.__aluno} | "
            f"Instrutor: {self.__instrutor} | "
            f"Status: {self.__status}"
        )