# Казино. Компьютер генерирует числа от 1 до 10 и от 1 до 2-х соответственно. Цифры от одного до 10 отвечают за номера,
# а от 1 до 2 за цвета(1-красный,2 черный). Пользователю дается 5 попыток угадать номер и цвет(Прим. введения с клавиатуры: 3 красный).
# В случае неудачи вывести на экран правильную комбинацию.

import random

lucky_number = str(random.randint(1, 10))
colour = random.randint(1, 2)
if colour == 1:
    colour = 'Красное' or 'К'
else:
    colour = 'Черное' or 'Ч'
attempt = 1
you_comb =  str(lucky_number + ' ' + colour)
while attempt:
    bet_comb = input(f'Выберите цифру от 1 до 10, и цвет Красный или Черный : ')
    bet_comb = bet_comb.strip()
    attempt += 1
    if you_comb == bet_comb:
        print(f'Выигрыш есть-можно поесть')
        break
    elif attempt > 5:
        print(f'Проиграть – не значит сдаться. \n Правильный ответ: {you_comb}')
        break
    else:
        print(f'Попытка не пытка. \n Номер: {attempt}')

