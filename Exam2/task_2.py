# 2.Найти в списке те элементы, значение которых меньше среднего арифметического, взятого от всех элементов списка.

import random

num1 = int(input('Введите первое число: '))
num2 = int(input('Введите второе число: '))
list1 = [random.randint(num1, num2) for i in range(10)]
sered = sum(list1) / len(list1)
list2 = []

for i in list1:
    if i < sered:
        list2.append(i)
print(list1)
print(sered)
print(list2)








