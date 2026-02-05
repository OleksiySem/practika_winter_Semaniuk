import tkinter as tk
from tkinter import messagebox

def create_app():
    root = tk.Tk()
    root.title("Програма вітання")
    root.geometry("300x250")

    def show_greeting():
        info_label.config(text="Вітаю, користувач!", fg="green")

    def clear_text():
        info_label.config(text="")

    def exit_app():
        root.destroy()

    info_label = tk.Label(root, text="", font=("Arial", 14, "bold"))
    info_label.pack(pady=20)

    btn_greet = tk.Button(root, text="Привітати", command=show_greeting, width=15, height=2)
    btn_greet.pack(pady=5)

    btn_clear = tk.Button(root, text="Очистити", command=clear_text, width=15, height=2)
    btn_clear.pack(pady=5)

    btn_exit = tk.Button(root, text="Вийти", command=exit_app, width=15, height=2, bg="#ffcccc")
    btn_exit.pack(pady=20)

    root.mainloop()
if __name__ == "__main__":
    create_app()