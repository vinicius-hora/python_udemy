def olaMundo():
    return 'olá mundo'

def mestre(funcao):
    return funcao()

teste = mestre(olaMundo)
print(teste)

#exericico 2

def mestre(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)
def falaOi(nome):
    return f'oi{nome}'
def saudacao(saudacao, nome):
    return f'{saudacao} e {nome}'

executar = mestre(falaOi, 'vinicius')
print(executar)