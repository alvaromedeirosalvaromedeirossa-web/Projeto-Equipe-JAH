"""
Classe Horario.
"""


class Horario:

    def __init__(
        self,
        id,
        data,
        hora,
        disponivel=True
    ):

        self.id = id
        self.data = data
        self.hora = hora
        self.disponivel = disponivel

    def reservar(self):

        self.disponivel = False

    def liberar(self):

        self.disponivel = True

    @property
    def ocupado(self):

        return not self.disponivel

    def to_dict(self):

        return {

            "id": self.id,
            "data": self.data,
            "hora": self.hora,
            "disponivel": self.disponivel

        }

    @classmethod
    def from_db(cls, row):

        return cls(

            row["id"],
            row["data"],
            row["hora"],
            row["disponivel"]

        )

    def __repr__(self):

        return (

            f"Horario("
            f"{self.data} "
            f"{self.hora})"

        )

    def __str__(self):

        return f"{self.data} {self.hora}"