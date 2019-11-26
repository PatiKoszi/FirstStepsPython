# ja w przedziale liczb znalez te podzielne przez podana liczbe
i = 0
while i < 20:
    i += 1
    if i % 4 != 0:
        continue
    print(i)

# tabliczka mnożenia
for i in range(1,10):
    for j in range(1,10):
        print(i*j, end='   ')
    print("\r")

