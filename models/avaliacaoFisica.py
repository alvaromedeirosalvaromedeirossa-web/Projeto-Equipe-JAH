"""
Classe AvaliacaoFisica.
"""

from __future__ import annotations


class AvaliacaoFisica:

    def __init__(
        self,
        id: int | None,
        aluno_id: int,
        instrutor_id: int,
        peso: float,
        altura: float,
        percentual_gordura: float,
        observacoes: str = ""
    ):

        self.id = id
        self.aluno_id = aluno_id
        self.instrutor_id = instrutor_id
        self.peso = float(peso)
        self.altura = float(altura)
        self.percentual_gordura = float(percentual_gordura)
        self.observacoes = observacoes

    @property
    def imc(self):

        return round(
            self.peso / (self.altura ** 2),
            2
        )

    @property
    def classificacao(self):

        if self.imc < 18.5:
            return "Abaixo do peso"

        elif self.imc < 25:
            return "Peso Normal"

        elif self.imc < 30:
            return "Sobrepeso"

        elif self.imc < 35:
            return "Obesidade I"

        elif self.imc < 40:
            return "Obesidade II"

        return "Obesidade III"

    def atualizar_medidas(
        self,
        peso,
        altura,
        gordura
    ):

        self.peso = float(peso)
        self.altura = float(altura)
        self.percentual_gordura = float(gordura)

    def to_dict(self):

        return {

            "id": self.id,
            "aluno_id": self.aluno_id,
            "instrutor_id": self.instrutor_id,
            "peso": self.peso,
            "altura": self.altura,
            "percentual_gordura": self.percentual_gordura,
            "observacoes": self.observacoes

        }

    @classmethod
    def from_db(cls, row):

        return cls(

            row["id"],
            row["aluno_id"],
            row["instrutor_id"],
            row["peso"],
            row["altura"],
            row["percentual_gordura"],
            row["observacoes"]

        )

    def __repr__(self):

        return f"AvaliacaoFisica(id={self.id})"

    def __str__(self):

        return f"IMC {self.imc}"