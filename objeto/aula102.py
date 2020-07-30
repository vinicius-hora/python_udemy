#classe
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__

    def falar(self):
        print('falando...')

class Cliente(Pessoa):
    def comprar(self):
        print(f'{self.nomeclasse} Comprando...')


class Aluno(Pessoa):
    def estudar(self):
        print(f'{self.nomeclasse} estudando...')

#main

c1 = Cliente('teste', 30)
c1.falar()
c1.comprar()

a1 = Aluno('vinicius', 28)
a1.falar()
a1.estudar()
