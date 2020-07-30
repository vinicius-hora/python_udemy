def func(*args, **kwargs):
    print(args)
    print(kwargs)
    print(len(args))

    nome = kwargs.get('nome')
    print(nome)
lista = [1,2,3,4,5]
lista2 = [10,20,30,40]

func(*lista, *lista2, nome = 'vinicius', sobrenome = 'teste')
