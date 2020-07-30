minhaString = 'O rato roeu a roupa do rei de roma'
tamanhoString = len(minhaString)
novaString = ''
c = 0

while c < tamanhoString:

    if minhaString[c] == 'r':
        novaString = novaString + minhaString[c].upper()
    else:
        novaString = novaString + minhaString[c]


    c += 1
    print(novaString)



#print(novaString)

