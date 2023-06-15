# 3. Создайте словарь из строки ' An apple a day keeps the doctor away' следующим образом: в качестве ключей возьмите
# символы строки, а значениями пусть будут числа, соответствующие количеству вхождений данной буквы в строку.


str1 = 'An apple a day keeps the doctor away'
my_dict = {i: str1.count(i) for i in str1}
print(my_dict)











