import tkinter as tk
from tkinter import font as tkfont
import Contact_book as cb

def lift_frame(frame_name):
    frame_name.lift()



root = tk.Tk()
root.title("ADDRESS-BOOK")
root.geometry("800x600")

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

b1 = tk.Button(f2, text="+", font=("Helvetica", "24"),command=lambda:lift_frame(f4))
b1.place(relx=0.06, rely=0.928, relwidth=0.0655, relheight=0.045)

b2 = tk.Button(f2, text="Edit", font=("Helvetica", "16"),command=lambda:lift_frame(f3))
b2.place(relx=0.75, rely=0.928, relwidth=0.0655, relheight=0.045)

b3 = tk.Button(f2, text="Favourites", font=("Helvetica", "8"))
b3.place(relx=0.85, rely=0.928, relwidth=0.0655, relheight=0.045)

b1.config(bg="#a8a8a8", fg="white")
b2.config(bg="#a8a8a8", fg="white")
b3.config(bg="#a8a8a8", fg="white")

f3 = tk.Frame(canvas, bg="#3f3f3f", bd=5)
f3.place(relx=0.25, relwidth=0.75, relheight=1)

b4 = tk.Button(f3, text="Back", font=("Helvetica", "8"),command=lambda:lift_frame(f2))
b4.place(relx=0.85, rely=0.928, relwidth=0.0655, relheight=0.045)

f4 = tk.Frame(canvas, bg="yellow", bd=5)
f4.place(relx=0.25, relwidth=0.75, relheight=1)

b4 = tk.Button(f4, text="Back", font=("Helvetica", "8"),command=lambda:lift_frame(f2))
b4.place(relx=0.85, rely=0.928, relwidth=0.0655, relheight=0.045)


name = tk.Entry(f4, width=20, bg="yellow")
name.insert(0, 'Enter Name')
name.place(relx=0.30, rely=0.25, relwidth=0.4, relheight=0.05)
phone = tk.Entry(f4, width=20, bg="yellow")
phone.insert(0, 'Enter Phone Number')
phone.place(relx=0.30, rely=0.30, relwidth=0.4, relheight=0.05)
email = tk.Entry(f4, width=20, bg="yellow")
email.insert(0, 'Enter Email')
email.place(relx=0.30, rely=0.35, relwidth=0.4, relheight=0.05)
addy = tk.Entry(f4, width=20, bg="yellow")
addy.insert(0, 'Enter Address')
addy.place(relx=0.30, rely=0.40, relwidth=0.4, relheight=0.05)
bd = tk.Entry(f4, width=20, bg="yellow")
bd.insert(0, 'Enter Birthday')
bd.place(relx=0.30, rely=0.45, relwidth=0.4, relheight=0.05)
fav = tk.Entry(f4, width=20, bg="yellow")
fav.insert(0, 'Enter if Favourite(yes/no)')
fav.place(relx=0.30, rely=0.50, relwidth=0.4, relheight=0.05)

b5 = tk.Button(f4, text="Add Contact",command = lambda: cb.call_add([name.get(), \
            phone.get(),email.get(),addy.get(),bd.get(),fav.get()]))
b5.place(relx=0.42, rely=0.60, relwidth=0.15, relheight=0.05)
    


f2.lift()



root.mainloop()
