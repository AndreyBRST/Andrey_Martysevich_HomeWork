# 5) Создайте 2 множества:
# - Если они одинаковые: вывести что они равны
# - Если 1 множество полностью состоит из второго: вывести сообщение множество 1
# состоит из множества2
#
# - Если 2 множество полностью состоит из 1: вывести сообщение множество 2
#  	 состоит из множества 1
#
# - Если они пересекаются: вывести элементы в которых они пересекаются
# - Если не пересекаются: вывести сообщение об этом

set1 = {1, 2, 3, 4, 5, 6, 7, 8}
set2 = {8, 9, 10, 11, 12, 1, 3}
if set1 == set2:
    print(f'Множества равны')
elif set1.issubset(set2):
    print(f'Множество №1 состоит из множества #2: {set1.issubset(set2)}')
elif set2.issubset(set1):
    print(f'Множество №2 состоит из множества №1: {set2.issubset(set1)}')
elif set1.intersection(set2):
    print(f'Множества пересекаются в этих элементах: {set1.intersection(set2)}')















