def sortowanieBabelkowe(lista):
    for i in range(len(lista)):
        for j in range(len(lista)-1-i):
            if lista[j] > lista[j+1]:
                swap(lista, j, j+1)
        print(lista)

def swap(lista, a, b):
    lista[a], lista[b] = lista[b], lista[a]


lista = [6,1,5,8,-5,-2,0]

sortowanieBabelkowe(lista)