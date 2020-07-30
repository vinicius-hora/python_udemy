from itertools import combinations, product

numero = ['0','1']

for grupo in product(numero, repeat=4):
    print(grupo)