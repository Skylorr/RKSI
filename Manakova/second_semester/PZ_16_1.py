# Вариант 4.
# Создайте класс «Календарь», который имеет атрибуты год, месяц и день. Добавьте
# методы для определения дня недели, проверки на високосный год и определения
# количества дней в месяце.

import datetime
import calendar


class MyCalendar:

    def __init__(self, year: int, month: int, day: int):
        try:
            datetime.date(year, month, day)
            self.year = year
            self.month = month
            self.day = day
        except ValueError:
            raise ValueError("Ошибка: введена некорректная дата.")

    def get_day_of_week(self) -> str:
        days = [
            "Понедельник",
            "Вторник",
            "Среда",
            "Четверг",
            "Пятница",
            "Суббота",
            "Воскресенье",
        ]
        dt = datetime.date(self.year, self.month, self.day)
        return days[dt.weekday()]

    def is_leap_year(self) -> bool:
        return calendar.isleap(self.year)

    def get_days_in_month(self) -> int:
        return calendar.monthrange(self.year, self.month)[1]


try:
    print("--- Тест 1: Валидная дата ---")
    my_date = MyCalendar(2026, 5, 30)
    print(f"Дата: {my_date.day}.{my_date.month}.{my_date.year}")
    print(f"День недели: {my_date.get_day_of_week()}")
    print(f"Високосный год: {my_date.is_leap_year()}")
    print(f"Дней в этом месяце: {my_date.get_days_in_month()}")

    print("\n--- Тест 2: Високосный год ---")
    leap_date = MyCalendar(2024, 2, 15)
    print(f"Дата: {leap_date.day}.{leap_date.month}.{leap_date.year}")
    print(f"Високосный год: {leap_date.is_leap_year()}")
    print(f"Дней в феврале 2024: {leap_date.get_days_in_month()}")

    print("\n--- Тест 3: Проверка ошибки ---")
    bad_date = MyCalendar(2025, 2, 30)

except ValueError as e:
    print(e)
