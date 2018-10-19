from tkinter import *

root = Tk()

def leftClick(event):
	print("Left")

def middleClick(event):
	print("middle")

def rightClick(event):
	print("right")



frame = Frame(root, width=300, hight=250)
frame.bind("<Button-1>", leftClick)

root.mainloop()