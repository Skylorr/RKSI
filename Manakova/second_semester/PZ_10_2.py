# Вариант 4.
# Из предложенного текстового файла (text18-4.txt) вывести на экран его содержимое,
# количество символов, принадлежащих к группе букв. Сформировать новый файл, в
# который поместить текст в стихотворной форме предварительно заменив символы верхнего
# регистра на нижний.

import os

input_poem_file = "text18-4.txt"
output_poem_file = "text18-4_lower.txt"

if not os.path.exists(input_poem_file):
    sample_text = (
        "Буря мглою небо кроет,\n"
        "Вихри снежные крутя;\n"
        "То, как зверь, она завоет,\n"
        "То заплачет, как дитя."
    )
    with open(input_poem_file, "w", encoding="utf-8") as f:
        f.write(sample_text)

try:
    print("=== Содержимое исходного файла ===")
    letter_count = 0
    lines = []
    
    with open(input_poem_file, "r", encoding="utf-8") as f_in:
        for line in f_in:
            print(line, end="")
            lines.append(line)
            for char in line:
                if char.isalpha():
                    letter_count += 1
                    
    print(f"\n\nКоличество символов, принадлежащих к группе букв: {letter_count}")
    print("-" * 40)
    
    lower_lines = [line.lower() for line in lines]
    
    with open(output_poem_file, "w", encoding="utf-8") as f_out:
        f_out.writelines(lower_lines)
        
    print(f"Новый файл '{output_poem_file}' успешно сформирован.")
    print("\n=== Содержимое нового файла ===")
    with open(output_poem_file, "r", encoding="utf-8") as f_check:
        print(f_check.read())

except FileNotFoundError:
    print(f"Ошибка: Файл {input_poem_file} не найден.")
except Exception as e:
    print(f"Произошла ошибка при обработке файла: {e}")
