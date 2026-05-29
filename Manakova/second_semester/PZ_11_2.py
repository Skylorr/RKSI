# Вариант 4.
# Составить генератор (yield), который выводит из строки только буквы.

def extract_letters(input_string):
    for char in input_string:
        if char.isalpha():
            yield char

try:
    user_string = input("Введите строку, содержащую буквы, цифры или символы: ")
    print(f"Исходная строка: {user_string}")
    
    letters_generator = extract_letters(user_string)
    
    result_list = list(letters_generator)
    
    print(f"Найденные буквы: {result_list}")
    print(f"Результат строкой: {''.join(result_list)}")

except Exception as e:
    print(f"Произошла ошибка при обработке строки: {e}")
