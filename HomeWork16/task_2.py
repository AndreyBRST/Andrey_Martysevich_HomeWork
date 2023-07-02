# 2)	Функция sum(a,b) принимает 2 числа и возвращает их сумму. Написать декоратор, который возвращает ошибку если
# переданы не числовые параметры(например строка)
# примерно такое:
# @validate_int_parameters
# def sum(a,b)
# sum(3, "1") => ошибка sum(4, 2) = > 6

def validate_int_parameters(func):
    def num1(a, b):
        if not (isinstance(a, int) and isinstance(b, int)):
            return ValueError('Вы ввели не числовые параметры!')
        return func(a, b)
    return num1

@validate_int_parameters
def sum(a, b):
    return a, b
# a = int(input('Введите первое число: '))
# b = int(input('Введите второе число: '))
# print(f'({a},{b}) => {sum(a,b)}')
a = 3
b = "1"
print(sum(a,b))






