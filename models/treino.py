"""
Classe Treino.

Representa um treino criado para um aluno.
"""

from __future__ import annotations

from models.exercicio import Exercicio


class Treino:

    def __init__(
        self,
        id: int | None,
        nome: str,
        descricao: str,
        aluno_id: int,
        instrutor_id: int
    ):

        self._id = id
        self.nome = nome
        self.descricao = descricao
        self.aluno_id = aluno_id
        self.instrutor_id = instrutor_id

        # composição
        self._exercicios: list[Exercicio] = []

    # ==================================
    # ID
    # ==================================

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, valor):
        self._id = valor

    # ==================================
    # Nome
    # ==================================

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):

        valor = valor.strip()

        if len(valor) < 3:
            raise ValueError(
                "Nome do treino inválido."
            )

        self._nome = valor

    # ==================================
    # Descrição
    # ==================================

    @property
    def descricao(self):
        return self._descricao

    @descricao.setter
    def descricao(self, valor):

        self._descricao = valor.strip()

    # ==================================
    # Aluno
    # ==================================

    @property
    def aluno_id(self):
        return self._aluno

    @aluno_id.setter
    def aluno_id(self, valor):

        self._aluno = int(valor)

    # ==================================
    # Instrutor
    # ==================================

    @property
    def instrutor_id(self):
        return self._instrutor

    @instrutor_id.setter
    def instrutor_id(self, valor):

        self._instrutor = int(valor)

    # ==================================
    # Exercícios
    # ==================================

    @property
    def exercicios(self):

        return self._exercicios

    def adicionar_exercicio(
        self,
        exercicio: Exercicio
    ):

        if exercicio not in self._exercicios:

            self._exercicios.append(exercicio)

    def remover_exercicio(
        self,
        exercicio: Exercicio
    ):

        if exercicio in self._exercicios:

            self._exercicios.remove(exercicio)

    def limpar_exercicios(self):

        self._exercicios.clear()

    def quantidade_exercicios(self):

        return len(self._exercicios)

    # ==================================
    # Conversão
    # ==================================

    def to_dict(self):

        return {

            "id": self.id,
            "nome": self.nome,
            "descricao": self.descricao,
            "aluno_id": self.aluno_id,
            "instrutor_id": self.instrutor_id

        }

    @classmethod
    def from_db(cls, row):

        return cls(

            row["id"],
            row["nome"],
            row["descricao"],
            row["aluno_id"],
            row["instrutor_id"]

        )

    def __repr__(self):

        return f"Treino(id={self.id}, nome='{self.nome}')"

    def __str__(self):

        return self.nome