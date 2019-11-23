import random


print("Podaj pseudonim: ")
nick = input()
#haslo = "skarpeta"

lista = ["jedenastopietrowiec", "ostatni"]
haslo = str(lista[random.randint(0, len(lista)-1)])
tablica = list(haslo)

for i in range(len(haslo)):
    tablica[i] = '_'
# print(tablica)
print(' '.join(tablica))

zycia = 6

while zycia > 0:
    print(nick, "Pozostalo ci ", zycia, "zyc")
    # litera = input("Podaj litere: ")
    print(nick, "Podaj litere: ")
    litera = input()

    if litera in haslo:
        for i in range(len(tablica)):
            if haslo[i] == litera:
                tablica[i] = litera
                print(' '.join(tablica))
        if ''.join(map(str, tablica)) == haslo:
            print(nick, "ZWYCIESTWO!!!")
            break
    else:
        zycia -= 1






