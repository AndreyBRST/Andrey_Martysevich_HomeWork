# Функция для определения того, является ли строка палиндромом

def Palindrome(str1):
    str1 = ''.join(str1.split(' ')).casefold()
    rev = reversed(str1)
    return list(str1) == list(rev)

new_string = input('Введите строку для определения: ')
print(Palindrome(new_string))








