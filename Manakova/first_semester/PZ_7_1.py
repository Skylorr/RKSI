# 1. Дано целое число N (1 < N < 26).
# Вывести N первых прописных букв латинского алфавита.

N = int(input('Введи число N (1 < N < 26): '))

Letters = []
i = 0
while i < N:
    Letters.append(chr(ord('A') + i))
    i += 1

print('Первые', N, 'букв латинского алфавита:')
print(''.join(Letters))
