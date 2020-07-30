t1 = 1,2,3,4,5,'teste'
t2 = 6,7,8,9,'vinicus'
t3 = t1 + t2

n1,n2,n3, *_ = t3
t2 = list(t2)
t2[2] = 'troquei o valor'
t2 = tuple(t2)

print(t3)
print(n1)
print(n3)
print(t2)