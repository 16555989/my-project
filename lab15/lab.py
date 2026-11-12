
import tkinter as tk
from tkinter import messagebox
from tabulation import tabulate

def show_graph():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())

        if a >= b:
            messagebox.showerror("Помилка", "Ліва межа повинна бути меншою за праву")
            return

        data = tabulate(a, b)

        window = tk.Toplevel(root)
        window.title("Графік функції")
        window.geometry("600x400")

        canvas = tk.Canvas(window, width=580, height=360, bg="white")
        canvas.pack(padx=10, pady=10)

        xs = [p[0] for p in data]
        ys = [p[1] for p in data]

        xmin, xmax = min(xs), max(xs)
        ymin, ymax = min(ys), max(ys)

        if ymin == ymax:
            ymax += 1

        margin = 30
        width = 580 - 2 * margin
        height = 360 - 2 * margin

        points = []

        for x, y in data:
            px = margin + (x - xmin) / (xmax - xmin) * width
            py = 360 - margin - (y - ymin) / (ymax - ymin) * height
            points.extend([px, py])

        canvas.create_line(points, fill="blue", width=2)

    except ValueError:
        messagebox.showerror("Помилка", "Введіть числові межі")

root = tk.Tk()
root.title("Графік функції")
root.geometry("300x220")
root.configure(bg="blue")

tk.Label(root, text="Ліва межа:", bg="blue").grid(row=0, column=0, padx=5, pady=10)
entry_a = tk.Entry(root)
entry_a.grid(row=0, column=1)

tk.Label(root, text="Права межа:", bg="blue").grid(row=1, column=0, padx=5, pady=10)
entry_b = tk.Entry(root)
entry_b.grid(row=1, column=1)

frame = tk.Frame(root, bg="blue")
frame.grid(row=2, column=0, columnspan=2, pady=15)

tk.Button(frame, text="Побудувати графік", command=show_graph).grid(row=0, column=0)

root.mainloop()
