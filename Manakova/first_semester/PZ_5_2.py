# 2
# Функция RectPS — периметр и площадь прямоугольника

def RectPS(x1, y1, x2, y2):
    # локальные переменные
    w = abs(x2 - x1)
    h = abs(y2 - y1)
    P = 2 * (w + h)
    S = w * h
    return P, S

# Ввод координат для трех прямоугольников

def read_float(msg):
    x = input(msg)
    while type(x) != float:
        try:
            x = float(x)
        except ValueError:
            print("Неправильно ввели!")
            x = input(msg)
    return x

print("\nПервый прямоугольник:")
x1 = read_float("x1: ")
y1 = read_float("y1: ")
x2 = read_float("x2: ")
y2 = read_float("y2: ")
P, S = RectPS(x1, y1, x2, y2)
print("Периметр =", P, "Площадь =", S)

print("\nВторой прямоугольник:")
x1 = read_float("x1: ")
y1 = read_float("y1: ")
x2 = read_float("x2: ")
y2 = read_float("y2: ")
P, S = RectPS(x1, y1, x2, y2)
print("Периметр =", P, "Площадь =", S)

print("\nТретий прямоугольник:")
x1 = read_float("x1: ")
y1 = read_float("y1: ")
x2 = read_float("x2: ")
y2 = read_float("x2: ")
P, S = RectPS(x1, y1, x2, y2)
print("Периметр =", P, "Площадь =", S)
