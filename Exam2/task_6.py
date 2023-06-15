# 6. Сжать массив, удалив из него все элементы, величина которых находится в интервале [а, b].
# Освободившиеся в конце массива элементы заполнить нулями.


import random

a = int(input('Введите первое число "a": '))
b = int(input('Введите второе число "b": '))
num1 = [random.randint(0, 89) for i in range(7)]
print(num1)
num2 = []
for i in num1:
    if a <= i <= b:
        del i
    else:
        num2.append(i)
    num3 = len(num2)
for i in range(7 - num3):
    num2.append(0)
print(num2)










