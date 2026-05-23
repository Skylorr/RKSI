# Составить генератор (yield), который выводит из строки только буквы.

def letter_generator(input_string):
    for char in input_string:
        if char.isalpha():
            yield char


def run_generator_task():
    source_text = "PyCharm Community 2026! Лабораторная работа №11."
    print(f"Исходная строка: '{source_text}'")

    gen = letter_generator(source_text)
    result_text = "".join(gen)
    print(f"Результат работы генератора: '{result_text}'")


if __name__ == "__main__":
    run_generator_task()
