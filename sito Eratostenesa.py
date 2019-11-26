def sito_Eratostenesa(n):
    primes = [1 for x in range(n+1)]
    for i in range(2, n):
        for j in range(i+1, n):
            if j % i == 0:
                primes[j] = 0
    return primes
print(sito_Eratostenesa(30))