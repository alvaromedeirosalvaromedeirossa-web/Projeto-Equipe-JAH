"""
Classe Administrador.

Representa o administrador do sistema.
"""

from models.usuario import Usuario


class Administrador(Usuario):

    def __init__(self, id, usuario, senha):
        super().__init__(id, usuario, senha)

    def __repr__(self):
        return (
            f"Administrador("
            f"id={self.id}, "
            f"usuario='{self.usuario}')"
        )

    def __str__(self):
        return f"Administrador: {self.usuario}"