a = lambda x,y: x * y
print(a(2,2))

lista = [
    ['p1', 13],
    ['p2', 135],
    ['p3', 10],
    ['p4', 18]
]
def ordena(item):
    return item[1]

lista.sort(key = lambda item: item[1], reverse= True)
print(lista)