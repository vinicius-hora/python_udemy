s1 = {1,2,3,4,5,6}

print(s1)

s2 = set()
s2.add(3)
s2.add(4)
s2.discard(3)
s2.update('Python')

print(s2)
s3 = s1 | s2
print(s3)
