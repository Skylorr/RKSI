# Вариант 4.
# В квадратной матрице все элементы, не лежащие на главной диагонали увеличить в
# 2 раза.

import random

try:
    size = int(input("Введите размер квадратной матрицы (N): "))
    if size <= 0:
        raise ValueError
        
    matrix = [[random.randint(1, 9) for _ in range(size)] for _ in range(size)]
    
    print("\nИсходная квадратная матрица:")
    for row in matrix:
        print(row)
        
    updated_matrix = [
        [matrix[i][j] if i == j else matrix[i][j] * 2 for j in range(size)]
        for i in range(size)
    ]
    
    print("\nРезультирующая матрица:")
    for row in updated_matrix:
        print(row)

except ValueError:
    print("Ошибка: введено некорректное число.")
