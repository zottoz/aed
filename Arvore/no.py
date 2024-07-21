class No:
    def __init__(self, valor):
        self.esq = None
        self.dir = None
        self.valor = valor
    def __str__(self):
        return f"Valor: {self.valor}."