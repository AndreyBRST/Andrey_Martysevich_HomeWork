# Создать текстовый файл, записать в него построчно данные, которые вводит пользователь.
# Окончанием ввода пусть служит пустая строка.

with open('task_2.txt', 'w') as file:
    while True:
        tekst = (input('Введите текст: '))
        #file.write(f'{tekst} \n')
        file.write(f'\n')
        if tekst == ' ':
            break




















