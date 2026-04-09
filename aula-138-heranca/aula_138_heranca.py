# Herança simples - Relações entre classes
# Associação - usa, Agregação - tem
# Composição - É dono de, Herança - É um
#
# Herança vs Composição
#
# Classe principal (Pessoa)
#   -> super class, base class, parent class
# Classes filhas (Cliente)
#   -> sub class, child class, derived class

class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def falar_nome_class(self):
        print(self.nome, self.sobrenome, self.__class__.__name__)

class Aluno(Pessoa):
    ...

class Cliente(Pessoa):
    ...


a1 = Aluno('João', 'Paulo')
a1.falar_nome_class()
c1 = Cliente('Ana', 'Medeiros')
c1.falar_nome_class()