# 2.Есть список с четными и нечетными элементами. Посчитать количество четных и нечетных элементов.
list_nums = [2, 3, 6, 9, 12, 14, 15, 21, 33, 56, 72, 75, 91]
chet = 0
nechet = 0
for num in list_nums:
    if  num % 2 == 0:
        chet += 1
    else:
        nechet +=1
print(f'Четные: {chet} ')
print(f'Нечетные: {nechet} ')
