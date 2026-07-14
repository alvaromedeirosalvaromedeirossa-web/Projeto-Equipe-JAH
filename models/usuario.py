"""
Classe Usuario.

Responsável pela autenticação do sistema.
"""

from __future__ import annotations

import hashlib


class Usuario:
    """
    Representa um usuário que pode acessar o sistema.
    """

    def __init__(
        self,
        id: int | None,
        usuario: str,
        senha: str
    ) -> None:

        self._id = id
        self.usuario = usuario
        self._senha = self._criptografar(senha)

    # ==========================================
    # ID
    # ==========================================

    @property
    def id(self) -> int | None:
        return self._id

    @id.setter
    def id(self, valor: int | None):
        self._id = valor

    # ==========================================
    # USUÁRIO
    # ==========================================

    @property
    def usuario(self) -> str:
        return self._usuario

    @usuario.setter
    def usuario(self, valor: str):

        valor = valor.strip()

        if len(valor) < 4:
            raise ValueError(
                "Usuário deve possuir pelo menos 4 caracteres."
            )

        self._usuario = valor

    # ==========================================
    # SENHA
    # ==========================================

    @property
    def senha(self):

        return self._senha

    # ==========================================
    # MÉTODOS PRIVADOS
    # ==========================================

    def _criptografar(self, senha: str) -> str:

        return hashlib.sha256(
            senha.encode("utf-8")
        ).hexdigest()

    # ==========================================
    # MÉTODOS
    # ==========================================

    def autenticar(
        self,
        usuario: str,
        senha: str
    ) -> bool:

        return (

            self.usuario == usuario and

            self._senha == self._criptografar(senha)

        )

    def alterar_senha(
        self,
        senha_atual: str,
        nova_senha: str
    ) -> bool:

        if not self.autenticar(
            self.usuario,
            senha_atual
        ):
            return False

        if len(nova_senha) < 6:
            raise ValueError(
                "A nova senha deve possuir pelo menos 6 caracteres."
            )

        self._senha = self._criptografar(
            nova_senha
        )

        return True

    def to_dict(self):

        return {

            "id": self.id,
            "usuario": self.usuario,
            "senha": self.senha

        }

    @classmethod
    def from_db(cls, row):

        obj = cls(

            row["id"],
            row["usuario"],
            "123456"

        )

        obj._senha = row["senha"]

        return obj

    def __repr__(self):

        return (

            f"Usuario("
            f"id={self.id}, "
            f"usuario='{self.usuario}')"

        )

    def __str__(self):

        return self.usuario