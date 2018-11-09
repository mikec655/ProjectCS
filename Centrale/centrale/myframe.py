from tkinter import ttk

class MyFrame(ttk.Frame):
    #hier wordt de style van het frame gedefinieerd.
    def __init__(self, nb, name):
        style = ttk.Style()
        style.configure('My.TFrame', background='white')
        super().__init__(nb, style='My.TFrame')
        nb.add(self, text=name)
    
    def deleteFrame(self):
        #hier wordt het frame vernietigd
        self.destroy()

