class A:
    vc = 123

a1 = A()
a2 = A()

A.vc = 321

print(a1.vc)
print(A.vc)