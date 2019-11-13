
class MojaKlasa:
    zmienna = "zupa"
    def funkcja(self):
        print("to jest wnętrze kalsy")

#Tworzymy objekt bedacy realizacja klasy
#Objekty biora swoje zmienne i funkcje z klas, są ich polaczeniem
#Zmienna moj objekt przechowuje obiekt klasy Mojaklasa
myobject = MojaKlasa()
print(myobject.zmienna)
myobject.funkcja()

#gotowa klasa Pojazd

class Pojazd:
    nazwa = ""
    rodzaj = "auto"
    kolor = ""
    wartosc = 100.00
    def opis(self):
        napis_opisu = "%s to %s %s warty %.2f zl." % (self.nazwa, self.kolor, self.rodzaj, self.wartosc)
        return napis_opisu

# Ponizej umiesc swoj kod

Auto1 = Pojazd()
Auto1.nazwa = "Ferrari"
Auto1.rodzaj = "kabriolet"
Auto1.kolor = "czerwony"
Auto1.wartosc = 60000.00

Auto2 = Pojazd()
Auto2.nazwa = "Ikarus"
Auto2.rodzaj = "autobus"
Auto2.kolor = "niebieski"
Auto2.warosc = 100000.00
głklj
# sprawdzenie kodu
print(Auto1.opis())
print(Auto2.opis())
