import tkinter

window = tkinter.Tk()
window.title("GUI")

# creating 2 frames TOP and BOTTOM
top_frame = tkinter.Frame(window).pack()
bottom_frame = tkinter.Frame(window).pack(side = "bottom")

# now, create some widgets in the top_frame and bottom_frame
btn1 = tkinter.Button(top_frame, text = "Button1", fg = "red").pack()# 'fg - foreground' is used to color the contents
btn2 = tkinter.Button(top_frame, text = "Button2", fg = "green").pack()# 'text' is used to write the text on the Button
btn3 = tkinter.Button(bottom_frame, text = "Button2", fg = "purple").pack(side = "left")# 'side' is used to align the widgets
btn4 = tkinter.Button(bottom_frame, text = "Button2", fg = "orange").pack(side = "left")

window.mainloop()