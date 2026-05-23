#В последовательности на n целых чисел умножить элементы до n-1 на элемент n.

import random

def process_sequence():
    print("--- Задача 1: Умножение элементов на последний элемент ---")

    n = 7
    initial_sequence = [random.randint(1, 10) for _ in range(n)]
    print(f"Исходная последовательность (n = {n}): {initial_sequence}")

    last_element = initial_sequence[-1]
    print(f"Последний элемент (n): {last_element}")

    result_sequence = [
        x * last_element for x in initial_sequence[:-1]
    ] + [last_element]

    print(f"Результирующая последовательность: {result_sequence}\n")


if __name__ == "__main__":
    process_sequence()
