"""
exceptions.py

Exceções personalizadas utilizadas em todo o sistema da Academia.

Autor:
Projeto POO - Academia
"""


class AcademiaError(Exception):
    """
    Classe base para todas as exceções do sistema.
    """
    pass


# ==========================
# PESSOA
# ==========================

class PessoaError(AcademiaError):
    pass


class NomeInvalidoError(PessoaError):
    pass


class EmailInvalidoError(PessoaError):
    pass


class TelefoneInvalidoError(PessoaError):
    pass


# ==========================
# ALUNO
# ==========================

class AlunoError(AcademiaError):
    pass


class MatriculaInvalidaError(AlunoError):
    pass


class PesoInvalidoError(AlunoError):
    pass


class AlturaInvalidaError(AlunoError):
    pass


# ==========================
# INSTRUTOR
# ==========================

class InstrutorError(AcademiaError):
    pass


class CREFInvalidoError(InstrutorError):
    pass


# ==========================
# PLANO
# ==========================

class PlanoError(AcademiaError):
    pass


class ValorPlanoError(PlanoError):
    pass


# ==========================
# EXERCÍCIO
# ==========================

class ExercicioError(AcademiaError):
    pass


# ==========================
# TREINO
# ==========================

class TreinoError(AcademiaError):
    pass


# ==========================
# PAGAMENTO
# ==========================

class PagamentoError(AcademiaError):
    pass


# ==========================
# DOCUMENTO
# ==========================

class DocumentoError(AcademiaError):
    pass


# ==========================
# HORÁRIO
# ==========================

class HorarioError(AcademiaError):
    pass


# ==========================
# AGENDAMENTO
# ==========================

class AgendamentoError(AcademiaError):
    pass