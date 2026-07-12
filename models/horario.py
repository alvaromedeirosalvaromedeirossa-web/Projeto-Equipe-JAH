class Horario:
    def __init__(self, id, data, hora, disponivel):
        self.id=id; self.data=data; self.hora=hora; self.disponivel=disponivel
    def reservar(self): self.disponivel=0
    def liberar(self): self.disponivel=1
    def esta_disponivel(self): return bool(int(self.disponivel))
