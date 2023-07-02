#Написать 12 функций по переводу:
#
# 1. Дюймы в сантиметры
# 2. Сантиметры в дюймы
# 3. Мили в километры
# 4. Километры в мили
# 5. Фунты в килограммы
# 6. Килограммы в фунты
# 7. Унции в граммы
# 8. Граммы в унции
# 9. Галлон в литры
# 10. Литры в галлоны
# 11. Пинты в литры
# 12. Литры в пинты
# Написать программу, со следующим интерфейсом: пользователю предоставляется на выбор 12 вариантов перевода(описанных в первой задаче).
# Пользователь вводит цифру от одного до двенадцати. После программа запрашивает ввести численное значение. Затем программа
# выдает конвертированный результат. Использовать функции из первого задания. Программа должна быть в бесконечном цикле. Код выхода из
# программы - “0”.


def dum_v_cm(dum):
    return dum * 2.54
def cm_v_dum(cm):
    return cm / 0.39
def mil_v_km(mil):
    return mil * 1.61
def km_v_mil(km):
    return km / 0.62
def funt_v_kg(funt):
    return funt * 0.45
def kg_v_funt(kg):
    return kg / 2.2
def unc_v_gram(unc):
    return unc * 28.35
def gram_v_unc(gram):
    return gram / 0.035
def gallon_v_litr(gallon):
    return gallon * 4.55
def litr_v_gallon(litr):
    return litr / 0.22
def pint_v_litr(pint):
    return  pint * 0.57
def litr_v_pint(litr):
    return litr / 1.76
while True:
    print('1.Дюймы в сантиметры')
    print('2. Сантиметры в дюймы')
    print('3. Мили в километры')
    print('4. Километры в мили')
    print('5. Фунты в килограммы')
    print('6. Килограммы в фунты')
    print('7. Унции в граммы')
    print('8. Граммы в унции')
    print('9. Галлон в литры')
    print('10. Литры в галлоны')
    print('11. Пинты в литры')
    print('12. Литры в пинты')
    print('Для завершения программы введите "0": ')
    per = int(input('Что вы хотите перевести?: '))
    if per == 0:
        break
    num1 = int(input('Введите число которое хотите переневести: '))
    if per == 1:
        result = dum_v_cm(num1)
        print(dum_v_cm(per))
    elif per == 2:
        result = cm_v_dum(num1)
        print(cm_v_dum(per))
    elif per == 3:
        result = mil_v_km(num1)
        print(mil_v_km(per))
    elif per == 4:
        result = km_v_mil(num1)
        print(km_v_mil(per))
    elif per == 5:
        result = funt_v_kg(num1)
        print(funt_v_kg(per))
    elif per == 6:
        result = kg_v_funt(num1)
        print(kg_v_funt(per))
    elif per == 7:
        result = unc_v_gram(num1)
        print(unc_v_gram(per))
    elif per == 8:
        result = gram_v_unc(num1)
        print(gram_v_unc(per))
    elif per == 9:
        result = gallon_v_litr(num1)
        print(gallon_v_litr(per))
    elif per == 10:
        result = litr_v_gallon(num1)
        print(litr_v_gallon(per))
    elif per == 11:
        result = pint_v_litr(num1)
        print(pint_v_litr(per))
    elif per == 12:
        result = litr_v_pint(num1)
        print(litr_v_pint(per))
    else:
        print('Ошибка')


