# 4) Дана строка. Сохранить в ней только первые вхождения символов, удалив все остальные. Результат вывести в виде кортежа.


string = 'Hello'
print(string)
# tuple = tuple(string)
print(tuple(set(string)))
print(tuple(set(string).pop()))








