# Выведите статистику частности букв в кортеже
# long_word = ( 'т', 'т', 'а', 'и', 'и', 'а', 'и’,'и', 'и', 'т', 'т', 'а', 'и', 'и','и', 'и', 'и', 'т', 'и’)
# Примечание: Статистика частности - число повторений каждой из букв.

long_word = ( 'т' , 'т' , 'а' , 'и' , 'и' , 'и' , 'т' , 'т' , 'а' , 'и' , 'и' , 'и' , 'и' , 'т' , 'и')
print(long_word)
t = long_word.count('т')
a = long_word.count('а')
i = long_word.count('и')
print(f'Буква "т" повторяется: {t} ')
print(f'Буква "а" повторяется: {a} ')
print(f'Буква "и" повторяется: {i} ')





