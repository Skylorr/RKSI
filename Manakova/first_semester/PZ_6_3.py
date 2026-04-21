# 3. Дан список размера N.
# Переставить в обратном порядке элементы между минимальным и максимальным.

N = int(input('Введи размер списка: '))
ListAppend = []

i = 0
while i < N:
    ListAppend.append(int(input('Введи элемент списка: ')))
    i += 1

print('Исходный список:', ListAppend)

mn = min(ListAppend)
mx = max(ListAppend)

imin = ListAppend.index(mn)
imax = ListAppend.index(mx)

start = min(imin, imax)
end = max(imin, imax)

part = ListAppend[start:end+1]
part.reverse()

ListAppend[start:end+1] = part

print('Полученный список:', ListAppend)
