from tkinter import ttk
import loginscherm
import properties

class MyFrame(ttk.Frame):
    def __init__(self, nb):
        super().__init__(nb)


    def voegFrameToe(self, nb):
        nb.add(self, text="NAME")
    
    def verwijderFrame(self, frame):
        pass

