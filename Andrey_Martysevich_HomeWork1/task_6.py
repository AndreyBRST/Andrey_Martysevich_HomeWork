#6.* Вычислить сумму цифр случайного трёхзначного числа.
import random

num1 = random.randint(100,999)
print ('Случайное число "num1" =', num1)
print(num1 // 100 + num1 // 10 % 10 + num1 % 10)
