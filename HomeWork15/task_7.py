# Напишите функцию, которая определяет количество гласных в строке

def glas_str(text):
    glas1 = ('А', 'а', 'У', 'у', 'О', 'о', 'Ы', 'ы', 'И', 'и', 'Э', 'э', 'Я', 'я', 'Ю', 'ю', 'Ё', 'ё', 'Е', 'е')
    glas2 = ('A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u', 'Y', 'y')
    text_glas = 0
    for i in text:
        if i in glas1:
            text_glas += 1
        elif i in glas2:
            text_glas += 1
    return text_glas
popytka = input('Введите строку для определения: ')
print(f'Результат определения: {glas_str(popytka)}')












