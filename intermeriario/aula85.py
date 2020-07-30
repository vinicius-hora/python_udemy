

def master(funcao):
    def slave():
        print('agora estou decorada')
        funcao()
    return slave
@master
def fala_oi():
    print('oi')

def outra_func():
    print('outro oi')
var = master()
var()