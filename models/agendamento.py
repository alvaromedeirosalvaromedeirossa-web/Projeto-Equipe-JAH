"""
Classe Agendamento.
"""


class Agendamento:

    STATUS = (

        "Agendado",
        "Confirmado",
        "Cancelado",
        "Concluído"

    )

    def __init__(
        self,
        id,
        aluno_id,
        instrutor_id,
        horario_id,
        status="Agendado"
    ):

        self.id = id
        self.aluno_id = aluno_id
        self.instrutor_id = instrutor_id
        self.horario_id = horario_id

        if status not in self.STATUS:

            raise ValueError(
                "Status inválido."
            )

        self.status = status

    def confirmar(self):

        self.status = "Confirmado"

    def cancelar(self):

        self.status = "Cancelado"

    def concluir(self):

        self.status = "Concluído"

    def to_dict(self):

        return {

            "id": self.id,
            "aluno_id": self.aluno_id,
            "instrutor_id": self.instrutor_id,
            "horario_id": self.horario_id,
            "status": self.status

        }

    @classmethod
    def from_db(cls, row):

        return cls(

            row["id"],
            row["aluno_id"],
            row["instrutor_id"],
            row["horario_id"],
            row["status"]

        )

    def __repr__(self):

        return (

            f"Agendamento("
            f"id={self.id}, "
            f"status='{self.status}')"

        )

    def __str__(self):

        return self.status