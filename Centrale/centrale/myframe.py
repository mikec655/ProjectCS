from tkinter import ttk

class MyFrame(ttk.Frame):
    def __init__(self, nb, name):
        super().__init__(nb)
        nb.add(self, text=name)
    
    def deleteFrame(self):
        self.destroy()

