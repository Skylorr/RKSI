# Вариант 4.
# 1. Средствами языка Python сформировать текстовый файл (.txt), содержащий
# последовательность из целых положительных и отрицательных чисел. Сформировать
# новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
# обработку элементов:
# Исходные данные:
# Количество элементов:
# Минимальный элемент:
# Элементы, умноженные на первый максимальный элемент:

numbers_string = "15 -3 8 -12 4 20 -7 20"

with open("numbers_input.txt", "w", encoding="utf-8") as file:
    file.write(numbers_string)

with open("numbers_input.txt", "r", encoding="utf-8") as file:
    content = file.read()

numbers = [int(x) for x in content.split()]

total_count = len(numbers)
min_element = min(numbers)
max_element = max(numbers)

multiplied_elements = [x * max_element for x in numbers]
multiplied_string = " ".join(map(str, multiplied_elements))

with open("numbers_output.txt", "w", encoding="utf-8") as file:
    file.write(f"Исходные данные: {content}\n")
    file.write(f"Количество элементов: {total_count}\n")
    file.write(f"Минимальный элемент: {min_element}\n")
    file.write(
        f"Элементы, умноженные на первый максимальный элемент: {multiplied_string}\n"
    )

with open("numbers_output.txt", "r", encoding="utf-8") as file:
    print(file.read())
