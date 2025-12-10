# Даны два целых числа: A, B. Проверить истинность высказывания:
# «Справедливы неравенства A > 2 и B < 3».

a, b = input("Введите A: "), input("Введите B: ")

while type(a) != int:
    try:
        a = int(a)
    except ValueError:
        print("Неправильно ввели!")
        a = input("Введите A: ")

while type(b) != int:
    try:
        b = int(b)
    except ValueError:
        print("Неправильно ввели!")
        b = input("Введите B: ")

if a > 2 and b < 3:
    print("Высказывание истинно.")
else:
    print("Высказывание ложно.")