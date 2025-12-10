# Дано целое число N (> 0). Перевернуть число, используя // и %

n = input("Введите число N (>0): ")

while type(n) != int:  # обработка исключений
    try:
        n = int(n)
    except ValueError:
        print("Неправильно ввели!")
        n = input("Введите число N (>0): ")

rev = 0
while n > 0:
    rev = rev * 10 + (n % 10)
    n //= 10

print("Перевернутое число:", rev)