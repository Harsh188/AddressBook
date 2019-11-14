import tkinter as tk
from tkinter import font as tkfont
import Contact_book as cb

root = tk.Tk()
root.title("ADDRESS-BOOK")

canvas = tk.Canvas(root, height=600, width=800)
canvas.pack()

f1 = tk.Frame(root, bg="#373737", bd=5)
f1.place(relwidth=0.25, relheight=1)

textentry = tk.Entry(f1, width=20, bg="#ffffff")
textentry.insert(0, "Enter Name")
textentry.place(relx=0.039, rely=0.04, relwidth=0.925, relheight=0.035)

lbx = tk.Listbox(f1)
lbx.place(relx=0.039, rely=0.125, relwidth=0.925, relheight=0.875)

sbr = tk.Scrollbar(lbx)
sbr.pack(side="right", fill="y")

sbr.config(command=lbx.yview)
lbx.config(yscrollcommand=sbr.set)

for data in range(100):
    lbx.insert(data,"Sample data"+str(data+1))

root.mainloop()
