"""
Classe Instrutor.

Representa um instrutor da academia.
"""

from __future__ import annotations

from models.pessoa import Pessoa
from models.exceptions import CREFInvalidoError


class Instrutor(Pessoa):
    """
    Classe responsável por representar um instrutor.
    """

    def __init__(
        self,
        id: int | None,
        nome: str,
        email: str,
        telefone: str,
        cref: str,
        especialidade: str,
        experiencia: int = 0
    ) -> None:

        super().__init__(
            id,
            nome,
            email,
            telefone
        )

        self.cref = cref
        self.especialidade = especialidade
        self.experiencia = experiencia

    # ==========================================
    # CREF
    # ==========================================

    @property
    def cref(self) -> str:
        return self._cref

    @cref.setter
    def cref(self, valor: str) -> None:

        valor = str(valor).strip().upper()

        if len(valor) < 4:
            raise CREFInvalidoError(
                "CREF inválido."
            )

        self._cref = valor

    # ==========================================
    # ESPECIALIDADE
    # ==========================================

    @property
    def especialidade(self) -> str:
        return self._especialidade

    @especialidade.setter
    def especialidade(self, valor: str) -> None:

        valor = valor.strip()

        if not valor:
            raise ValueError(
                "Especialidade obrigatória."
            )

        self._especialidade = valor.title()

    # ==========================================
    # EXPERIÊNCIA
    # ==========================================

    @property
    def experiencia(self) -> int:
        return self._experiencia

    @experiencia.setter
    def experiencia(self, valor: int) -> None:

        valor = int(valor)

        if valor < 0:
            raise ValueError(
                "Experiência inválida."
            )

        self._experiencia = valor

    # ==========================================
    # MÉTODOS
    # ==========================================

    def aumentar_experiencia(self, anos: int = 1):

        self.experiencia += anos

    def alterar_especialidade(self, especialidade: str):

        self.especialidade = especialidade

    def atribuir_treino(self, treino):

        return f"{self.nome} assumiu o treino '{treino}'."

    def to_dict(self):

        dados = super().to_dict()

        dados.update({

            "cref": self.cref,
            "especialidade": self.especialidade,
            "experiencia": self.experiencia

        })

        return dados

    @classmethod
    def from_db(cls, row):

        return cls(

            row["id"],
            row["nome"],
            row["email"],
            row["telefone"],
            row["cref"],
            row["especialidade"],
            row["experiencia"]

        )

    def __repr__(self):

        return (
            f"Instrutor("
            f"id={self.id}, "
            f"nome='{self.nome}')"
        )

    def __str__(self):

        return (
            f"{self.nome} "
            f"({self.especialidade})"
        )