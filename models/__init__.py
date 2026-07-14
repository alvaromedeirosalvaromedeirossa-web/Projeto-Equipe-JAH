"""
Pacote de modelos do sistema Academia.
"""

from .pessoa import Pessoa
from .usuario import Usuario
from .administrador import Administrador
from .aluno import Aluno
from .instrutor import Instrutor
from .plano import Plano
from .pagamento import Pagamento
from .exercicio import Exercicio
from .treino import Treino
from .treinoExercicio import TreinoExercicio
from .avaliacaoFisica import AvaliacaoFisica
from .documento import Documento
from .horario import Horario
from .agendamento import Agendamento

__all__ = [
    "Pessoa",
    "Usuario",
    "Administrador",
    "Aluno",
    "Instrutor",
    "Plano",
    "Pagamento",
    "Exercicio",
    "Treino",
    "TreinoExercicio",
    "AvaliacaoFisica",
    "Documento",
    "Horario",
    "Agendamento",
]