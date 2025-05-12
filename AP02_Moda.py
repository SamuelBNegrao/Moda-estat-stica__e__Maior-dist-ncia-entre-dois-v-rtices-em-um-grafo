def moda(lista):
    modas = {}
    for indx in lista:
        if indx in modas:
            modas[indx] += 1
        else:
            modas[indx] = 1
    maior_valor = 0
    maior_chave = None
    for chave in modas:
        if maior_valor < modas[chave]:
            maior_valor = modas[chave]
            maior_chave = chave 
    print(maior_chave)
    return

lista1 = [0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9]
lista2 = [i//10 for i in range(100, -10, -1)] + [10,11,12,13,14,5,16,17,18,19]
lista3 = [(i**3)//1000 for i in range(100, -10, -1)]

moda(lista1)
moda(lista2)
moda(lista3)
