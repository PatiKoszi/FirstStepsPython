


def sortowanieBabelkowe(lista):
    for i in range(len(lista)):
        for j in range(len(lista) - 1 - i):
            if lista[j] > lista[j + 1]:
                lista = swap(lista,j,j+1)
            printLista(lista)

def swap(lista, i, j):
    lista[i], lista[j] = lista[j], lista[i]
    return lista

def printLista(lista):
    for x in lista:
        print(x, end=', ')
    print(' ')



lista = [6, 1, 8, 9, 12, 3, -1, 0, -69]
sortowanieBabelkowe(lista)
