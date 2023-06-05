# Напишите программу, которая запрашивает у пользователя информацию о различных книгах и сохраняет их данные в
# файл формата CSV.
# Требования: Программа должна запрашивать у пользователя информацию о каждой книге, включая название, автора и год издания.
# Информация о каждой книге должна быть сохранена в отдельной строке файла CSV. Файл CSV должен иметь следующие заголовки столбцов:
# "Название", "Автор", "Год издания". Программа должна продолжать запрашивать информацию о книгах до тех пор, пока пользователь не введет
# команду "stop" для завершения. В конце выполнения программы должно быть выведено сообщение о успешном сохранении данных.


import csv
with open('library.csv', 'w', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(['Название книги', 'Автор', 'Год издания'])
    while True:
        title = input('Введите название книги: ')
        if title == 'stop':
            break
        name = input('Введите ФИО автора: ')
        if name == 'stop':
            break
        yers = input('Введите год издания: ')
        if yers == 'stop':
            break
        writer.writerow([title,name,yers])
print('Данные успешно сохранены!')















