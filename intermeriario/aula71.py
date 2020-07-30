from itertools import count

contador = count(start = 5, step = 2)

for valor in contador:
    print(valor)

    if valor >=100:
        break
