class AvaliacaoFisica:
    def __init__(self, id, aluno_id, instrutor_id, peso, altura, imc, percentual_gordura, observacoes):
        self.id=id; self.aluno_id=aluno_id; self.instrutor_id=instrutor_id; self.peso=peso; self.altura=altura; self.imc=imc; self.percentual_gordura=percentual_gordura; self.observacoes=observacoes
    def calcular_imc(self):
        if self.altura and float(self.altura) > 0: self.imc = float(self.peso)/(float(self.altura)**2)
        return self.imc
