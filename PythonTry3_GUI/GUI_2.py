from functools import partial as pto
import tkinter as tk

WARN = "warn"
CRIT = "crit"
REGU = "regu"

SIGNS = {
    "do not enter":CRIT,
    "railroad crossing":WARN,
    "55\nspeed limit":REGU,
    "wrong way":CRIT,
    "meging traffic":WARN,
    "one way":REGU,
    }

critCB = lambda : showerror("Error","Error Button Pressed!")
warnCB = lambda : showwarning("Warning","Warning Button Pressed!")
infoCB = lambda : showinfo("Info", "Info Button Pressed!")

top = tk.Tk()
top.title("Road Signs")
tk.Button(top,text="QUIT",command=top.quit,bg="red",fg="white").pack()

MyButton = pto(tk.Button,top)
CritButton = pto(MyButton,command=critCB,bg="white",fg='red')
WarnButton = pto(MyButton,command=warnCB,bg="goldnrod1")
ReguButton = pto(MyButton,command=infoCB,bg="white")

for eachSign in SIGNS:
    signType = SIGNS[eachSign]
    cmd = '%sButton (text={%r}{%s}).pack(fill=\"x\",expand=True)'.format(signType.title(),eachSign,".upper()" if signType == CRIT else ".title()")
    eval(cmd)
top.mainloop()