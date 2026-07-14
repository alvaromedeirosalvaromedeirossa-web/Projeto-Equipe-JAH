"""
Classe Exercicio.
"""

from __future__ import annotations


class Exercicio:

    def __init__(
        self,
        id: int | None,
        nome: str,
        grupo_muscular: str,
        series: int,
        repeticoes: int
    ):

        self._id = id
        self.nome = nome
        self.grupo_muscular = grupo_muscular
        self.series = series
        self.repeticoes = repeticoes

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, valor):
        self._id = valor

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):

        if len(valor.strip()) < 2:
            raise ValueError(
                "Nome inválido."
            )

        self._nome = valor.strip()

    @property
    def grupo_muscular(self):
        return self._grupo

    @grupo_muscular.setter
    def grupo_muscular(self, valor):

        self._grupo = valor.strip()

    @property
    def series(self):
        return self._series

    @series.setter
    def series(self, valor):

        valor = int(valor)

        if valor <= 0:
            raise ValueError()

        self._series = valor

    @property
    def repeticoes(self):
        return self._repeticoes

    @repeticoes.setter
    def repeticoes(self, valor):

        valor = int(valor)

        if valor <= 0:
            raise ValueError()

        self._repeticoes = valor

    def descricao(self):

        return (
            f"{self.nome} "
            f"{self.series}x{self.repeticoes}"
        )

    def to_dict(self):

        return {

            "id": self.id,
            "nome": self.nome,
            "grupo_muscular": self.grupo_muscular,
            "series": self.series,
            "repeticoes": self.repeticoes

        }

    @classmethod
    def from_db(cls, row):

        return cls(

            row["id"],
            row["nome"],
            row["grupo_muscular"],
            row["series"],
            row["repeticoes"]

        )

    def __repr__(self):

        return (
            f"Exercicio("
            f"{self.nome})"
        )

    def __str__(self):

        return self.nome