import tkinter as tk

HEIGHT = 400
WIDTH = 400

root = tk.Tk()
root.title("ADDRESS-BOOK")


canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root, bg="#80c1ff", bd=5)
frame.place(relwidth=0.75, relheight=0.1, relx=0.5, rely=0.1, anchor="n")

entry = tk.Entry(frame, font=40)
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Get Contact")
button.place(relx=0.7, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg="#80c1ff", bd=5)
lower_frame.place(relwidth=0.75, relheight=0.6, relx=0.5, rely=0.25, anchor="n")

label = tk.Label(lower_frame, text="Details will be displagi
root.mainloop()
