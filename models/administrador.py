from .usuario import Usuario

class Administrador(Usuario):
    def cadastrar_aluno(self): return "Aluno cadastrado."
    def cadastrar_instrutor(self): return "Instrutor cadastrado."
    def gerenciar_planos(self): return "Gerenciando planos."
    def gerenciar_horarios(self): return "Gerenciando horários."
