class Pagamento:
    def __init__(self, id, aluno_id, plano_id, valor, data, status):
        self.id=id; self.aluno_id=aluno_id; self.plano_id=plano_id; self.valor=valor; self.data=data; self.status=status
    def confirmar_pagamento(self): self.status="Pago"
    def cancelar_pagamento(self): self.status="Cancelado"
    def esta_pago(self): return self.status == "Pago"
