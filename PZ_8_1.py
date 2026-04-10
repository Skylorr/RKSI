#Найдите ключ с минимальным значением в sample_dict = {'Physics': 82, 'Math': 65,'history': 75}

sample_dict = {'Physics': 82, 'Math': 65, 'history': 75}

min_key = min(sample_dict, key=sample_dict.get)
print('Ключ с минимальным значением:', min_key)
print('Минимальное значение:', sample_dict[min_key])

# Исходный словарь
sample_dict = {
    'Physics': 82,
    'Math': 65,
    'history': 75
}

print(f"Исходный словарь: {sample_dict}")

# Находим ключ с минимальным значением
# Функция min принимает словарь и аргумент key, 
# который указывает, что сравнивать нужно значения (get)
min_key = min(sample_dict, key=sample_dict.get)

print(f"Ключ с минимальным значением: {min_key}")
