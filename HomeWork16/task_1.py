# 1)	Реализовать калькулятор с 4 методами:
# Сумма, вычитание , умножение, деление.
# Метод принимает 2 аргумента и возвращает результат.
# Невалидные данные должны быть обработаны. Валидатором является в программе метод, который будет проверять
# ваши аргументы на то, является ли это число

def calculator(num):
    try:
        float(num)
        return True
    except ValueError:
        return False
def sum_numbers(num1, num2):
    if calculator(num1) and calculator(num2):
        return float(num1) + float(num2)
    else:
        raise ValueError("Невалидные данные, должны быть числа!")
def subtract_numbers(num1, num2):
    if calculator(num1) and calculator(num2):
        return float(num1) - float(num2)
    else:
        raise ValueError("Невалидные данные,должны быть числами!")
def multiply_numbers(num1, num2):
    if calculator(num1) and calculator(num2):
        return float(num1) * float(num2)
    else:
        raise ValueError("Невалидные данные, должны быть числами!")
def divide_numbers(num1, num2):
    if calculator(num1) and calculator(num2):
        if float(num2) != 0:
            return float(num1) / float(num2)
        else:
            raise ZeroDivisionError("Делить на ноль запрещено!")
    else:
        raise ValueError("Невалидные данные, должны быть числами!")

print(sum_numbers(1286, 13876))
print(subtract_numbers(13, 25))
print(multiply_numbers(44, 15))
print(divide_numbers(199, 3))


















