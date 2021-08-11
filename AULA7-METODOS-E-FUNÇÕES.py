#criando uma função
#funcao maior item
def maior(colecao):
    maior_item  = colecao[0]
    for item in colecao:
        if item > maior_item:
            maior_item = item
    return maior_item

print(maior([1, 2, 3, 4, 5, 78, 98, 0]))

#funcao menor item
def menor(colecao):
    menor_item = colecao[0]
    for item in colecao:
        if item < menor_item:
            menor_item = item
    return menor_item

print(menor([2, 3, 6, 8, 45, 2, 1, 0]))