l1 = [1,2,3,4,5,6,7,8,9]
l2 = [variavel for variavel in l1]
print(l2)

l3 = [variavel * 2 for variavel in l1]
print(l3)

l4 = [(v, v2)for v in l1 for v2 in range(3)]
print(l4)

s1 = ['luiz', 'vinicius', 'livia']
s2 = [v.replace('i', '@') for v in s1]
print(s2)

lista = list(range(100))
print(lista)
lista1 = [v for v in lista if v %3 == 0 if v % 8 == 0]
print(lista1)

lista2 = [v if v % 3 == 0 else 0 for v in lista]
print(lista2)