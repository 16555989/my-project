
import tkinter as tk
from tkinter import messagebox

def sort_array():
    try:
        numbers = list(map(int, entry_input.get().split()))

        if not numbers:
            messagebox.showerror("Помилка", "Введіть масив чисел")
            return

        numbers.sort(reverse=True)

        result = " ".join(map(str, numbers))

        entry_result.delete(0, tk.END)
        entry_result.insert(0, result)

        with open("array.txt", "w", encoding="utf-8") as file:
            file.write(result)

    except ValueError:
        messagebox.showerror("Помилка", "Введіть числа через пробіл")

root = tk.Tk()
root.title("Сортування масиву")
root.geometry("400x250")

frame = tk.Frame(root)
frame.pack(pady=15)

tk.Label(frame, text="Введіть масив чисел:").grid(row=0, column=0, pady=10)

entry_input = tk.Entry(frame, width=35)
entry_input.grid(row=1, column=0, padx=10)

tk.Button(
    frame,
    text="Сортувати за спаданням",
    command=sort_array
).grid(row=2, column=0, pady=15)

tk.Label(frame, text="Відсортований масив:").grid(row=3, column=0)

entry_result = tk.Entry(frame, width=35)
entry_result.grid(row=4, column=0, pady=10)

root.mainloop()
