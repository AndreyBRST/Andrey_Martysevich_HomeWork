# Есть список состоящий из слов и чисел, нужно записать в файл сначала слова в порядке их длины,
# а после слов цифры в порядке возрастания.

spis1 = ['Wary', 13, 'I', 51, 'Hangry', 129 ]
words = []
numbers = []
with open('task_1.txt.', 'w') as file:
    for i in spis1:
        if str(i).isalpha():
          words.append(i)
          words.sort(key=len)
        elif str(i).isdigit():
            numbers.append(i)
            numbers.sort()
        file.write(f'{words}\n{numbers}')
spis2 = words + numbers
print(spis2)























