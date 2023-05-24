x = int(input('Введите рост 1 человека: '))
y = int(input('Введите рост 2 человека: '))
z = int(input('Введите рост 3 человека: '))

if x < y:
    x, y = y, x

if y < z:
    y, z = z, y

if x < y:
    x, y = y, x

print(x, y, z)