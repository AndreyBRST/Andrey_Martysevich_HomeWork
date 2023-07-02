# Функция для определения всех чисел, на которые без остатка делится указанное


def func_1(num1):
    del_nums = []
    for i in range(1, num1 + 1):
        if num1 % i == 0:
            del_nums.append(i)
    return del_nums
num2 = int(input('Введите число для проверки: '))
print(f'Результат определения: {func_1(num2)}')







