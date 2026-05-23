# В квадратной матрице все элементы, не лежащие на главной диагонали увеличить в 2 раза.

import random


def process_matrix_diagonal():
    size = 4
    matrix = [[random.randint(1, 9) for _ in range(size)] for _ in range(size)]

    print("Исходная квадратная matrix:")
    for row in matrix:
        print(row)

    updated_matrix = [
        [
            matrix[i][j] if i == j else matrix[i][j] * 2
            for j in range(size)
        ]
        for i in range(size)
    ]

    print("\nРезультирующая matrix:")
    for row in updated_matrix:
        print(row)


if __name__ == "__main__":
    process_matrix_diagonal()
