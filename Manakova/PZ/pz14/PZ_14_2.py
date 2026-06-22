# Вариант 4.
# Разработать программу с применением пакета tk, взяв в качестве условия одну
# любую задачу из ПЗ № 1 – 9.

import tkinter as tk

def check_max():
    try:
        num1 = float(entry_1.get())
        num2 = float(entry_2.get())
        
        if num1 > num2:
            result_label.config(text=f"Максимальное число: {num1}", fg="green")
        elif num2 > num1:
            result_label.config(text=f"Максимальное число: {num2}", fg="green")
        else:
            result_label.config(text="Числа равны", fg="blue")
            
    except ValueError:
        result_label.config(text="Ошибка! Введите корректные числа", fg="red")

root = tk.Tk()
root.title("Практическая 14 — Задание 2")
root.geometry("400x250")
root.resizable(False, False)

main_frame = tk.Frame(root, padx=20, pady=20)
main_frame.pack(fill=tk.BOTH, expand=True)

title = tk.Label(main_frame, text="Поиск максимального числа", font=("Arial", 12, "bold"))
title.pack(pady=(0, 15))

frame_input = tk.Frame(main_frame)
frame_input.pack(fill=tk.X, pady=5)

lbl_1 = tk.Label(frame_input, text="Первое число:", font=("Arial", 10))
lbl_1.pack(side=tk.LEFT, padx=(0, 10))
entry_1 = tk.Entry(frame_input, font=("Arial", 10), width=10)
entry_1.pack(side=tk.LEFT, expand=True, fill=tk.X)

frame_input2 = tk.Frame(main_frame)
frame_input2.pack(fill=tk.X, pady=10)

lbl_2 = tk.Label(frame_input2, text="Второе число:", font=("Arial", 10))
lbl_2.pack(side=tk.LEFT, padx=(0, 10))
entry_2 = tk.Entry(frame_input2, font=("Arial", 10), width=10)
entry_2.pack(side=tk.LEFT, expand=True, fill=tk.X)

btn_calc = tk.Button(main_frame, text="Найти максимальное", command=check_max, font=("Arial", 10, "bold"), bg="#d1d1d1")
btn_calc.pack(pady=10, fill=tk.X)

result_label = tk.Label(main_frame, text="Результат отобразится здесь", font=("Arial", 10, "italic"))
result_label.pack(pady=5)

root.mainloop()
