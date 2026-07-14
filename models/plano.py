"""
Classe Plano.
Representa um plano da academia.
"""

from __future__ import annotations

from models.exceptions import ValorPlanoError


class Plano:

    def __init__(
        self,
        id: int |None,
        nome: str,
        valor: float,
        duracao: int,
        descricao: str = ""
    ):

        self._id = id
        self.nome = nome
        self.valor = valor
        self.duracao = duracao
        self.descricao = descricao

    # ===============================
    # ID
    # ===============================

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, valor):
        self._id = valor

    # ===============================
    # NOME
    # ===============================

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):

        valor = valor.strip()

        if len(valor) < 3:
            raise ValueError("Nome inválido.")

        self._nome = valor

    # ===============================
    # VALOR
    # ===============================

    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, valor):

        valor = float(valor)

        if valor <= 0:
            raise ValorPlanoError(
                "Valor inválido."
            )

        self._valor = valor

    # ===============================
    # DURAÇÃO
    # ===============================

    @property
    def duracao(self):
        return self._duracao

    @duracao.setter
    def duracao(self, valor):

        valor = int(valor)

        if valor <= 0:
            raise ValueError(
                "Duração inválida."
            )

        self._duracao = valor

    # ===============================
    # DESCRIÇÃO
    # ===============================

    @property
    def descricao(self):
        return self._descricao

    @descricao.setter
    def descricao(self, valor):

        self._descricao = valor.strip()

    # ===============================
    # MÉTODOS
    # ===============================

    def alterar_valor(self, novo):

        self.valor = novo

    def valor_mensal(self):

        return round(
            self.valor / self.duracao,
            2
        )

    def to_dict(self):

        return {

            "id": self.id,
            "nome": self.nome,
            "valor": self.valor,
            "duracao": self.duracao,
            "descricao": self.descricao

        }

    @classmethod
    def from_db(cls, row):

        return cls(

            row["id"],
            row["nome"],
            row["valor"],
            row["duracao"],
            row["descricao"]

        )

    def __repr__(self):

        return (
            f"Plano(id={self.id},"
            f" nome='{self.nome}')"
        )

    def __str__(self):

        return self.nome