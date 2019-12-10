lista = [1, 6, 8, 9, 12, 3, -1, 0, -69]

for i in range(len(lista)):
    for j in range(len(lista) - 1):
        if lista[j] > lista[j+1]:
            temp = lista[j]
            lista[j] = lista[j+1]
            lista[j + 1] = temp
     for x in lista:
        print(x, end=', ')
     print('')
