# Дан словарь с четным количеством элементов. Найти суммы значений элементов
# первой и второй половин с использованием функции. Результаты вывести на экран.

def calculate_half_sums(data_dict):
    items = list(data_dict.items())
    half_size = len(items) // 2

    first_half = items[:half_size]
    second_half = items[half_size:]

    sum_first = sum(val for key, val in first_half)
    sum_second = sum(val for key, val in second_half)

    return sum_first, sum_second


my_dict = {"a": 10, "b": 20, "c": 30, "d": 40, "e": 50, "f": 60}
print(f"Исходный словарь: {my_dict}")

first_sum, second_sum = calculate_half_sums(my_dict)
print(f"Сумма значений первой половины: {first_sum}")
print(f"Сумма значений второй половины: {second_sum}")
