# Если в матрице имеются положительные элементы, то вывести TRUE, иначе FALSE.

matrix = [[-1, -2, -3], [-4, 5, -6], [-7, -8, 0]]

print("Исходная матрица:")
for row in matrix:
    print(row)

has_positive = any(element > 0 for row in matrix for element in row)

print(f"\nРезультат проверки (наличие положительных элементов): {has_positive}")
