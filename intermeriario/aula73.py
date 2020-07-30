from itertools import groupby

alunos = [
    {'nome': 'luiz', 'nota': 'a'},
    {'nome': 'marcos', 'nota': 'b'},
    {'nome': 'teste', 'nota': 'c'},
    {'nome': 'maria', 'nota': 'd'},
    {'nome': 'vinicius', 'nota': 'a'},
    {'nome': 'pedro', 'nota': 'b'},
    {'nome': 'alguem', 'nota': 'c'},
    {'nome': 'roberta', 'nota': 'd'},
]

ordena = lambda item: item['nota']
alunos.sort(key=ordena)
alunosAgrupados = groupby(alunos, ordena)

for agrupamento, valoresAgrupados in alunosAgrupados:
    print(f'agrupamento: {agrupamento}')
    quantidade = len(list(valoresAgrupados))
    print(f'{quantidade} alunos tiraram {agrupamento}')