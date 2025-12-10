wl = input("Введите длину волны (нм): ")

while type(wl) != float:
    try:
        wl = float(wl)
    except ValueError:
        print("Неправильно ввели!")
        wl = input("Введите длину волны (нм): ")

if wl <= 450:
    print("Фиолетовый")
elif 450 < wl <= 480:
    print("Синий")
elif 480 < wl <= 510:
    print("Сине-зелёный")
elif 510 < wl <= 550:
    print("Зелёный")
elif 550 < wl <= 570:
    print("Жёлто-зелёный")
elif 570 < wl <= 590:
    print("Жёлтый")
elif 590 < wl <= 630:
    print("Оранжевый")
elif wl > 630:
    print("Красный")
else:
    print("Не попадает в диапазон видимого света")