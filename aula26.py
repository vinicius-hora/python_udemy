numero = input('digite um numero inteiro')
if numero.isdigit():
    numero = int(numero)
    if numero % 2 == 0:
        print('numero é par')
    else:
        print('numero é impar')
else:
    print('não é numero inteiro')

hora = input('digite a hora: ')
hora = int(hora)

if hora <= 11:
    print('bom dia')
elif hora > 11 and hora <18:
    print('boa tarde')
else:
    print('boa noite')

primeiroNome = input('digite o nome: ')
contNome = len(primeiroNome)

if contNome <= 4:
    print('nome curto')
elif contNome > 4 and contNome <=6:
    print('nome normal')
else:
    print('nome muito grande')

