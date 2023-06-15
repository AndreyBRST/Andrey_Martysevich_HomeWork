# На вход программы подается словарь a = {1:10, 2:20, 3:30}, необходимо получить список произведения ключа на значение.


a = {1:10, 2:20, 3:30}
a2 = []
for key in a.keys():
    print(f'Ключи: ',{key})
for value in a.values():
    print(f'Значение: ',{value})
for key,value in a.items():
    a2.append(key*value)
print(f'Результат умножения ключей на их значение: {a2}')



