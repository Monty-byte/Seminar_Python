import math
print('Задача 1')
n = int(input('Введите количество километров, которые машина проезжает за день: '))
m = int(input('Введите длину маршрута: '))

result: float = m/n

# result = math.ceil(result)

result = m // n + int(m % n > 0)


print(f'Количество дней = {result}')

