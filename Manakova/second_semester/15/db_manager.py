import sqlite3

DB_NAME = "library.db"


def init_db():
    try:
        with sqlite3.connect(DB_NAME) as conn:
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


def display_all():
    try:
        with sqlite3.connect(DB_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Catalog")
            return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Ошибка вывода: {e}")
        return []


def search_books(choice, value):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        if choice == "1":
            cursor.execute("SELECT * FROM Catalog WHERE genre = ?", (value,))
        elif choice == "2":
            cursor.execute("SELECT * FROM Catalog WHERE author LIKE ?", (f"%{value}%",))
        elif choice == "3":
            cursor.execute("SELECT * FROM Catalog WHERE year > ?", (int(value),))
        return cursor.fetchall()


def update_books(choice, val1, val2):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        if choice == "1":
            cursor.execute("UPDATE Catalog SET annotation = ? WHERE id = ?", (val1, int(val2)))
        elif choice == "2":
            cursor.execute("UPDATE Catalog SET series = ? WHERE author = ?", (val1, val2))
        elif choice == "3":
            cursor.execute("UPDATE Catalog SET country = ? WHERE genre = ?", (val1, val2))
        conn.commit()
        return cursor.rowcount


def delete_books(choice, value):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        if choice == "1":
            cursor.execute("DELETE FROM Catalog WHERE id = ?", (int(value),))
        elif choice == "2":
            cursor.execute("DELETE FROM Catalog WHERE author = ?", (value,))
        elif choice == "3":
            cursor.execute("DELETE FROM Catalog WHERE year < ?", (int(value),))
        conn.commit()
        return cursor.rowcount
