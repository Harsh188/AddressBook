import tkinter as tk


def click():
    Search_win = tk.Toplevel(root, height=HEIGHT, width=WIDTH)
    Search_win.title("Search Contact")
    Search_win.configure(background='#420666')
    bw1 = tk.Button(Search_win, text="Close", command=Search_win.destroy)
    bw1.place(relwidth=0.1,relheight=.1,relx=.45,rely=.8)


HEIGHT = 600
WIDTH = 800


root = tk.Tk()
root.title("ADDRESS-BOOK")


canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root, bg="#420666", bd=5)
frame.place(relwidth=1, relheight=1)

# entry = tk.Entry(frame, font=40)
# entry.place(relwidth=0.65, relheight=1)

b1 = tk.Button(frame, text="Search", command=click)
b1.place(relx=0.25, relwidth=0.5, relheight=0.25)


b2 = tk.Button(frame, text="Add")
b2.place(relx=0.25, rely=0.3, relwidth=0.5, relheight=0.25)

b3 = tk.Button(frame, text="Edit")
b3.place(relx=0.25, rely=0.65, relwidth=0.5, relheight=0.25)

# lower_frame = tk.Frame(root, bg="#80c1ff", bd=5)
# lower_frame.place(relwidth=0.75, relheight=0.6, relx=0.5, rely=0.25, anchor="n")

# label = tk.Label(lower_frame, text="Details will be displayed here")

root.mainloop()
