import json
CAMINHO_ARQUIVO = "aula127.json"

class pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

p1 = pessoa('João', 39)
p2 = pessoa('Ana', 33)
p3 = pessoa('Joana', 15)
bd = [vars(p1), p2.__dict__, vars(p3)]

with open(CAMINHO_ARQUIVO, 'w', encoding='utf-8') as arquivo:
    json.dump(bd, arquivo, ensure_ascii=False, indent=2)
    
