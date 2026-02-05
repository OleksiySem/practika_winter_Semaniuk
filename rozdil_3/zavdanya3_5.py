import tkinter as tk
from tkinter import ttk, colorchooser
import json, os

CFG = "config.json"
root = tk.Tk()
root.geometry("300x250")

bg_color = json.load(open(CFG)) if os.path.exists(CFG) else "#f0f0f0"

def set_bg(c):
    if c:
        root.configure(bg=c)
        for tab in tabs: tab.configure(bg=c)
        with open(CFG, 'w') as f: json.dump(c, f)

nb = ttk.Notebook(root)
nb.pack(fill='both', expand=True)

tabs = [tk.Frame(nb) for _ in range(3)]
nb.add(tabs[0], text='Головна'); nb.add(tabs[1], text='Налаштування'); nb.add(tabs[2], text='Про')

tk.Label(tabs[0], text="Введіть дані:", bg=bg_color).pack(pady=5)
tk.Entry(tabs[0]).pack(pady=2)
tk.Button(tabs[0], text="Зберегти", command=lambda: print("Дані введено")).pack(pady=5)

tk.Button(tabs[1], text="Обрати колір", command=lambda: set_bg(colorchooser.askcolor()[1])).pack(pady=20)

tk.Label(tabs[2], text="Автор: Студент\nРік: 2024", bg=bg_color).pack(pady=20)

set_bg(bg_color)
root.mainloop()