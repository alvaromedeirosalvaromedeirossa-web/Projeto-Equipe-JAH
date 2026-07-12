class Plano:
    def __init__(self, id, nome, valor, duracao):
        self.id=id; self.nome=nome; self.valor=valor; self.duracao=duracao
    def alterar_valor(self, novo_valor): self.valor=novo_valor
