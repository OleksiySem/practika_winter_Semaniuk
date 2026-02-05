import tkinter as tk

class MainWindow(tk.Tk):
    def __init__(self, process_callback):
        super().__init__()

        self.title("Мій Python Проект")
        self.geometry("400x250")
        self.process_callback = process_callback

        self._create_widgets()

    def _create_widgets(self):
        self.label_info = tk.Label(self, text="Введіть текст для обробки:", font=("Arial", 12))
        self.label_info.pack(pady=10)

        self.entry = tk.Entry(self, font=("Arial", 14), width=30)
        self.entry.pack(pady=5)

        self.btn_run = tk.Button(self, text="Обробити", command=self.on_click, bg="#4CAF50", fg="white")
        self.btn_run.pack(pady=15)

        self.label_result = tk.Label(self, text="Результат буде тут", font=("Arial", 12, "bold"), fg="blue")
        self.label_result.pack(pady=10)

    def on_click(self):
        user_input = self.entry.get()

        result = self.process_callback(user_input)

        self.label_result.config(text=f"Результат: {result}")
    def run(self):
        self.mainloop()