
# https://leanpub.com/pyprog/read#leanpub-auto-wprowadzenia--o-zawartoci-podrcznika
# Przykład 1.1 (objects):

text = str('123')
print(text.replace('2', 'a'))
n=1
print(n.__class__)
r=1.0
print(r.__class__)

#Przykład 1.2 (sort):

a = [1,5,4,2,0]
print(a)
b = a; b.sort()
print(b)
#Ostatni wiersz w powyższym przykładzie pokazuje, że należy odróżnić wynik działania funkcji
#(w tym wypadku metodę sort()) i wynik zwracany przez funkcję
print(a.sort())

# Przykład 1.3: Tabliczka mnozenia
digits = (0,1,2,3,4,5,6,7,8,9)
for i in digits:
    for y in digits:
        print('%s x %s = %s' % (i,y,i*y) )

# Oto przegląd dostępnych operatorów:
a = 13; b = 3
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b) #zaokrągla wynik w dół do najbliższej liczby > całkowitej
print(a%b)
#Operatory bitowe doczytac


#not (logiczne NIE)
#and and (logiczne I)
#or (logiczne LUB)


