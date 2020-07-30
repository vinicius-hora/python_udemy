class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, pertentual):
        self.preco = self.preco - (self.preco * (pertentual / 100))

    #Getter
    @property
    def preco(self):
        return self._preco

    # Setter
    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str):
            valor = float(valor.replace('R$', ''))

        self._preco = valor



p1 = Produto('camisa', 50)
p1.desconto(10)
print(p1.preco)

p2 = Produto('caneca', 15)
p2.desconto(10)
print(p2.preco)
p3 = Produto('caça', 'R$ 100')
p3.desconto(25)
print(p3.preco)