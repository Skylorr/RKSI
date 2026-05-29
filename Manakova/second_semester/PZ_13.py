# Вариант 4.
# В исходном текстовом файле (hotline.txt) после фразы «Горячая линия» добавить
# фразу «Министерства образования Ростовской области», посчитать количество
# произведённых добавлений. Сколько номеров телефонов заканчивается на «03»,
# «50». Вывести номера телефонов горячих линий, связанных с ЕГЭ/ГИА.

import re


def process_hotline_data():
    with open("hotline.txt", "r", encoding="utf-8") as file:
        content = file.read()

    file.seek(0)
    lines = file.readlines()

    modified_content, replacement_count = re.subn(
        r"(Горячая линия)",
        r"\1 Министерства образования Ростовской области",
        content,
    )

    with open("hotline_modified.txt", "w", encoding="utf-8") as file_out:
        file_out.write(modified_content)

    all_numbers = re.findall(r"[0-9]+", content)
    ends_with_03_or_50 = [
        num for num in all_numbers if num.endswith("03") or num.endswith("50")
    ]
    count_special_numbers = len(ends_with_03_or_50)

    ege_gia_numbers = []
    for line in lines:
        if re.search(r"ЕГЭ|ГИА", line, re.I):
            numbers_in_line = re.findall(r"[0-9]+", line)
            ege_gia_numbers.extend(numbers_in_line)

    print(f"Количество произведенных добавлений фразы: {replacement_count}")
    print(f"Количество номеров, заканчивающихся на '03' или '50': {count_special_numbers}")
    print("Номера телефонов горячих линий, связанных с ЕГЭ/ГИА:")
    for num in ege_gia_numbers:
        print(num)


if __name__ == "__main__":
    process_hotline_data()
