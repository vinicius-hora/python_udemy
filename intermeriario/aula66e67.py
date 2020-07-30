carrinho = []

carrinho.append(('produto 1', 30))
carrinho.append(('produto 2', 50))
carrinho.append(('produto 3', 40))
carrinho.append(('produto 4', 35))

total = sum([float(y) for x,y in carrinho])
print(total)