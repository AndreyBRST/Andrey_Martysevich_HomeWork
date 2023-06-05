# Дан список list=[15,48,'hello',6,19,'world’]. Все числа этого списка проверить на чётность. Если число чётное,
# то посчитать сумму его цифр. Если нечётное, то заменить  его на 1 в списке. Все слова: посчитать количество гласных и согласных.
# Вывести всё на экран.

list1 = [15, 48, 'hello', 6, 19, 'world']
list2 = ['a', 'e', 'i', 'o', 'u', 'y']

summ = 0
glas = 0
sogl = 0
for i in list1:
    if type(i) == int:
        if i % 2 == 0:
            summ += i
        print(i)
        else:
            index = list1.index(i)
            list1[index] = 1
            print(list1)
    elif type(i)






