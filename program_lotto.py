import random

def lista(n):
    lotto_digits = []
    for i in range(1,n+1):
        lotto_digits.append(i)
    print(lotto_digits)
lista(10)

def lista1(n):
    return[i+1 for i in range(n)]
print(lista1(10))

lista3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(lista3)

lista4 = list(range(1, 49))
print(lista4)


wylosowana_lista = random.sample(lista4, k=6)
wylosowana_lista.sort()
print(wylosowana_lista)

for j in wylosowana_lista:
    if j in lista4:
        lista4.remove(j)
print(lista4)






