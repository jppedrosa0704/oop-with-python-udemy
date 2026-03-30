class Caneta:

    def __init__(self, cor):
        self._cor = cor
        self._cor_tampa = None

    @property
    def cor(self):
        print('property')
        return self._cor

    @cor.setter
    def cor(self, valor):
        print('estou no setter', valor)
        self._cor = valor

    @property
    def cor_tampa(self):
        return self._cor_tampa
    
    @cor_tampa.setter
    def cor_tampa(self, valor):
        print('estou no setter')
        self._cor_tampa = valor

caneta = Caneta('Azul')
caneta.cor = 'rosa'
caneta.cor_tampa = 'marrom'
print(caneta.cor_tampa)
print(caneta.cor) #getter -> obter um valor