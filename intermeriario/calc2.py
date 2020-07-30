import math

PI = math.pi


def dobraLista(lista):
    return [x * 2 for x in lista]


def multi(lista):
    r = 1
    for i in lista:
        r *= i

    return r

if __name__ == '__main__':
    lista = [1, 2, 3, 4, 5]
    print(dobraLista(lista))
    print()
    print(multi(lista))
