# Вариант 4.
# В соответствии с номером варианта перейти по ссылке на прототип. Реализовать
# его в IDE PyCharm Community с применением пакета tk. Получить интерфейс максимально
# приближенный к оригиналу (см. таблицу 1).

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Обработка формы")
root.geometry("550x600")
root.resizable(False, False)

main_frame = tk.Frame(root, padx=20, pady=20)
main_frame.pack(fill=tk.BOTH, expand=True)

title_label = tk.Label(
    main_frame, 
    text="Форма регистрации пользователя", 
    font=("Arial", 14, "bold")
)
title_label.pack(pady=(0, 20))

form_border = tk.LabelFrame(main_frame, padx=15, pady=15)
form_border.pack(fill=tk.BOTH, expand=True)

grid_frame = tk.Frame(form_border)
grid_frame.pack(fill=tk.X)

grid_frame.columnconfigure(1, weight=1)

labels = ["Ваше имя:", "Пароль:", "Возраст:"]
entries = []

for i, text in enumerate(labels):
    lbl = tk.Label(grid_frame, text=text, anchor="w", font=("Arial", 10))
    lbl.grid(row=i, column=0, sticky="w", pady=8, padx=10)
    
    show_char = "*" if text == "Пароль:" else None
    entry = tk.Entry(grid_frame, show=show_char, font=("Arial", 10))
    entry.grid(row=i, column=1, sticky="ew", pady=8)
    entries.append(entry)

gender_label = tk.Label(grid_frame, text="Пол:", anchor="w", font=("Arial", 10))
gender_label.grid(row=3, column=0, sticky="w", pady=8)

gender_var = tk.StringVar(value="Мужской")
gender_frame = tk.Frame(grid_frame)
gender_frame.grid(row=3, column=1, sticky="w", pady=8)

rb_male = tk.Radiobutton(gender_frame, text="Мужской", variable=gender_var, value="Мужской", font=("Arial", 10))
rb_male.pack(side=tk.LEFT, padx=(0, 40))
rb_female = tk.Radiobutton(gender_frame, text="Женский", variable=gender_var, value="Женский", font=("Arial", 10))
rb_female.pack(side=tk.LEFT)

hobby_label = tk.Label(grid_frame, text="Ваши увлечения:", anchor="w", font=("Arial", 10))
hobby_label.grid(row=4, column=0, sticky="w", pady=8)

hobby_frame = tk.Frame(grid_frame)
hobby_frame.grid(row=4, column=1, sticky="w", pady=8)

music_var = tk.BooleanVar()
video_var = tk.BooleanVar()
draw_var = tk.BooleanVar()

cb_music = tk.Checkbutton(hobby_frame, text="Музыка", variable=music_var, font=("Arial", 10))
cb_music.pack(side=tk.LEFT, padx=(0, 20))
cb_video = tk.Checkbutton(hobby_frame, text="Видео", variable=video_var, font=("Arial", 10))
cb_video.pack(side=tk.LEFT, padx=(0, 20))
cb_draw = tk.Checkbutton(hobby_frame, text="Рисование", variable=draw_var, font=("Arial", 10))
cb_draw.pack(side=tk.LEFT)

country_label = tk.Label(grid_frame, text="Ваша страна:", anchor="w", font=("Arial", 10))
country_label.grid(row=5, column=0, sticky="w", pady=8)

country_combo = ttk.Combobox(grid_frame, state="readonly", font=("Arial", 10))
country_combo.grid(row=5, column=1, sticky="ew", pady=8)

city_label = tk.Label(grid_frame, text="Ваш город:", anchor="w", font=("Arial", 10))
city_label.grid(row=6, column=0, sticky="w", pady=8)

city_combo = ttk.Combobox(grid_frame, state="readonly", font=("Arial", 10))
city_combo.grid(row=6, column=1, sticky="ew", pady=8)

about_label = tk.Label(grid_frame, text="Кратко о себе:", anchor="w", font=("Arial", 10))
about_label.grid(row=7, column=0, sticky="nw", pady=8)

about_text = tk.Text(grid_frame, height=4, font=("Arial", 10))
about_text.grid(row=7, column=1, sticky="ew", pady=8)

captcha_label = tk.Label(form_border, text="Решите пример, запишите результат в поле ниже:", anchor="w", font=("Arial", 10))
captcha_label.pack(anchor="w", pady=(15, 5))

captcha_entry = tk.Entry(form_border, font=("Arial", 10))
captcha_entry.pack(fill=tk.X, pady=(0, 15))

btn_frame = tk.Frame(form_border)
btn_frame.pack(fill=tk.X, side=tk.BOTTOM, pady=5)

btn_cancel = tk.Button(btn_frame, text="Отменить ввод", width=18, font=("Arial", 10))
btn_cancel.pack(side=tk.LEFT, padx=(40, 0))

btn_confirm = tk.Button(btn_frame, text="Данные подтверждаю", width=22, font=("Arial", 10))
btn_confirm.pack(side=tk.RIGHT, padx=(0, 40))

root.mainloop()
