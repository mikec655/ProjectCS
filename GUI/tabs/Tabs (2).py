#!/usr/local/bin/python3
import tkinter as tk
from tkinter import *
from tkinter import ttk
 
# Root class to create the interface and define the controller function to switch frames
class RootApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(NoteBook)
 
# controller function
    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()
 
# sub-root to contain the Notebook frame and a controller function to switch the tabs within the notebook
class NoteBook(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.notebook = ttk.Notebook()
        self.Instellingen = Instellingen(self.notebook)
        self.Sensor1 = Sensor1(self.notebook)
        self.Sensor2 = Sensor2(self.notebook)
        self.Sensor3 = Sensor3(self.notebook)
        self.Sensor4 = Sensor4(self.notebook)
        self.Sensor5 = Sensor5(self.notebook)

        self.notebook.add(self.Instellingen, text="Instellingen")
        self.notebook.add(self.Sensor1, text="Sensor1")
        self.notebook.add(self.Sensor2, text="Sensor2")
        self.notebook.add(self.Sensor3, text="Sensor3")
        self.notebook.add(self.Sensor4, text="Sensor4")
        self.notebook.add(self.Sensor5, text="Sensor5")
        self.notebook.pack()
 
# controller function
    def switch_tab1(self, frame_class):
        new_frame = frame_class(self.notebook)
        self.tab1.destroy()
        self.tab1 = new_frame
         
# Notebook - Tab 1
class Instellingen(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self._frame = None
        self.switch_frame(Tab1_Frame1)
 
    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()
 
# first frame for Tab1
class Tab1_Frame1(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        # self.label = Label(self, text="Rolluik:")
        # self.label.grid(row=2, sticky=E)
        # self.label_1 = Label(master, text="Name")
        # self.label_2 = Label(master, text="pass")

        # self.entry_1 = Entry(master)
        # self.entry_2 = Entry(master)

        # button object with command to replace the frame
        self.button = Button(self, text="Change it!", command=lambda: master.switch_frame(Tab1_Frame2))
        # self.label_1.pack(side=LEFT, fill=X)
        # self.label_2.pack(side=LEFT, fill=Y)
        # self.label.pack(side=RIGHT, fill=Y)
        

        # self.entry_1.grid(row=0,column=1)
        # self.entry_2.grid(row=1,column=1)

        self.button.pack()

        # self.label_1 = Label(master, text="Name")
        # self.label_2 = Label(master, text="Password")

        # self.entry_1 = Entry(master)
        # self.entry_2 = Entry(master)

        # self.label_1.grid(row=0, sticky=E)
        # self.label_2.grid(row=1, sticky=E)

        # self.entry_1.grid(row=0,column=1)
        # self.entry_2.grid(row=1,column=1)

        # self.label_1.pack(side=LEFT, fill=X)
        # self.label_2.pack(side=LEFT, fill=X)
        # self.entry_1.pack(side=LEFT, fill=X)
        # self.entry_2.pack(side=LEFT, fill=X)

 
# second frame for Tab1
class Tab1_Frame2(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)

        
        self.label_1 = Label(master, text="Name")
        self.label_2 = Label(master, text="Password")

        self.entry_1 = Entry(master)
        self.entry_2 = Entry(master)

        self.label_1.grid(row=0, sticky=E)
        self.label_2.grid(row=1, sticky=E)

        self.entry_1.grid(row=0,column=1)
        self.entry_2.grid(row=1,column=1)

        self.label_1.pack(side=LEFT, fill=X)
        self.label_2.pack(side=LEFT, fill=X)
        self.entry_1.pack(side=LEFT, fill=X)
        self.entry_2.pack(side=LEFT, fill=X)
        self.label = Label(self, text="it has been changed!")
        # and another button to change it back to the previous frame
        self.button = Button(self, text="Change it back!", command=lambda: master.switch_frame(Tab1_Frame1))
        self.label.pack()
        self.button.pack()
 
class Sensor1(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        # self.label = Label(self, text="this is a test - two")
        # self.label.pack()
        # self.button = Button()
 
class Sensor2(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.label = Label(self, text="this is a test - three")
        self.label.pack()
 

class Sensor3(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.label = Label(self, text="this is a test - three")
        self.label.pack()

class Sensor4(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.label = Label(self, text="this is a test - three")
        self.label.pack()

class Sensor5(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.label = Label(self, text="this is a test - three")
        self.label.pack()

if __name__ == "__main__":
    Root = RootApp()
    Root.geometry("800x600")
    Root.title("Frame test")
    Root.mainloop()