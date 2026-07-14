"""
Classe base Pessoa.

Todas as pessoas do sistema herdam desta classe.
"""

from __future__ import annotations

from models.exceptions import (
    NomeInvalidoError,
    EmailInvalidoError,
    TelefoneInvalidoError
)


class Pessoa:
    """
    Classe base para pessoas da academia.
    """

    def __init__(
        self,
        id: int | None,
        nome: str,
        email: str,
        telefone: str
    ) -> None:

        self._id = id
        self.nome = nome
        self.email = email
        self.telefone = telefone

    # ==========================
    # ID
    # ==========================

    @property
    def id(self) -> int | None:
        return self._id

    @id.setter
    def id(self, valor: int | None) -> None:
        self._id = valor

    # ==========================
    # Nome
    # ==========================

    @property
    def nome(self) -> str:
        return self._nome

    @nome.setter
    def nome(self, valor: str) -> None:

        valor = valor.strip()

        if len(valor) < 3:
            raise NomeInvalidoError(
                "O nome deve possuir pelo menos 3 caracteres."
            )

        self._nome = valor.title()

    # ==========================
    # Email
    # ==========================

    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, valor: str) -> None:

        valor = valor.strip().lower()

        if "@" not in valor or "." not in valor:
            raise EmailInvalidoError(
                "Email inválido."
            )

        self._email = valor

    # ==========================
    # Telefone
    # ==========================

    @property
    def telefone(self) -> str:
        return self._telefone

    @telefone.setter
    def telefone(self, valor: str) -> None:

        telefone = "".join(filter(str.isdigit, valor))

        if len(telefone) not in (10, 11):
            raise TelefoneInvalidoError(
                "Telefone inválido."
            )

        self._telefone = telefone

    # ==========================
    # Métodos
    # ==========================

    def atualizar(
        self,
        nome: str,
        email: str,
        telefone: str
    ) -> None:

        self.nome = nome
        self.email = email
        self.telefone = telefone

    def to_dict(self) -> dict:

        return {
            "id": self.id,
            "nome": self.nome,
            "email": self.email,
            "telefone": self.telefone
        }

    @classmethod
    def from_db(cls, row):

        return cls(
            row["id"],
            row["nome"],
            row["email"],
            row["telefone"]
        )

    def __repr__(self):

        return (
            f"{self.__class__.__name__}"
            f"(id={self.id}, nome='{self.nome}')"
        )

    def __str__(self):

        return self.nome

    def __eq__(self, other):

        if not isinstance(other, Pessoa):
            return False

        return self.id == other.id

    def __hash__(self):

        return hash(self.id)