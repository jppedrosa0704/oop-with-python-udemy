#Metódos em instâncias de classes python.
#Hard coded - é ago que foi escrito diretamente no código

class carro:
    def __init__(self, nome):
        self.nome = nome

    def acelerar(self):
        print(f'{self.nome} está acelerando.')


fusca = carro('Fusca')
print(fusca.nome)
fusca.acelerar()

celta = carro(nome='Celta') #arumento nomeado
print(celta.nome)
celta.acelerar()
