from tkinter import *

root = Tk()

one = Label(root, text="one", bg="red", fg="white")
one.pack()
two = Label(root, text="one", bg="green", fg="white")
two.pack(fill=X)
three = Label(root, text="one", bg="blue", fg="white")
three.pack(side=LEFT, fill=Y)

root.mainloop()