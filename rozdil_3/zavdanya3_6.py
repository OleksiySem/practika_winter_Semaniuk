from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.messagebox import askyesnocancel

file_path = None

def save():
    global file_path
    path = file_path or asksaveasfilename(defaultextension=".txt")
    if path:
        file_path = path
        with open(path, "w", encoding="utf-8") as f: f.write(text.get("1.0", END))
        text.edit_modified(False)
        return True
    return False

def open_file():
    if not check_exit(): return
    path = askopenfilename()
    if path:
        global file_path
        file_path = path
        text.delete("1.0", END)
        text.insert("1.0", open(path, encoding="utf-8").read())
        text.edit_modified(False)

def check_exit():
    if text.edit_modified():
        ans = askyesnocancel("Увага", "Зберегти зміни перед виходом?")
        if ans is None: return False
        if ans: return save()
    return True

root = Tk()
root.title("Блокнот")
text = Text(root, undo=True); text.pack(fill=BOTH, expand=1)

m = Menu(root); root.config(menu=m)
fm = Menu(m, tearoff=0); m.add_cascade(label="Файл", menu=fm)
fm.add_command(label="Відкрити", command=open_file)
fm.add_command(label="Зберегти", command=save)
fm.add_command(label="Вийти", command=lambda: root.destroy() if check_exit() else None)

root.protocol("WM_DELETE_WINDOW", lambda: root.destroy() if check_exit() else None)
root.mainloop()