# 4) Имеется файл file.txt с текстом на латинице. Напишите программу, которая выводит следующую статистику по тексту:
# •	количество букв латинского алфавита;
# •	число слов;
# •	число строк.
# Пример ввода и вывода
# Предположим, что file.txt содержит приведенный ниже текст:
# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.


number_of_letters = 0
number_of_words = 0
number_of_rows = 0
with open('file.txt', 'r') as file:
    text = file.readlines()
for spis in text:
    number_of_letters = sum(map(str.isalpha, spis))
    number_of_words = len(spis.split())
    number_of_rows += 1
print(number_of_letters)
print(number_of_words)
print(number_of_rows)














