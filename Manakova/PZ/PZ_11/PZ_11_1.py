# Вариант 4.
# В последовательности на n целых чисел умножить элементы до n-1 на элемент n.

import random

try:
    n = int(input("Введите n: "))
    if n <= 1:
        raise ValueError
        
    initial_sequence = [random.randint(1, 10) for _ in range(n)]
    print(f"Исходная: {initial_sequence}")
    
    last_element = initial_sequence[-1]
    result_sequence = [x * last_element for x in initial_sequence[:-1]] + [last_element]
    
    print(f"Результат: {result_sequence}")

except ValueError:
    print("Ошибка ввода")
