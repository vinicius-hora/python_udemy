#classes
from abc import ABC, abstractclassmethod
class Conta(ABC):
    def __init__(self, agencia, conta, saldo):
        self._agencia = agencia
        self._conta = conta
        self._saldo = saldo

    @property
    def agencia(self):
        return self._agencia

    @property
    def conta(self):
        return self._conta

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        if isinstance(valor, (int, float)):
            raise ValueError ("Saldo precisa ser numerico")
        self._saldo = valor

    def depositar(self, valor):
        if isinstance(valor, (int, float)):
            raise ValueError ("deposito  precisa ser numerico")
        self._saldo += valor
        self.detalhes()

    def detalhes(self):
        print(f'Agência: {self.agencia}', end = ' ')
        print(f'Conta: {self.conta}', end=' ')
        print(f'Saldo: {self.saldo}')
    @abstractclassmethod
    def sacar(self, valor):
        pass

class ContaPoupanca(Conta):
    def sacar(self, valor):
        if self.saldo < valor:
            print('saldo insuficiente')
            return
        self.saldo -= valor
        self.detalhes()

class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo, limite = 100):
        super().__init__()
        self._limite = limite

    @property
    def limite(self):
        return self._limite



    def sacar(self, valor):
        if (self.saldo + self.limite) < valor:
            print('saldo insuficiente')
            return
        self.saldo -= valor
        self.detalhes()

#main

cp = ContaPoupanca(1111, 2222, 0)
cp.depositar(100)
cp.sacar(10)

cc = ContaCorrente(222, 33333, 0)
cc.depositar(100)
