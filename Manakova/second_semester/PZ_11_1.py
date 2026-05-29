# Вариант 4.
# В последовательности на n целых чисел умножить элементы до n-1 на элемент n.

initial_sequence = [12, 3.85, 5, -4, 7]
print(f"Исходная последовательность: {initial_sequence}")

last_element = initial_sequence[-1]
print(f"Последний элемент: {last_element}")

result_sequence = [x * last_element for x in initial_sequence[:-1]] + [
    last_element
]
print(f"Результирующая последовательность: {result_sequence}")
