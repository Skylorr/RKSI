# Вариант 4.
# Составить генератор (yield), который выводит из строки только буквы.

def letter_generator(input_string):
    for char in input_string:
        if char.isalpha():
            yield char


source_text = "PyCharm Community 2026! Лабораторная работа №11."
print(f"Исходная строка: '{source_text}'")

gen = letter_generator(source_text)
result_text = "".join(gen)
print(f"Результат работы генератора: '{result_text}'")
