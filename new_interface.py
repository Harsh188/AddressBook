import tkinter as tk
from tkinter import font as tkfont
import Contact_book as cb


def lift_frame(frame_name):
    frame_name.lift()

def disp_info_fav():
	info = cb.disp_fav()
    # print(info)
    # output1.delete(0.0, END)
	output1.delete(1.0,tk.END)
	output1.insert(tk.END, info)
	# print(output1.get('1.0',tk.END))

def disp_info_name(evt):
	# get selected line index
    index = lbx.curselection()
    # get the line's text
    seltext = lbx.get(index)
    # print(seltext)
    info = cb.search(seltext)
    output1.delete(1.0,tk.END)
    output1.insert(tk.END,info)

def call_add(list_info):
		cb.add_contact(list_info)

def call_edit():
	pass

def name_search(sv):
	try:
		lbx.delete(0,tk.END)
	except:
		pass
	name = sv.get()
	names = cb.get_names(name)
	# print(names)
	for n,name in enumerate(names):
		# print(n, name)
		lbx.insert(n,name)

def initial_listbox():
	name = ' '
	names = cb.get_names(name)
	# print(names)
	for n,name in enumerate(names):
		# print(n, name)
		lbx.insert(n,name)

root = tk.Tk()
root.title("ADDRESS-BOOK")
root.geometry("800x600")

canvas = tk.Canvas(root, height=600, width=600)
canvas.place(relwidth=1, relheight=1)

f1 = tk.Frame(canvas, bg="#373737", bd=5)
f1.place(relwidth=0.25, relheight=1)

sv = tk.StringVar()
sv.trace("w", lambda name, index, mode, sv=sv: name_search(sv))

textentry1 = tk.Entry(f1, width=20, bg="#ffffff",textvariable=sv)
textentry1.insert(0, " ")
textentry1.place(relx=0.039, rely=0.04, relwidth=0.925, relheight=0.035)
textentry1.pack()

lbx = tk.Listbox(f1, background="#373737", fg="white",selectmode = tk.SINGLE)
lbx.place(relx=0.039, rely=0.125, relwidth=0.925, relheight=0.9)
lbx.config(borderwidth=0)
initial_listbox()
lbx.bind('<<ListboxSelect>>', disp_info_name)

sbr = tk.Scrollbar(lbx)
sbr.pack(side="right", fill="y")

sbr.config(command=lbx.yview)
lbx.config(yscrollcommand=sbr.set)

f2 = tk.Frame(canvas, bg="#2a2a2a", bd=5)
f2.place(relx=0.25, relwidth=0.75, relheight=1)

output1 = tk.Text(f2, background="#2a2a2a", fg="white")
output1.place(relx=0.1, rely=0, relwidth=0.8, relheight=0.85)

b1 = tk.Button(f2, text="+", font=("Helvetica", "24"), command=lambda: lift_frame(f4))
b1.place(relx=0.06, rely=0.928, relwidth=0.0655, relheight=0.045)

b2 = tk.Button(f2, text="Edit", font=("Helvetica", "8"), command=lambda: lift_frame(f3))
b2.place(relx=0.75, rely=0.928, relwidth=0.0655, relheight=0.045)

b3 = tk.Button(f2, text="Favourites", font=("Helvetica", "8"))
b3.place(relx=0.85, rely=0.928, relwidth=0.0655, relheight=0.045)

b1.config(bg="#a8a8a8", fg="white")
b2.config(bg="#a8a8a8", fg="white")
b3.config(bg="#a8a8a8", fg="white")

f3 = tk.Frame(canvas, bg="#3f3f3f", bd=5)
f3.place(relx=0.25, relwidth=0.75, relheight=1)

b4 = tk.Button(f3, text="Back", font=("Helvetica", "8"), command=lambda: lift_frame(f2))
b4.place(relx=0.85, rely=0.928, relwidth=0.0655, relheight=0.045)

f4 = tk.Frame(canvas, bg="#373737", bd=5)
f4.place(relx=0.25, relwidth=0.75, relheight=1)

b4 = tk.Button(f4, text="Back", font=("Helvetica", "8"), command=lambda: lift_frame(f2))
b4.place(relx=0.85, rely=0.928, relwidth=0.0655, relheight=0.045)


name = tk.Entry(f4, width=20, bg="yellow")
name.insert(0, "Enter Name")
name.place(relx=0.30, rely=0.25, relwidth=0.4, relheight=0.05)
phone = tk.Entry(f4, width=20, bg="yellow")
phone.insert(0, "Enter Phone Number")
phone.place(relx=0.30, rely=0.30, relwidth=0.4, relheight=0.05)
email = tk.Entry(f4, width=20, bg="yellow")
email.insert(0, "Enter Email")
email.place(relx=0.30, rely=0.35, relwidth=0.4, relheight=0.05)
addy = tk.Entry(f4, width=20, bg="yellow")
addy.insert(0, "Enter Address")
addy.place(relx=0.30, rely=0.40, relwidth=0.4, relheight=0.05)
bd = tk.Entry(f4, width=20, bg="yellow")
bd.insert(0, "Enter Birthday")
bd.place(relx=0.30, rely=0.45, relwidth=0.4, relheight=0.05)
fav = tk.Entry(f4, width=20, bg="yellow")
fav.insert(0, "Enter if Favourite(yes/no)")
fav.place(relx=0.30, rely=0.50, relwidth=0.4, relheight=0.05)

b5 = tk.Button(
    f4,
    text="Add Contact",
    command=lambda: cb.call_add(
        [name.get(), phone.get(), email.get(), addy.get(), bd.get(), fav.get()]
    ),
)
b5.place(relx=0.42, rely=0.60, relwidth=0.15, relheight=0.05)


f2.lift()


if __name__ == "__main__":
	root.mainloop()
