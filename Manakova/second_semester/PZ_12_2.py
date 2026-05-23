# Если в матрице имеются положительные элементы, то вывести TRUE, иначе FALSE.

import random


def check_positive_elements():
    rows, cols = 3, 3
    matrix = [[random.randint(-10, 5) for _ in range(cols)] for _ in range(rows)]

    print("Исходная matrix:")
    for row in matrix:
        print(row)

    has_positive = any(element > 0 for row in matrix for element in row)

    print(f"\nРезультат проверки (наличие положительных элементов): {has_positive}")


if __name__ == "__main__":
    check_positive_elements()
