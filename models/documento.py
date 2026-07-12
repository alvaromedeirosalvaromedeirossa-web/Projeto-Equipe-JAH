class Documento:
    def __init__(self, id, aluno_id, tipo, arquivo):
        self.id=id; self.aluno_id=aluno_id; self.tipo=tipo; self.arquivo=arquivo
    def atualizar_arquivo(self, novo_arquivo): self.arquivo=novo_arquivo
