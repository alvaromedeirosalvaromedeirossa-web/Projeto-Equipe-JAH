"""
Classe Aluno.

Representa um aluno da academia.
"""

from __future__ import annotations

from models.pessoa import Pessoa
from models.exceptions import (
    MatriculaInvalidaError,
    PesoInvalidoError,
    AlturaInvalidaError
)


class Aluno(Pessoa):
    """
    Classe responsável por representar um aluno.
    """

    def __init__(
        self,
        id: int | None,
        nome: str,
        email: str,
        telefone: str,
        matricula: str,
        peso: float,
        altura: float
    ) -> None:

        super().__init__(
            id,
            nome,
            email,
            telefone
        )

        self.matricula = matricula
        self.peso = peso
        self.altura = altura

    # ==========================================
    # MATRÍCULA
    # ==========================================

    @property
    def matricula(self) -> str:
        return self._matricula

    @matricula.setter
    def matricula(self, valor: str) -> None:

        valor = str(valor).strip()

        if len(valor) < 3:
            raise MatriculaInvalidaError(
                "Matrícula inválida."
            )

        self._matricula = valor

    # ==========================================
    # PESO
    # ==========================================

    @property
    def peso(self) -> float:
        return self._peso

    @peso.setter
    def peso(self, valor: float) -> None:

        valor = float(valor)

        if valor <= 0:
            raise PesoInvalidoError(
                "Peso inválido."
            )

        self._peso = valor

    # ==========================================
    # ALTURA
    # ==========================================

    @property
    def altura(self) -> float:
        return self._altura

    @altura.setter
    def altura(self, valor: float) -> None:

        valor = float(valor)

        if valor <= 0:
            raise AlturaInvalidaError(
                "Altura inválida."
            )

        self._altura = valor

    # ==========================================
    # IMC
    # ==========================================

    @property
    def imc(self) -> float:

        return round(
            self.peso / (self.altura ** 2),
            2
        )

    @property
    def classificacao_imc(self) -> str:

        if self.imc < 18.5:
            return "Abaixo do peso"

        if self.imc < 25:
            return "Peso normal"

        if self.imc < 30:
            return "Sobrepeso"

        if self.imc < 35:
            return "Obesidade Grau I"

        if self.imc < 40:
            return "Obesidade Grau II"

        return "Obesidade Grau III"

    # ==========================================
    # MÉTODOS
    # ==========================================

    def atualizar_dados(
        self,
        nome: str,
        email: str,
        telefone: str,
        peso: float,
        altura: float
    ) -> None:

        super().atualizar(
            nome,
            email,
            telefone
        )

        self.peso = peso
        self.altura = altura

    def to_dict(self) -> dict:

        dados = super().to_dict()

        dados.update({

            "matricula": self.matricula,
            "peso": self.peso,
            "altura": self.altura,
            "imc": self.imc

        })

        return dados

    @classmethod
    def from_db(cls, row):

        return cls(

            row["id"],
            row["nome"],
            row["email"],
            row["telefone"],
            row["matricula"],
            row["peso"],
            row["altura"]

        )

    def __repr__(self):

        return (
            f"Aluno("
            f"id={self.id}, "
            f"nome='{self.nome}', "
            f"matricula='{self.matricula}')"
        )

    def __str__(self):

        return (
            f"{self.nome} "
            f"({self.matricula})"
        )