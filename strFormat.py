waluta = 'dolar'
us = 1
pln = 4.08234915
print('Aktualna {} {} kosztuje {:.4f}'.format(us, waluta, pln))

print('{} ma {}'.format('Ala', 'kota'))

print('{1} ma {0}'.format('Ala', 'kota'))

#Zadanie1

dlugosc = int(input('Podaj dlugos w centymetrach: '))
metry = dlugosc/ 1000
cale = int(dlugosc) / 2.54
print('Twoje {} cm to {} metra'.format(dlugosc, metry))
print('Twoje {} cm to {:.4f} cala'.format(dlugosc, cale))

