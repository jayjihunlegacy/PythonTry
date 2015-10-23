import tkinter as tk

top = tk.Tk();
top.geometry("250x500")

# 1. Label
label = tk.Label(top,text="HELLO world",font="Helvetica -12 bold");
label.pack(fill="y", expand=1)

# 2. Button
quit = tk.Button(top,text="QUIT",command=top.quit,bg="red",fg="white")
quit.pack()

# 3. Scale
def resize(ev=None):
    label.config(font="Helvetica -{} bold".format(scale.get()))

scale = tk.Scale(top, from_=10, to=40, orient="horizontal",command=resize)
scale.set(12)
scale.pack(fill="x",expand=1)

# 4. Canvas
canvas = tk.Canvas()
canvas.create_polygon(((0,0),(100,100),(100,0)))
canvas.pack()

# 5. Entry
entry = tk.Entry()
entry.pack()





tk.mainloop()
