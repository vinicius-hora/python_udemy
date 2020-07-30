string = 'o brasil é o pais do futebol brasil brasil, o brasil é penta'
lista1 = string.split(' ')
lista2 = string.split(',')

palavra = ''
cont = 0
for valor in lista1:
    qtdVezes = lista1.count(valor)
    if qtdVezes > cont:
        cont = qtdVezes
        palavra = valor

print(f'a palavra {palavra} apareceu {cont}x')
print(lista1)

for indice, valor in enumerate(lista1):
    print(indice, valor)
