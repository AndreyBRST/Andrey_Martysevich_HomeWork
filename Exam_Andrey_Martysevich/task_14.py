# С клавиатуры вводится десятизначное число. Вывести на экран четные числа входящие в данное число. Например 1234567892  2 4 6 7 8 2

num1 = int(input('Введите десятичное число: '))
num2 = str(num1)
num3 = []
for i in num2:
    if int(i) % 2 == 0:
        num3.append(i)
        print(i)