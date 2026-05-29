# Вариант 4.
# В последовательности на n целых чисел умножить элементы до n-1 на элемент n.

import random

try:
    n = int(input("Введите количество элементов последовательности (n > 1): "))
    if n <= 1:
        raise ValueError("Количество элементов должно быть больше 1.")
        
    initial_sequence = [random.randint(1, 10) for _ in range(n)]
    print(f"Исходная последовательность: {initial_sequence}")
    
    last_element = initial_sequence[-1]
    
    result_sequence = [initial_sequence[i] * last_element for i in range(n - 1)] + [last_element]
    
    print(f"Последний элемент (n): {last_element}")
    print(f"Результирующая последовательность: {result_sequence}")

except ValueError as e:
    print(f"Ошибка ввода данных: {e}")
except Exception as e:
    print(f"Произошла непредвиденная ошибка: {e}")
