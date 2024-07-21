class Arvore:
    def __init__(self):
        self.root = None

    def inserir(self, valor):
        if(self.root==None):
            self.root = No(valor)
        else:
            acno = self.root
            self.inserirrec(acno, valor)

    def inserirrec(self, no, valor):
        if(no.esq==None):
            no.esq = No(valor)
        elif(no.dir==None):
            no.dir = No(valor)
        else:
            self.inserirrec(no.esq, valor)            
            pass
    
    def imprimir(self, no):
        if no:
            print(no.valor)
            self.imprimir(no.esq)
            self.imprimir(no.dir)
            