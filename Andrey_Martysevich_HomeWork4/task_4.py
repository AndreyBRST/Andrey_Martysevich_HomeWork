# 4. Дан список чисел. Если число встречается более двух раз, то добавить его в новый список
list1 = [1, 1, 3, 24, 29, 44, 98, 5, 44, 91, 25, 91, 79]
list2 = []
for i in list1:
        if list1.count(i) > 1:
                list2.append(i)
print(list2)
