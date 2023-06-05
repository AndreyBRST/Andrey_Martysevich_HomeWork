#3. Ввести предложение. Если число символов в предложении кратно 3 - добавить ! к концу строки. Вывести строку на экран.
string = input('Введите предложение: ')
str_len = int(string)
if str_len % 3 == 0:
    new_str = string + '!'
    print(new_str)
else:
    print(string)