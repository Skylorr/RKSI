#Дан словарь с четным количеством элементов. 
#Найти суммы значений элементов первой и второй половин с использованием функции. 
#Результаты вывести на экран.

def half_sums(d):
    values = list(d.values())
    mid = len(values) // 2
    sum_first = sum(values[:mid])
    sum_second = sum(values[mid:])
    return sum_first, sum_second


data = {
    'a': 10,
    'b': 20,
    'c': 30,
    'd': 40
}

s1, s2 = half_sums(data)

print('Сумма первой половины:', s1)
print('Сумма второй половины:', s2)
