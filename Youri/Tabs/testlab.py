#!/usr/local/bin/python3
from tkinter import *
from tkinter import ttk
  
class App(Tk):
    def __init__(self,*args,**kwargs):
       Tk.__init__(self,*args,**kwargs)
       self.notebook = ttk.Notebook()
       self.add_tab()
       self.notebook.grid(row=0)
  
    def add_tab(self):
        tab = Area(self.notebook)
        tab2 = Volume(self.notebook) 
        self.notebook.add(tab,text="Tag")
        self.notebook.add(tab2,text="Tag2")
  
  
class Area(Frame):
   def __init__(self,name,*args,**kwargs):
       Frame.__init__(self,*args,**kwargs)
       self.label = Label(self, text="Hi This is Tab1")
       self.label.grid(row=1,column=0,padx=10,pady=10)
       self.name = name
  
class Volume(Frame):
   def __init__(self,name,*args,**kwargs):
       Frame.__init__(self,*args,**kwargs)
       self.label = Label(self, text="Hi This is Tab2")
       self.label.grid(row=1,column=0,padx=10,pady=10)
       self.name = name
  
my_app = App()
my_app.mainloop()