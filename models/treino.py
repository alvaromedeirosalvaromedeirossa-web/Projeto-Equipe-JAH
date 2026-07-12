class Treino:
    def __init__(self, id, nome, descricao, aluno_id, instrutor_id):
        self.id=id; self.nome=nome; self.descricao=descricao; self.aluno_id=aluno_id; self.instrutor_id=instrutor_id
        self.exercicios=[]
    def adicionar_exercicio(self, exercicio): self.exercicios.append(exercicio)
    def remover_exercicio(self, exercicio):
        if exercicio in self.exercicios: self.exercicios.remove(exercicio)
    def listar_exercicios(self): return self.exercicios
