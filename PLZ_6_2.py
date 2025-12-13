# 2. Дан список размера N.
# Найти номер последнего локального максимума.

N = int(input('Введи размер списка: '))
ListAppend = []

i = 0
while i < N:
    ListAppend.append(int(input('Введи элемент списка: ')))
    i += 1

print('Список:', ListAppend)

last = -1
i = 1
while i < N - 1:
    if ListAppend[i] > ListAppend[i - 1] and ListAppend[i] > ListAppend[i + 1]:
        last = i
    i += 1

if last == -1:
    print('Локальных максимумов нет')
else:
    print('Номер последнего локального максимума:', last)
