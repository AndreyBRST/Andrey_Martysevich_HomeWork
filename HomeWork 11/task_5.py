# 5) Сгенерировать список используя генератор списков. В списке должно быть 10 элементов в произвольном случайном диапазоне.
# Перевести все числа в строку и получить из списка -  строку.

import random
list1 = [random.randint(0, 50) for i in range (10)]
list2 = []
for i in list1:
    str1 = str(i)
    list2.append(i)
print(','.join(map(str,list2)))






