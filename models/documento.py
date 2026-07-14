"""
Classe Documento.
"""


class Documento:

    def __init__(
        self,
        id,
        aluno_id,
        tipo,
        arquivo
    ):

        self.id = id
        self.aluno_id = aluno_id
        self.tipo = tipo
        self.arquivo = arquivo

    @property
    def extensao(self):

        return self.arquivo.split(".")[-1].lower()

    def validar(self):

        return self.extensao in [

            "pdf",
            "png",
            "jpg",
            "jpeg"

        ]

    def nome_arquivo(self):

        return self.arquivo.split("/")[-1]

    def to_dict(self):

        return {

            "id": self.id,
            "aluno_id": self.aluno_id,
            "tipo": self.tipo,
            "arquivo": self.arquivo

        }

    @classmethod
    def from_db(cls, row):

        return cls(

            row["id"],
            row["aluno_id"],
            row["tipo"],
            row["arquivo"]

        )

    def __repr__(self):

        return f"Documento({self.tipo})"

    def __str__(self):

        return self.nome_arquivo()