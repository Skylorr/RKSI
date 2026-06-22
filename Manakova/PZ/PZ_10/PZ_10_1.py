# Вариант 4.
# 1. Средствами языка Python сформировать текстовый файл (.txt), содержащий
# последовательность из целых положительных и отрицательных чисел. Сформировать
# новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
# обработку элементов:
# Исходные данные:
# Количество элементов:
# Минимальный элемент:
# Элементы, умноженные на первый максимальный элемент:

import random

input_filename = "data_v4_1.txt"
output_filename = "result_v4_1.txt"

try:
    random_numbers = [str(random.randint(-50, 50)) for _ in range(10)]
    with open(input_filename, "w", encoding="utf-8") as f_in:
        f_in.write(" ".join(random_numbers))
    print(f"Файл '{input_filename}' успешно создан.")
except IOError as e:
    print(f"Ошибка при создании исходного файла: {e}")

try:
    with open(input_filename, "r", encoding="utf-8") as f_in:
        content = f_in.read()
        
    numbers = [int(x) for x in content.split()]
    
    if not numbers:
        print("Файл пуст!")
    else:
        count_elements = len(numbers)
        min_element = min(numbers)
        max_element = max(numbers)
        
        multiplied_elements = [x * max_element for x in numbers]
        
        with open(output_filename, "w", encoding="utf-8") as f_out:
            f_out.write(f"Исходные данные: {content}\n")
            f_out.write(f"Количество элементов: {count_elements}\n")
            f_out.write(f"Минимальный элемент: {min_element}\n")
            f_out.write(
                f"Элементы, умноженные на первый максимальный элемент ({max_element}): "
                f"{' '.join(map(str, multiplied_elements))}\n"
            )
            
        print(f"Результаты успешно обработаны и записаны в '{output_filename}'.")
        print("\nСодержимое результирующего файла:")
        with open(output_filename, "r", encoding="utf-8") as f_check:
            print(f_check.read())

except FileNotFoundError:
    print(f"Ошибка: Не удалось найти файл {input_filename}")
except ValueError:
    print("Ошибка: В файле содержатся некорректные данные (не числа)")
except Exception as e:
    print(f"Произошла непредвиденная ошибка: {e}")
