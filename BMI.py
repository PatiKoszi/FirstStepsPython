print('Kalkulatro BMI')
waga = input("Podaj swoja wage:   ")
wzrost = input ('Podaj swoj wzrost:  ')

BMI = (int(waga) / (int(wzrost) ** 2)) * 10000
print('Twoj BMI to: ' + str(round(BMI,2)))

if BMI < 18.5:
    print('niedowag')
elif BMI >=18.5 and BMI <= 24.9:
    print('waga prawidlowa')
elif BMI > 25 and BMI <= 29.9:
    print ('nadwaga')
elif BMI > 30:
    print ('otylosc')





