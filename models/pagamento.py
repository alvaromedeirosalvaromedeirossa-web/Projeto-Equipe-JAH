"""
Classe Pagamento.
"""

from __future__ import annotations

from datetime import datetime


class Pagamento:

    def __init__(
        self,
        id: int | None,
        aluno_id: int,
        plano_id: int,
        valor: float,
        data: str,
        status: str
    ):

        self.id = id
        self.aluno_id = aluno_id
        self.plano_id = plano_id
        self.valor = float(valor)
        self.data = data
        self.status = status

    @property
    def pago(self):

        return self.status.lower() == "pago"

    def pagar(self):

        self.status = "Pago"

    def cancelar(self):

        self.status = "Cancelado"

    def pendente(self):

        self.status = "Pendente"

    def data_formatada(self):

        return datetime.strptime(

            self.data,

            "%Y-%m-%d"

        ).strftime("%d/%m/%Y")

    def to_dict(self):

        return {

            "id": self.id,
            "aluno_id": self.aluno_id,
            "plano_id": self.plano_id,
            "valor": self.valor,
            "data": self.data,
            "status": self.status

        }

    @classmethod
    def from_db(cls, row):

        return cls(

            row["id"],
            row["aluno_id"],
            row["plano_id"],
            row["valor"],
            row["data"],
            row["status"]

        )

    def __repr__(self):

        return (

            f"Pagamento("
            f"id={self.id},"
            f"valor={self.valor})"

        )

    def __str__(self):

        return f"R$ {self.valor:.2f}"