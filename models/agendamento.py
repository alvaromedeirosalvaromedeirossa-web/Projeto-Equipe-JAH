class Agendamento:
    def __init__(self, id, aluno_id, instrutor_id, horario_id, status):
        self.id=id; self.aluno_id=aluno_id; self.instrutor_id=instrutor_id; self.horario_id=horario_id; self.status=status
    def confirmar(self): self.status="Confirmado"
    def cancelar(self): self.status="Cancelado"
