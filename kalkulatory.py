initial_deposit = 250
annual_interst_rate = 0.015
annual_savings = 1080
period = 25


capital = 285.75

for i in range(period):
    odsetki = (capital * annual_interst_rate)
    capital = capital + annual_savings + odsetki
    print(capital)


