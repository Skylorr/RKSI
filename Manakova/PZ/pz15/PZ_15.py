# Вариант 4.
# Приложение БИБЛИОТЕКА для автоматизированного контроля литературных
# источников в библиотеке. БД должна содержать таблицу Каталог с информацией о книгах
# и следующей структурой записи: Код книги, Жанр, Страна издания, Серия, Автор,
# Название книги, Год выпуска, Аннотация.

import sqlite3

def init_db():
    try:
        with sqlite3.connect("library.db") as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS Catalog (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    genre TEXT NOT NULL,
                    country TEXT NOT NULL,
                    series TEXT,
                    author TEXT NOT NULL,
                    title TEXT NOT NULL,
                    year INTEGER NOT NULL,
                    annotation TEXT
                )
            """)
            
            cursor.execute("SELECT COUNT(*) FROM Catalog")
            if cursor.fetchone()[0] == 0:
                sample_books = [
                    ('Фэнтези', 'Великобритания', 'Гарри Поттер', 'Дж.К. Роулинг', 'Гарри Поттер и Философский камень', 1997, 'Книга о мальчике, который выжил.'),
                    ('Фэнтези', 'Великобритания', 'Гарри Поттер', 'Дж.К. Роулинг', 'Гарри Поттер и Тайная комната', 1998, 'Второй год обучения в Хогвартсе.'),
                    ('Фэнтези', 'Великобритания', 'Властелин колец', 'Дж.Р.Р. Толкин', 'Братство Кольца', 1954, 'Путешествие Фродо начинается.'),
                    ('Фантастика', 'США', 'Дюна', 'Фрэнк Герберт', 'Дюна', 1965, 'История о песчаной планете Арракис.'),
                    ('Детектив', 'Великобритания', 'Шерлок Холмс', 'Артур Конан Дойл', 'Этюд в багровых тонах', 1887, 'Первое появление Холмса и Ватсона.'),
                    ('Классика', 'Россия', 'Нет', 'Лев Толстой', 'Война и мир', 1869, 'Эпопея о русском обществе в эпоху войн.'),
                    ('Классика', 'Россия', 'Нет', 'Федор Достоевский', 'Преступление и наказание', 1866, 'Роман о психологических муках Раскольникова.'),
                    ('Фантастика', 'Россия', 'Метро', 'Дмитрий Глуховский', 'Метро 2033', 2005, 'Жизнь людей в московском метро после катастрофы.'),
                    ('Антиутопия', 'Великобритания', 'Нет', 'Джордж Оруэлл', '1984', 1949, 'Роман о тоталитарном государстве.'),
                    ('Фэнтези', 'Польша', 'Ведьмак', 'Анджей Сапковский', 'Последнее желание', 1993, 'Приключения ведьмака Геральта из Ривии.')
                ]
                cursor.executemany("""
                    INSERT INTO Catalog (genre, country, series, author, title, year, annotation)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                """, sample_books)
                conn.commit()
    except sqlite3.Error as e:
        print(f"Ошибка БД: {e}")

def search_books():
    print("\n[ПОИСК] Выберите условие:")
    print("1. Поиск по жанру")
    print("2. Поиск по автору")
    print("3. Поиск книг, выпущенных после заданного года")
    choice = input("Ваш выбор: ")
    
    try:
        with sqlite3.connect("library.db") as conn:
            cursor = conn.cursor()
            if choice == "1":
                genre = input("Введите жанр: ")
                cursor.execute("SELECT * FROM Catalog WHERE genre = ?", (genre,))
            elif choice == "2":
                author = input("Введите автора: ")
                cursor.execute("SELECT * FROM Catalog WHERE author LIKE ?", (f"%{author}%",))
            elif choice == "3":
                year = int(input("Введите год: "))
                cursor.execute("SELECT * FROM Catalog WHERE year > ?", (year,))
            else:
                print("Неверный выбор.")
                return
                
            rows = cursor.fetchall()
            if rows:
                for row in rows:
                    print(f"ID: {row[0]} | {row[4]} - {row[5]} ({row[6]} г.) | Жанр: {row[1]} | Страна: {row[2]}")
            else:
                print("Книги не найдены.")
    except (sqlite3.Error, ValueError) as e:
        print(f"Ошибка при поиске: {e}")

def update_books():
    print("\n[РЕДАКТИРОВАНИЕ] Выберите условие:")
    print("1. Изменить аннотацию по ID книги")
    print("2. Изменить серию для конкретного автора")
    print("3. Обновить страну издания для всех книг определенного жанра")
    choice = input("Ваш choice: ")
    
    try:
        with sqlite3.connect("library.db") as conn:
            cursor = conn.cursor()
            if choice == "1":
                book_id = int(input("Введите ID книги: "))
                new_ann = input("Введите новую аннотацию: ")
                cursor.execute("UPDATE Catalog SET annotation = ? WHERE id = ?", (new_ann, book_id))
            elif choice == "2":
                author = input("Введите имя автора: ")
                new_series = input("Введите новую серию: ")
                cursor.execute("UPDATE Catalog SET series = ? WHERE author = ?", (new_series, author))
            elif choice == "3":
                genre = input("Введите жанр: ")
                new_country = input("Введите новую страну: ")
                cursor.execute("UPDATE Catalog SET country = ? WHERE genre = ?", (new_country, genre))
            else:
                print("Неверный выбор.")
                return
                
            conn.commit()
            print(f"Успешно обновлено строк: {cursor.rowcount}")
    except (sqlite3.Error, ValueError) as e:
        print(f"Ошибка при обновлении: {e}")

def delete_books():
    print("\n[УДАЛЕНИЕ] Выберите условие:")
    print("1. Удалить книгу по конкретному ID")
    print("2. Удалить все книги определенного автора")
    print("3. Удалить старые книги (до указанного года выпуска)")
    choice = input("Ваш выбор: ")
    
    try:
        with sqlite3.connect("library.db") as conn:
            cursor = conn.cursor()
            if choice == "1":
                book_id = int(input("Введите ID книги для удаления: "))
                cursor.execute("DELETE FROM Catalog WHERE id = ?", (book_id,))
            elif choice == "2":
                author = input("Введите автора для удаления его книг: ")
                cursor.execute("DELETE FROM Catalog WHERE author = ?", (author,))
            elif choice == "3":
                year = int(input("Удалить книги до какого года: "))
                cursor.execute("DELETE FROM Catalog WHERE year < ?", (year,))
            else:
                print("Неверный выбор.")
                return
                
            conn.commit()
            print(f"Успешно удалено строк: {cursor.rowcount}")
    except (sqlite3.Error, ValueError) as e:
        print(f"Ошибка при удалении: {e}")

def display_all():
    try:
        with sqlite3.connect("library.db") as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Catalog")
            rows = cursor.fetchall()
            print("\n=== ВЕСЬ КАТАЛОГ КНИГ ===")
            for row in rows:
                print(f"ID: {row[0]} | Жанр: {row[1]} | Страна: {row[2]} | Серия: {row[3]} | Автор: {row[4]} | Название: {row[5]} | Год: {row[6]} | Аннотация: {row[7]}")
    except sqlite3.Error as e:
        print(f"Ошибка вывода: {e}")

def main():
    init_db()
    while True:
        print("\n=== МЕНЮ БИБЛИОТЕКИ ===")
        print("1. Показать все книги")
        print("2. Поиск книг (3 варианта запросов)")
        print("3. Редактировать данные (3 варианта запросов)")
        print("4. Удалить данные (3 варианта запросов)")
        print("5. Выход")
        
        choice = input("Выберите действие: ")
        if choice == "1":
            display_all()
        elif choice == "2":
            search_books()
        elif choice == "3":
            update_books()
        elif choice == "4":
            delete_books()
        elif choice == "5":
            break
        else:
            print("Неверный пункт меню.")

if __name__ == "__main__":
    main()
