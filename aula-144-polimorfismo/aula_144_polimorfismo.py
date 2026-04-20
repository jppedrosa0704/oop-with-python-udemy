# Polimorfismo em Python Orientado a Objetos
# Polimorfismo é o princípio que permite que
# classes deridavas de uma mesma superclasse
# tenham métodos iguais (com mesma assinatura)
# mas comportamentos diferentes.
# Assinatura do método = Mesmo nome e quantidade
# de parâmetros (retorno não faz parte da assinatura)
# Opinião + princípios que contam:
# Assinatura do método: nome, parâmetros e retorno iguais
# SO"L"ID
# Princípio da substituição de liskov
# Objetos de uma superclasse devem ser substituíveis
# por objetos de uma subclasse sem quebrar a aplicação.
from abc import ABC, abstractmethod

class Notificacao(ABC):
    def __init__(self, mensagem):
        self.mensagem = mensagem
    
    @abstractmethod
    def enviar(self) -> bool:
        ...

class NotificaçãoEmail(Notificacao):
    def enviar(self) -> bool:
        print(f"E-mail: enviando - {self.mensagem}")
        return True

class NotificaçãoSMS(Notificacao):
    def enviar(self)-> False:
        print(f"SMS: enviando - {self.mensagem}")
        return False
    
def notificar(notificacao: Notificacao):
    notificacao_enviada = notificacao.enviar()

    if notificacao_enviada:
        print('Notificação enviada')

    else:
        print('Notificação não enviada')

notificacao_email = NotificaçãoEmail('Testando email')
notificar(notificacao_email)

notificacao_sms = NotificaçãoSMS('Testando SMS')
notificar(notificacao_sms)

# TEste
# n = NotificaçãoSMS('Testando mensagem')
# n.enviar()

# n = NotificaçãoEmail('Testando email')
# n.enviar()