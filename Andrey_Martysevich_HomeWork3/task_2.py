# 2.Пользователь вводит три числа. Если все числа больше 10, то вывести на экран yes , иначе no
num1 = int(input('Введите первое число: '))
num2 = int(input('Введите второе число: '))
num3 = int(input('Введите третье число: '))
if num1 > 10 and num2 > 10 and num3 > 10:
    print('Yes')
else:
    print('No')