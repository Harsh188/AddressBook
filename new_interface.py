import tkinter as tk
from tkinter import font as tkfont
import Contact_book as cb


def disp_info_fav():
    info = cb.disp_fav()
    output1.delete(0.0, END)
    output1.insert(END, info)


root = tk.Tk()
root.title("ADDRESS-BOOK")

canvas = tk.Canvas(root, height=600, width=800)
canvas.place(relwidth=1, relheight=1)

f1 = tk.Frame(canvas, bg="#373737", bd=5)
f1.place(relwidth=0.25, relheight=1)

textentry1 = tk.Entry(f1, width=20, bg="#ffffff")
textentry1.insert(0, "Enter Name")
textentry1.place(relx=0.039, rely=0.04, relwidth=0.925, relheight=0.035)

lbx = tk.Listbox(f1, background="#373737", fg="white")
lbx.place(relx=0.039, rely=0.125, relwidth=0.925, relheight=0.9)
lbx.config(borderwidth=0)

sbr = tk.Scrollbar(lbx)
sbr.pack(side="right", fill="y")

sbr.config(command=lbx.yview)
lbx.config(yscrollcommand=sbr.set)

for data in range(100):
    lbx.insert(data, "Sample data" + str(data + 1))

f2 = tk.Frame(canvas, bg="#2a2a2a", bd=5)
f2.place(relx=0.25, relwidth=0.75, relheight=1)

output1 = tk.Text(f2, background="#2a2a2a", fg="white")
output1.place(relx=0.1, rely=0, relwidth=0.8, relheight=0.85)

b1 = tk.Button(f2, text="+", font=("Helvetica", "24"))
b1.place(relx=0.06, rely=0.928, relwidth=0.0655, relheight=0.045)

b2 = tk.Button(f2, text="Edit", font=("Helvetica", "16"))
b2.place(relx=0.75, rely=0.928, relwidth=0.0655, relheight=0.045)

b3 = tk.Button(
    f2, text="Favourites", font=("Helvetica", "8"), command=lambda: disp_info_fav()
)
b3.place(relx=0.85, rely=0.928, relwidth=0.0655, relheight=0.045)

b1.config(bg="#a8a8a8", fg="white")
b2.config(bg="#a8a8a8", fg="white")
b3.config(bg="#a8a8a8", fg="white")


root.mainloop()
