from tkinter import Button, Label, CENTER, LEFT, X
from tkinter import ttk
from myframe import MyFrame

class Home(MyFrame):
    def __init__(self, nb, aansturingen):
        #hier wordt het homeframe gemaakt met de verschillende functionele knoppen voor het startscherm
        super().__init__(nb, "Home")
        self.aansturingen = aansturingen.copy()
        self.widgets = []
        style = ttk.Style()
        style.configure('My.TFrame', background='white')
        self.subFrame = ttk.Frame(self, style='My.TFrame')
        subFrame = ttk.Frame(self.subFrame, style='My.TFrame')
        label = Label(subFrame, fg='black', bg='white', text="Alle Schermen")
        label.pack(fill=X) 
        inrol_button = Button(subFrame, text="Inrollen", command=self.inrollen)
        inrol_button.pack(fill=X) 
        uitrol_button = Button(subFrame, text="Uitrollen", command=self.uitrollen)
        uitrol_button.pack(fill=X) 
        stop_button = Button(subFrame, text="Onderbreek", command=self.stop)
        stop_button.pack(fill=X) 
        subFrame.pack(padx=5, side=LEFT)
        self.subFrame.place(relx=0.5, rely=0.5, anchor=CENTER)

    def update(self, aansturingen):
        #wanneer er nieuwe aansturingen worden aangesloten wordt hier het frame geupdate.
        if aansturingen == self.aansturingen:
            return
        for widget in self.widgets:
            widget.destroy()
        for aansturing in aansturingen:
            subFrame = ttk.Frame(self.subFrame, style='My.TFrame')
            label = Label(subFrame, fg='black', bg='white', text=aansturing.name)
            label.pack(fill=X)    
            inrol_button = Button(subFrame,  text="Inrollen", command=aansturing.inrollen)
            inrol_button.pack(fill=X)
            uitrol_button = Button(subFrame,  text="Uitrollen", command=aansturing.uitrollen)
            uitrol_button.pack(fill=X)
            stop_button = Button(subFrame, text="Onderbreek", command=aansturing.stop)
            stop_button.pack(fill=X) 
            self.widgets.append(subFrame)
            subFrame.pack(padx=5, side=LEFT)
        self.aansturingen = aansturingen.copy()
        

    def uitrollen(self):
        #definiteert de aansturing voor het uitrollen.
        for aansturing in self.aansturingen:
            aansturing.uitrollen()

    def inrollen(self):
        #definiteert de aansturing voor het inrollen.
        for aansturing in self.aansturingen:
            aansturing.inrollen()

    def stop(self):
        #definiteert de aansturing voor het stoppen.
        for aansturing in self.aansturingen:
            aansturing.stop()
