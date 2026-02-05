import tkinter as tk

def save():
    msg = f"Ім'я: {en_name.get()}\nСтать: {var_sex.get()}" if var_agree.get() else "Потрібна згода!"
    lbl_res.config(text=msg, fg="black" if var_agree.get() else "red")

root = tk.Tk()

tk.Label(root, text="Ім'я:").grid(row=0, column=0)
en_name = tk.Entry(root); en_name.grid(row=0, column=1)

var_sex = tk.StringVar(value="Чол")
tk.Label(root, text="Стать:").grid(row=1, column=0)
tk.Radiobutton(root, text="Чол", variable=var_sex, value="Чол").grid(row=1, column=1, sticky="w")
tk.Radiobutton(root, text="Жін", variable=var_sex, value="Жін").grid(row=2, column=1, sticky="w")

var_agree = tk.BooleanVar()
tk.Checkbutton(root, text="Погоджуюсь", variable=var_agree).grid(row=3, columnspan=2)

tk.Button(root, text="Зберегти", command=save).grid(row=4, columnspan=2)
lbl_res = tk.Label(root); lbl_res.grid(row=5, columnspan=2)

root.mainloop()