# В текстовом файле посчитать количество строк, а также для каждой
# отдельной строки определить количество в ней символов.

with open('task_3.txt', 'r') as file:
    list1 = file.read().split('\n')
    print(list1)
    count = 0
    for i in list1:
        count += 1
        print(f"В {count} строке {len(i)} символов")


















