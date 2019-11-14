import tkinter as tk
from tkinter import font as tkfont
import Contact_book as cb

root = tk.Tk()
root.title("ADDRESS-BOOK")

canvas = tk.Canvas(root, height=600, width=800)
canvas.pack()

f1 = tk.Frame(canvas, bg="#373737", bd=5)
f1.place(relwidth=0.25, relheight=1)

textentry1 = tk.Entry(f1, width=20, bg="#ffffff")
textentry1.insert(0, "Enter Name")
textentry1.place(relx=0.039, rely=0.04, relwidth=0.925, relheight=0.035)

lbx = tk.Listbox(f1,background="#373737",fg="white")
lbx.place(relx=0.039, rely=0.125, relwidth=0.925, relheight=0.9)
lbx.config(borderwidth=0)

sbr = tk.Scrollbar(lbx)
sbr.pack(side="right", fill="y")

sbr.config(command=lbx.yview)
lbx.config(yscrollcommand=sbr.set)

for data in range(100):
    lbx.insert(data,"Sample data"+str(data+1))

f2 = tk.Frame(canvas, bg="#2a2a2a", bd=5)
f2.place(relx = 0.25,relwidth=0.75, relheight=1)

root.mainloop()
