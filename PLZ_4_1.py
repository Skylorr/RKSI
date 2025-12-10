p = input("Введите цену за 1 кг конфет: ")

while type(p) != float:  # обработка исключений
    try:
        p = float(p)
    except ValueError:
        print("Неправильно ввели!")
        p = input("Введите цену за 1 кг конфет: ")

x = 0.1
while x <= 1.0:
    print(round(x, 1), "кг =", p * x)
    x = round(x + 0.1, 1)