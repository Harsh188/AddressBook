from tkinter import *


def click():
    entered_text = textentry.get()
    output.delete(0.0, END)
    try:
        definition = my_compdictionary[entered_text]
    except:
        definition = "none found bruh"
    output.insert(END, definition)


window = Tk()
window.title("Address Book")
window.configure(background="black")


Label(
    window, text="Zayds dictionary", bg="black", fg="white", font="none 24 bold"
).grid(row=1, column=0, sticky=W)


textentry = Entry(window, width=20, bg="white")
textentry.grid(row=2, column=0, sticky=W)


Button(window, text="Submit", width="6", command=click).grid(row=3, column=0, sticky=W)

Label(window, text="\nDefinition", bg="black", fg="white", font="none 24 bold").grid(
    row=4, column=0, sticky=W
)

output = Text(window, width=75, height=6, wrap=WORD, background="white")
output.grid(row=5, columnspan=2, sticky=W)

my_compdictionary = {"chakka": "abdul", "gandu": "Ass tit wah"}

window.mainloop()

