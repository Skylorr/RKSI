# Вариант 4.
# Составить генератор (yield), который выводит из строки только буквы.

def extract_letters(input_string):
    for char in input_string:
        if char.isalpha():
            yield char

try:
    user_string = input("Введите строку: ")
    print(f"Результат: {''.join(extract_letters(user_string))}")
except Exception:
    print("Ошибка")
