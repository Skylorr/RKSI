import db_manager as db


def run_search():
    print("\n[ПОИСК] Выберите условие:")
    print("1. Поиск по жанру")
    print("2. Поиск по автору")
    print("3. Поиск книг, выпущенных после заданного года")
    choice = input("Ваш выбор: ")

    if choice not in ["1", "2", "3"]:
        print("Неверный выбор.")
        return

    try:
        if choice == "1":
            val = input("Введите жанр: ")
        elif choice == "2":
            val = input("Введите автора: ")
        elif choice == "3":
            val = input("Введите год: ")

        rows = db.search_books(choice, val)
        if rows:
            for row in rows:
                print(f"ID: {row[0]} | {row[4]} - {row[5]} ({row[6]} г.) | Жанр: {row[1]} | Страна: {row[2]}")
        else:
            print("Книги не найдены.")
    except (ValueError, Exception) as e:
        print(f"Ошибка при поиске: {e}")


def run_update():
    print("\n[РЕДАКТИРОВАНИЕ] Выберите условие:")
    print("1. Изменить аннотацию по ID книги")
    print("2. Изменить серию для конкретного автора")
    print("3. Обновить страну издания для всех книг определенного жанра")
    choice = input("Ваш выбор: ")

    if choice not in ["1", "2", "3"]:
        print("Неверный выбор.")
        return

    try:
        if choice == "1":
            val2 = input("Введите ID книги: ")
            val1 = input("Введите новую аннотацию: ")
        elif choice == "2":
            val2 = input("Введите имя автора: ")
            val1 = input("Введите новую серию: ")
        elif choice == "3":
            val2 = input("Введите жанр: ")
            val1 = input("Введите новую страну: ")

        count = db.update_books(choice, val1, val2)
        print(f"Успешно обновлено строк: {count}")
    except (ValueError, Exception) as e:
        print(f"Ошибка при обновлении: {e}")


def run_delete():
    print("\n[УДАЛЕНИЕ] Выберите условие:")
    print("1. Удалить книгу по конкретному ID")
    print("2. Удалить все книги определенного автора")
    print("3. Удалить старые книги (до указанного года выпуска)")
    choice = input("Ваш выбор: ")

    if choice not in ["1", "2", "3"]:
        print("Неверный выбор.")
        return

    try:
        if choice == "1":
            val = input("Введите ID книги для удаления: ")
        elif choice == "2":
            val = input("Введите автора для удаления его книг: ")
        elif choice == "3":
            val = input("Удалить книги до какого года: ")

        count = db.delete_books(choice, val)
        print(f"Успешно удалено строк: {count}")
    except (ValueError, Exception) as e:
        print(f"Ошибка при удалении: {e}")


def main():
    db.init_db()
    while True:
        print("\n=== МЕНЮ БИБЛИОТЕКИ ===")
        print("1. Показать все книги")
        print("2. Поиск книг (3 варианта запросов)")
        print("3. Редактировать данные (3 варианта запросов)")
        print("4. Удалить данные (3 варианта запросов)")
        print("5. Выход")

        choice = input("Выберите действие: ")
        if choice == "1":
            rows = db.display_all()
            print("\n=== ВЕСЬ КАТАЛОГ КНИГ ===")
            for row in rows:
                print(f"ID: {row[0]} | Жанр: {row[1]} | Страна: {row[2]} | Серия: {row[3]} | Автор: {row[4]} | Название: {row[5]} | Год: {row[6]} | Аннотация: {row[7]}")
        elif choice == "2":
            run_search()
        elif choice == "3":
            run_update()
        elif choice == "4":
            run_delete()
        elif choice == "5":
            break
        else:
            print("Неверный пункт меню.")


if __name__ == "__main__":
    main()
