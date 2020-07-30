#exercicio 1
def saudacao(msg, nome):
    return f'{msg} seu nome é {nome}'

variavel = saudacao('bom dia', 'fulano')
print(variavel)

#exercicio 2
def soma(n1, n2, n3):
    return n1 + n2 + n3
resultado = soma(5, 10, 15)
print(resultado)

#exercicio 3
def porcentagem(valor, aumento):
    return (valor / 100) * aumento + valor
total = porcentagem(100, 50)
print(total)

#exercicio 4
def fizzbuzz(numero):
    if numero % 3 == 0 and numero % 5 ==0:
        return 'fizzbuzz'
    if numero % 3 == 0:
        return 'fizz'
    if numero % 5 == 0:
        return 'buzz'

    return numero

teste = fizzbuzz(7)
print(teste)