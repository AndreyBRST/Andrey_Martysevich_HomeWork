# 1)	Простейший калькулятор c введёнными двумя числами вещественного типа. Ввод с клавиатуры: операции + - * / и два числа.
# Операции являются функциями. Обработать ошибку: “Деление на ноль” Ноль использовать в качестве завершения программы
# (сделать как отдельную операцию).




def sum(num1, num3):
   return num1 + num3
def diff(num1, num3):
        return num1 - num3
def mult(num1, num3):
       return num1 * num3
def div(num1, num3):
    return num1 / num3

num1 = float(input('Введите первое число вещественного типа: '))
num2 = input('Введите арефметический символ (+,-,*,/): ')
num3 = float(input('Введите второе число вещественного типа: '))


if num2 == '+':
    print(f'{num1} + {num3} = {sum(num1, num3)}')
elif num2 == '-':
    print(f'{num1} - {num3} = {diff(num1,num3)}')
elif num2 == '*':
    print(f'{num1} * {num3} = {mult(num1,num3)}')
elif num2 == '/':
    print(f'{num1} / {num3} = {div(num1,num3)}')
else:
    print('Ошибка!')
while True:
    #print()
    num2 = input('Для завершения введите 0: ')
    if num2 == '0':
        print('Программа завершена!')
        break

















