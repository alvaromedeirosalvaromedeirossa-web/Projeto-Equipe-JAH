class Exercicio:
    def __init__(self, id, nome, grupo_muscular, series, repeticoes):
        self.id=id; self.nome=nome; self.grupo_muscular=grupo_muscular; self.series=series; self.repeticoes=repeticoes
    def exibir_informacoes(self): return self.__dict__.copy()
