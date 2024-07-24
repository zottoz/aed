class Lista:
    def __init__(self):
        self.tam = 0
        self.inicio = None
        
    def adiciona(self, dados):
        novoNo = No(dados)
        if(self.inicio == None):
            self.inicio = novoNo
        else:
            novoNo.proximo = self.inicio
            self.inicio = novoNo
        self.tam = self.tam + 1

    def adicionaFim(self, valor):
        if(self.tam == 0):
            self.adiciona(valor)
        else:
            atual = self.inicio
            while(atual.proximo):
                atual = atual.proximo
            atual.proximo = No(valor)
            self.tam = self.tam + 1
        
    def imprimir(self):
        if(self.inicio):
            print(self.inicio.dados)
            self.__imprimir_rec__(self.inicio.proximo)
        else:
            print("Lista Vazia")
            
    def __imprimir_rec__(self, no):
        if(no):
            print(no.dados)
            self.__imprimir_rec__(no.proximo)       

    def tamanho(self):
        return self.tam

    def removeInicio(self):
        if(self.inicio):
            temp = self.inicio
            self.inicio = self.inicio.proximo
            temp = None
            self.tam = self.tam - 1

    def removeFim(self):
        atual = self.inicio
        anterior = None
        if(self.tam == 0):
            print("a lista está vazia")
        elif(self.tam == 1):
            self.inicio = None
        else:
            while(atual.proximo != None):
                anterior = atual
                atual = atual.proximo
            anterior.proximo = None        
        self.tam = self.tam - 1
        
    def removeValor(self, valor):
        if(self.inicio.dados == valor):
            aux = self.inicio
            self.inicio = self.inicio.proximo
            aux.proximo = None
        else:
            anterior = self.inicio
            atual = self.inicio.proximo
            while(atual):
                if(atual.dados == valor):
                    anterior.proximo = atual.proximo
                    pass
            #_avança
            atual = atual.proximo
        