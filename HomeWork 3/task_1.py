# 1. Определить, является ли год високосным.
num1 = int(input('Введите год: '))
if num1 % 4 == 0:
    print(f'{num1} Год высокосный ')
else:
    print(f'{num1} Год не высокосный ' )