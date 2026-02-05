import tkinter as tk

def calc(op):
    try:
        n1, n2 = float(e1.get().replace(',', '.')), float(e2.get().replace(',', '.'))

        res = n1 + n2 if op == '+' else n1 - n2 if op == '-' else n1 * n2 if op == '*' else n1 / n2

        lbl_res['text'] = f"Результат: {int(res) if res.is_integer() else round(res, 4)}"
        lbl_res['fg'] = "black"
    except ZeroDivisionError:
        lbl_res.config(text="Помилка: ділення на 0", fg="red")
    except ValueError:
        lbl_res.config(text="Помилка: введіть числа", fg="red")

root = tk.Tk()
root.title("Калькулятор")
root.geometry("250x200")

e1 = tk.Entry(root);
e1.pack(pady=5)
e2 = tk.Entry(root);
e2.pack(pady=5)

frame = tk.Frame(root)
frame.pack(pady=5)
for op in ['+', '-', '*', '/']:
    tk.Button(frame, text=op, width=5, command=lambda o=op: calc(o)).pack(side='left', padx=2)
lbl_res = tk.Label(root, text="Чекаю введення...")
lbl_res.pack(pady=10)

root.mainloop()