
class ContaCorrente:

    def __init__(self, saldo):
        self.saldo = saldo
        self.titular = None
        self.email = None
        self.id_doc = 1020

    def inserir_titular(self, nome):
        self.titular = nome
        return nome

    def depositar_saldo(self, value, validation_code):
        if validation_code == self.id_doc:
            self.saldo += value
            print("saldo atual: {}".format(self.saldo))
            return "Deposito Concluido"
        else:
            return "Incorrect Code"

conta1 = ContaCorrente(100)
conta1.inserir_titular("renato")
print(conta1.titular)

print(conta1.depositar_saldo(100, 1020))
