def minimum(lista):
    min = lista[0]
    minidex = 0
    for i in range(len(lista)):
        if lista[i] < min:
            min = lista[i]
            minidex = i
    print(min)
    print(minidex)

minimum([1,5,-8,0,3])
