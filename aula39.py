loginUser = False

msg = 'usuário logado' if loginUser else 'usuário precisa logar'

print(msg)

idade = input(' digite a idade: ')
maior = int(idade) >= 18

msg = 'pode acessar' if maior else 'não pode acessar'
print(msg)