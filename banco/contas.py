from abc import ABC, abstractclassmethod

class Conta(ABC):
    def __init__(self, agencia, conta, saldo):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        self.mostrar()

    def mostrar(self):
        print(f'agencia: {self.agencia} \n conta: {self.conta} \n saldo: {self.saldo}' )

    @abstractclassmethod
    def sacar(self, valor): pass




class ContaPoupanca(Conta):
    def sacar(self, valor):
        if(self.saldo < valor):
            print('saldo insuficiente')
            return
        self.saldo -= valor
        self.mostrar()

class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo, limite):
        super().__init__(agencia, conta, saldo)
        self.limite = limite

    def sacar(self, valor):
        if (self.saldo + self.limite) < valor:
            print('saldo insuficiente')
            return
        self.saldo -= valor
        self.mostrar()
