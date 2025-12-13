# 2. Дана строка-предложение.
# Вначале поместить символы на четных позициях,
# затем в обратном порядке символы на нечетных позициях.

s = input('Введи строку: ')

even = []
odd = []

i = 0
while i < len(s):
    if i % 2 == 0:
        even.append(s[i])
    else:
        odd.append(s[i])
    i += 1

odd.reverse()

Encrypted = ''.join(even) + ''.join(odd)

print('Зашифрованная строка:', Encrypted)
