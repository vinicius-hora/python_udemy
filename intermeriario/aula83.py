file = open('abc.txt', 'w+')
file.write('linha 1\n')
file.write('linha 2\n')
file.write('linha 3\n')
print('lendo linhas: ')
file.seek(0, 0)
print(file.read())
print('#########################')
file.seek(0, 0)
print(file.readline())
print(file.readline())
file.close()

with open ('abc2.txt', 'w+') as file:
    file.write('linha 1\n')
    file.write('linha 2\n')
    file.write('linha 3\n')
    print('lendo linhas: ')
    file.seek(0, 0)
    print(file.read())