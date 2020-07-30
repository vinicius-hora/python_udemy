d1 = {
    'chave1': 'valor',
    'chave2': 'outro valor',
    'chave3': 'Tupla'
}

#d1['nomedachave'] = 'agora essa merda existe'
'''d1.update({'nova_chave': 'novo_valor'})

if d1.get('nova_chave') is not None:
    print(d1.get('nova_chave'))
 '''

print(d1)
print('str' in d1)
print('valor' in  d1.values())
print(len(d1))

print('\n usando for: \n')
for k, v in d1.items():
    print(k, v)