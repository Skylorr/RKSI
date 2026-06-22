# Вариант 4.
# Если в матрице имеются положительные элементы, то вывести TRUE, иначе FALSE.

import random

try:
    rows = int(input("Введите количество строк матрицы: "))
    cols = int(input("Введите количество столбцов матрицы: "))
    if rows <= 0 or cols <= 0:
        raise ValueError
        
    matrix = [[random.randint(-10, 5) for _ in range(cols)] for _ in range(rows)]
    
    print("\nИсходная матрица:")
    for row in matrix:
        print(row)
        
    has_positive = any(element > 0 for row in matrix for element in row)
    
    print(f"\nРезультат проверки (наличие положительных элементов): {has_positive}")

except ValueError:
    print("Ошибка: введены некорректные размеры матрицы.")
