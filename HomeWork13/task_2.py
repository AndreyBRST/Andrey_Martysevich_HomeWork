# 2) Если в функцию передается кортеж, то посчитать длину всех его слов. Если список, то посчитать кол-во букв и чисел в
# нем.
# Число - количество нечетных цифр. Строка - количество букв.

def func(data):
    if type(data) == tuple:
        return sum(len(str(i)) for i in data if isinstance(i, str))
    elif type(data) == list:
        letters = 0
        nums = 0
        for i in data:
            if type(i) == str:
                letters += len(i)
            elif type(i) == int and i % 2 != 0:
                nums += 1
        return letters, nums

# my_tuple = (1, 2, 3, 'hello', 'world')
# my_list = [1, 2, 3, 'hello', 'world']
# print(f'длина слов в кортеже = {func(my_tuple)}')
# print(f'количество букв и нечётных чисел в списке = {func(my_list)}')

func_tuple = ('Hello', 'Moscow', 'Brest')
func_list = [23, 'Order', 45, 'Cat', 'Sun']
print(f'Длина всех слов: {func(func_tuple)}')
print(f'Количество букв и нечетных чисел: {func(func_list)}')
































