def sito_Eratostenesa(n):
    temp = [1 for x in range(n+1)]
    for i in range(2, n+1):
        for j in range(i+1, n+1):
            if j % i == 0:
                temp[j] = 0
    print(temp)
    primes = []
    for i in range(len(temp)):
        if temp[i] == 1:
            primes.append(i)

    return primes
print(sito_Eratostenesa(100))