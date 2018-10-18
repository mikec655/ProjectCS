from tkinter import *

root = Tk()

topFrame = Frame(root)
topFrame.pack()
buttomFrame = Frame(root)
buttomFrame.pack(side=BOTTOM)

button1 = Button(topFrame, text='Button1', fg='red')
button2 = Button(topFrame, text='Button2', fg='blue')
button3 = Button(topFrame, text='Button3', fg='green')
button4 = Button(buttomFrame, text='Button 4', fg='purple')

# theLabel = Label(root, text='hello')

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=BOTTOM)

# theLabel.pack()
root.mainloop()