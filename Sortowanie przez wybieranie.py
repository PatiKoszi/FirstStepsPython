def minimum(lista):
    min = lista[0]
    for i in range(len(lista)):
        if lista[i] < min:
            min = lista[i]
    print(min)

minimum([1,5,-8,0,3])
