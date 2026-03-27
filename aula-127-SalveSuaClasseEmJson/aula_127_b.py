#importa dados da aula 127_a

from aula_127_a_exercicio_SalveSuaClasseEmJson import CAMINHO_ARQUIVO, pessoa, json

with open(CAMINHO_ARQUIVO, 'r', encoding='utf-8') as arquivo:
    pessoas = json.load(arquivo)
    print(pessoas)
    p1 = pessoa(**pessoas[0])
    p2 = pessoa(**pessoas[1])
    p3 = pessoa(**pessoas[2])

    print(p1.nome, p1.idade)
    print(p2.nome, p2.idade)
    print(p3.nome, p3.idade)

