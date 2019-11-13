
sum = 0
for i in range(1,11):
    sum += i
    print(sum, end=' ')
print()

for i in range(1,6):
    szecian = i * i * i
    print(szecian, end = ' ')
print()

list = str(input(' Podaj imiona: '))
# split
for imie in list.split():
    print('hi ' + imie)