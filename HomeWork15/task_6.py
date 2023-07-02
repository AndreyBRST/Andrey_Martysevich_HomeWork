# Напишите функцию для сортировки слов в алфавитном порядке

def alf_sort(str):
    alf = [text.lower() for text in str.split()]
    alf.sort()
    return alf
test_word = input('Введите слова для сортировки: ')
print(f'Результат сортировки: {alf_sort(test_word)}')










