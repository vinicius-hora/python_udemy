class Pessoa:
    ano_atual = 2020
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        print(self.ano_atual - self.idade)

    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)


p1 = Pessoa('vinicius', 28)
print(p1)
print(p1.nome)
"""
    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.falando = falando
        self.comendo = comendo

    def falar(self, assunto):
        if self.comendo:
            print(f'{self.nome} não pode falar comendo')
            return

        if self.falando:
            print(f'{self.nome} já está falando sobre {assunto}')
            return
        print(f'{self.nome} está falando')
        self.falando = True

    def parar_falar(self):
        if not self.falando:
            print(f'{self.nome} não está falando')
            return

        print(f'{self.nome} parou de falar')
        self.falando = False


    def comer(self, alimento):
        if self.comendo:
            print(f'{self.nome} já está comendo')
            return

        if self.falando:
            print(f'{self.nome} Não pode comer falando.')
            return

        print(f'{self.nome} está comendo {alimento}.')
        self.comendo = True

    def parar_comer(self):
        if not self.comendo:
            print(f'{self.nome} não está comendo')
            return

        print(f'{self.nome} parou de comer')
        self.comendo = False
"""


