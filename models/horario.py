class Horario:
    def __init__(self, id_horario, dia_semana, hora_inicio, hora_fim, disponivel=True):
        self.__id_horario = id_horario
        self.__dia_semana = dia_semana
        self.__hora_inicio = hora_inicio
        self.__hora_fim = hora_fim
        self.__disponivel = disponivel

    # Getters
    def get_id_horario(self):
        return self.__id_horario

    def get_dia_semana(self):
        return self.__dia_semana

    def get_hora_inicio(self):
        return self.__hora_inicio

    def get_hora_fim(self):
        return self.__hora_fim

    def get_disponivel(self):
        return self.__disponivel

    # Setters
    def set_dia_semana(self, dia_semana):
        self.__dia_semana = dia_semana

    def set_hora_inicio(self, hora_inicio):
        self.__hora_inicio = hora_inicio

    def set_hora_fim(self, hora_fim):
        self.__hora_fim = hora_fim

    def set_disponivel(self, disponivel):
        self.__disponivel = disponivel

    # Métodos
    def reservar(self):
        if self.__disponivel:
            self.__disponivel = False
        else:
            raise Exception("Horário já está reservado.")

    def liberar(self):
        self.__disponivel = True

    def esta_disponivel(self):
        return self.__disponivel

    def exibir_informacoes(self):
        return {
            "ID": self.__id_horario,
            "Dia": self.__dia_semana,
            "Início": self.__hora_inicio,
            "Fim": self.__hora_fim,
            "Disponível": self.__disponivel
        }

    def __str__(self):
        status = "Disponível" if self.__disponivel else "Ocupado"
        return (
            f"{self.__dia_semana} | "
            f"{self.__hora_inicio} - {self.__hora_fim} | "
            f"{status}"
        )