# -*- encoding: iso-8859-1 -*-

""" Mini-calculadora, feita como exerc�cio em Python """


class CalcError(Exception):
    pass


class Calc(object):
    """ Implementa todo o processo da calculadora, desde a leitura at� o parsing. """

    TOK_IMPR, TOK_FIM, TOK_NOME, TOK_NUM = range(4)

    def __init__(self, entrada):
        """ Inicializa a calculadora.
        entrada deve ser um objeto que tenha o m�todo read().
        """
        self.entrada = entrada
        self.cur_tok = Calc.TOK_IMPR
        self.num_value = 0.0
        self.str_value = ''
        self.values = {'pi': 3.14156}
        import re
        self.letras = re.compile('[a-zA-Z]')
        self.numeros = re.compile('[0-9\.]')

    def run(self):
        while self.cur_tok != Calc.TOK_FIM:
            try:
                valor = self.expr()
                if valor is not None:
                    print(valor)
            except CalcError as msg:
                print("Erro:", msg)

    def expr(self):
        esq = self.term()
        while self.cur_tok in ('+', '-', '\n'):
            if self.cur_tok == '+':
                esq += self.term()
            elif self.cur_tok == '-':
                esq -= self.term()
            else:
                break
        if self.cur_tok == Calc.TOK_FIM:
            return None
        return esq

    def term(self):
        esq = self.prim()
        while self.cur_tok in ('*', '/'):
            if self.cur_tok == '*':
                esq *= self.prim()
            else:
                v = self.prim()
                if v == 0.0:
                    raise CalcError("Divis�o por Zero")
                else:
                    esq /= v
        return esq

    def prim(self):
        self.next_token()
        v = 0.0
        if self.cur_tok == Calc.TOK_NOME:
            nome = self.str_value
            self.next_token()
            if self.cur_tok == '=':
                v = self.expr()
                self.values[nome] = v
                return v
            else:
                v = self.values.get(nome, 0.0)
                return v
        elif self.cur_tok == Calc.TOK_NUM:
            v = self.num_value
        elif self.cur_tok == '(':
            v = self.expr()
            if self.cur_tok != ')':
                raise CalcError("')' esperado")
        elif self.cur_tok == Calc.TOK_FIM:
            return 0
        else:
            raise CalcError("Token inesperado")
        self.next_token()
        return v

    def next_token(self):
        if not hasattr(self, 'ch'):
            ch = ' '
            while ch in (' ', '\t'):
                ch = self.entrada.read(1)
        else:
            ch = self.ch

        if self.numeros.match(ch):
            pontos = ch == '.' and 1 or 0
            s = ''
            while self.numeros.match(ch):
                s += ch
                ch = self.entrada.read(1)
                if ch == '.':
                    pontos += 1
            if pontos > 1:
                raise CalcError("Valor ponto flutuante inv�lido")
            self.num_value = float(s)
            self.cur_tok = Calc.TOK_NUM
        elif self.letras.match(ch):
            s = ''
            while self.letras.match(ch):
                s += ch
                ch = self.entrada.read(1)
            self.str_value = s
            self.cur_tok = Calc.TOK_NOME
        elif len(ch) == 0:
            self.cur_tok = Calc.TOK_FIM
        else:
            self.cur_tok = ch
            if ch == '\n':
                if hasattr(self, 'ch'):
                    del self.ch
                return
            ch = sys.stdin.read(1)

        while ch in (' ', '\t'):
            ch = sys.stdin.read(1)

        self.ch = ch


if __name__ == "__main__":
    import sys

    calc = Calc(sys.stdin)
    calc.run()