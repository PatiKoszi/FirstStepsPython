
fruits = ['apple', 'orange','pear', 'banana', 'apple']

print('start')
for i, fruit in enumerate(fruits):
    print('sprawdzam pozycje:  {} {}'.format(i, fruit))
    print('{} to pozycja sprawdzana'.format(fruit))
    print(i)
    if i == 3:
        break
    print(i)
    print(fruit)
print('koniec')









