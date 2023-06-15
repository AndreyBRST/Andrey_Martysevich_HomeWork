# 2. Определить существование треугольника.
num1 = int(input('Сторона A: '))
num2 = int(input('Сторона B: '))
num3 = int(input('Сторона C: '))
if num1 + num2 > num3 and num1 + num3 > num2 and num3 + num2 > num1:
    print('Треугольник существует')
else:
    print('Треугольник не существует')