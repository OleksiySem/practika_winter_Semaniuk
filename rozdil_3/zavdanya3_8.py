import tkinter as tk
from tkinter import colorchooser, messagebox

def draw(event):
    global obj
    x, y = event.x, event.y
    if str(event.type) == '4':
        app.sx, app.sy = x, y
        obj = cv.create_line(x, y, x, y, fill=app.clr) if tool.get() == "L" else cv.create_oval(x, y, x, y, outline=app.clr)
    else:
        cv.coords(obj, app.sx, app.sy, x, y)

def set_clr(): app.clr = colorchooser.askcolor()[1] or app.clr

app = tk.Tk()
app.title("Графіка")
app.clr, tool = "black", tk.StringVar(value="L")

btn_frame = tk.Frame(app)
btn_frame.pack()

tk.Radiobutton(btn_frame, text="Лінія", variable=tool, value="L").pack(side=tk.LEFT)
tk.Radiobutton(btn_frame, text="Коло", variable=tool, value="C").pack(side=tk.LEFT)
tk.Button(btn_frame, text="Колір", command=set_clr).pack(side=tk.LEFT)
tk.Button(btn_frame, text="Очистити", command=lambda: cv.delete("all")).pack(side=tk.LEFT)
tk.Button(btn_frame, text="Зберегти", command=lambda: cv.postscript(file="img.ps")).pack(side=tk.LEFT)

cv = tk.Canvas(app, width=600, height=400, bg="white")
cv.pack()
cv.bind("<Button-1>", draw)
cv.bind("<B1-Motion>", draw)

app.mainloop()