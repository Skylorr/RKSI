# Вариант 4.
# В квадратной матрице все элементы, не лежащие на главной диагонали увеличить в
# 2 раза.

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print("Исходная квадратная матрица:")
for row in matrix:
    print(row)

size = len(matrix)
updated_matrix = [
    [matrix[i][j] if i == j else matrix[i][j] * 2 for j in range(size)]
    for i in range(size)
]

print("\nРезультирующая матрица:")
for row in updated_matrix:
    print(row)
