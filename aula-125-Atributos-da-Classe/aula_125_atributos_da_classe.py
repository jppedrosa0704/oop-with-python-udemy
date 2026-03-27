#Atributos de classe

class  pessoa:
    ANO_ATUAL = 2026

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_de_nascimento(self):
        return pessoa.ANO_ATUAL - self.idade
        
p1 = pessoa('João', 40)
p2 = pessoa('Ana', 33)

print(pessoa.ANO_ATUAL)
print(p1.get_ano_de_nascimento())
print(p2.get_ano_de_nascimento())
