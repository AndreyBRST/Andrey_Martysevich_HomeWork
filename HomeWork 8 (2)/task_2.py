#2. Даны два действительных числа. Найти среднее арифметическое и среднее геометрическое этих чисел.
num1 = int(input("Введите первое действительное число"))
num2 = int(input("Введите второе действительное число"))
a = (num1 + num2)/2 # арефметическое
b = (num1 * num2) ** 0.5 # геометрическое
print(a)
print(b)
