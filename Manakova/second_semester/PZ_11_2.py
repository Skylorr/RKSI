# Составить генератор (yield), который выводит из строки только буквы.

def letter_generator(input_string):
    for char in input_string:
        if char.isalpha():
            yield char

def run_generator_task():
    print("--- Задача 2: Генератор букв из строки ---")

    source_text = "Python 3.10 - это отличный язык! Год 2026."
    print(f"Исходная строка: '{source_text}'")

    gen = letter_generator(source_text)

    result_letters = "".join(gen)
    print(f"Результат работы генератора (только буквы): '{result_letters}'")

if __name__ == "__main__":
    run_generator_task()
