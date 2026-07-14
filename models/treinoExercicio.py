"""
Relacionamento entre treino e exercício.
"""

from __future__ import annotations


class TreinoExercicio:

    def __init__(
        self,
        id: int | None,
        treino_id: int,
        exercicio_id: int
    ):

        self.id = id
        self.treino_id = treino_id
        self.exercicio_id = exercicio_id

    def to_dict(self):

        return {

            "id": self.id,
            "treino_id": self.treino_id,
            "exercicio_id": self.exercicio_id

        }

    @classmethod
    def from_db(cls, row):

        return cls(

            row["id"],
            row["treino_id"],
            row["exercicio_id"]

        )

    def __repr__(self):

        return (

            f"TreinoExercicio("
            f"{self.treino_id},"
            f"{self.exercicio_id})"

        )

    def __str__(self):

        return (

            f"Treino {self.treino_id} "
            f"→ Exercício {self.exercicio_id}"

        )