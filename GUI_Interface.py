import tkinter as tk
from tkinter import font as tkfont
import Contact_book as cb

class SampleApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(
            family="Helvetica", size=24, weight="bold", slant="italic"
        )
        self.title("ADDRESS-BOOK")
        self.geometry("800x600")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, SearchPage, AddContact, EditPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.config(bg="#350066")
        label = tk.Label(self, text="Address Book", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(
            self,
            text="Search Contact",
            command=lambda: controller.show_frame("SearchPage"),
        )
        button2 = tk.Button(
            self, text="Add Contact", command=lambda: controller.show_frame("AddContact")
        )
        button3 = tk.Button(
            self,
            text="Edit Contact",
            command=lambda: controller.show_frame("EditPage"),
        )

        button1.place(relx=0.25, rely=0.2, relwidth=0.5, relheight=0.2)
        button2.place(relx=0.25, rely=0.45, relwidth=0.5, relheight=0.2)
        button3.place(relx=0.25, rely=0.7, relwidth=0.5, relheight=0.2)


class SearchPage(tk.Frame):

    def disp_info_name(self, name):
        info = cb.search(name)
        output1 = tk.Text(self, background="white")
        output1.place(relx=0.1, rely=0.5, relwidth=0.8, relheight=0.3)
        output1.insert(tk.END, info)

    def disp_info_fav(self):
        info = cb.disp_fav()
        output1 = tk.Text(self, background="white")
        output1.place(relx=0.1, rely=0.5, relwidth=0.8, relheight=0.3)
        output1.insert(tk.END, info)


    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.config(bg="#4f0099")
        self.controller = controller
        label = tk.Label(self, text="Get Contact", font=controller.title_font)
        label.place(relx=0.25, rely=0.05, relheight=0.06, relwidth=0.5)

        textentry = tk.Entry(self, width=20, bg="yellow")
        textentry.insert(0, 'Enter Name')
        
        textentry.place(relx=0.30, rely=0.25, relwidth=0.4, relheight=0.05)

        output1 = tk.Text(self, background="white")
        output1.place(relx=0.1, rely=0.5, relwidth=0.8, relheight=0.3)

        b2 = tk.Button(self, text="Get Contact", command = lambda: self.disp_info_name(textentry.get()))
        b2.place(relx=0.35, rely=0.35, relwidth=0.15, relheight=0.05)

        b3 = tk.Button(self, text="Get Favourites", command = lambda: self.disp_info_fav())
        b3.place(relx=0.5, rely=0.35, relwidth=0.15, relheight=0.05)

        button = tk.Button(
            self,
            text="Go back",
            command=lambda: controller.show_frame("StartPage"),
        )
        button.place(relx=0.1
        , rely=0.85, relwidth=0.15, relheight=0.05)

    

class AddContact(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.config(bg="#8400ff")
        self.controller = controller
        label = tk.Label(self, text="This is page 2", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(
            self,
            text="Go to the start page",
            command=lambda: controller.show_frame("StartPage"),
        )
        button.pack()


class EditPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.config(bg="#9c33ff")
        self.controller = controller
        label = tk.Label(self, text="This is page 3", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(
            self,
            text="Go to the start page",
            command=lambda: controller.show_frame("StartPage"),
        )
        button.pack()


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
