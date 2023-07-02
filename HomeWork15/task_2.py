# Написать функцию date, принимающую 3 аргумента — день, месяц и год. Вернуть True, если такая дата есть в нашем календаре,
# и False иначе.

def date(day, month, year):
    if 1 <= day <= 31:
        print(True)
    else:
        print(False)
    if 1 <= month <= 12:
        print(True)
    else:
        print(False)
    if 1 <= year <= 2023:
        print(True)
    else:
        print(False)
day = int(input('Введите день от 1 до 31: '))
month = int(input('Введите месяц от 1 до 12: '))
year = int(input('Введите год от 1 до 2023: '))
date(day, month, year)











