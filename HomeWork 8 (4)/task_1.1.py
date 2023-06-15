# 1.1 Напишите программу, которая выполняет сравнение двух переменных .
num1 = int(input('Введите первое число: '))
num2 = int(input('Введите второе число: '))
if num1 > num2 and num1 < num2:
    print(f'{num1} Больше чем {num2}')
elif num1 < num2:
    print(f'{num1} Меньше чем {num2}')
else:
    print(f'{num1} Больше чем {num2}')