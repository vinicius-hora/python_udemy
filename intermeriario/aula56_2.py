clientes = {
    'cliente1' :  {
        'nome': 'vinicius',
        'sobrenome': 'bastos',
    },
    'cliente2': {
        'nome': 'teste',
        'sobrenome': 'outro',
    },
    'cliente3': {
        'nome': 'Paulo Cesar',
        'sobrenome': 'da Hora',
    },

}

for clientes_k, clientes_v in clientes.items():
    print(f'exibindo {clientes_k}')
    for dados_k, dados_v in clientes_v.items():
        print(f'\t{dados_k} = {dados_v}')