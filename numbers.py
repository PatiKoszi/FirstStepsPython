# naiwny test pierwszosci
def liczby_pierwsze(x):
    if x <= 1:
        return False
    for i in range(2,x):
        if x % i == 0:
            return False
        else:
            return True
print(liczby_pierwsze(16))
print(liczby_pierwsze(7))
print(liczby_pierwsze(13))

# sito eratrotenesa




