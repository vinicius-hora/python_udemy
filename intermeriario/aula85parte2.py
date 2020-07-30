from time import time
from time import sleep

def vel(func):
    def inter(*args, **kwargs):
        start_time = time()
        result =  func(*args, **kwargs)
        end_time = time()
        tempo = (end_time - start_time)*1000
        print(f'A funcao {func.__name__} levou {tempo: .2f} para executar')
    return inter
@vel
def demora():
    for i in range(5):
        print(i)
        sleep(1)

demora()