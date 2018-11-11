from tkinter import Button, Label, OptionMenu, StringVar, CENTER, LEFT, RIGHT, X
from tkinter import ttk
from myframe import MyFrame

class Home(MyFrame):
    def __init__(self, nb, aansturingen):
        #hier wordt het homeframe gemaakt met de verschillende functionele knoppen voor het startscherm
        super().__init__(nb, "Home")
        self.aansturingen = aansturingen.copy()
        self.widgets = []
        self.optionMenuLookUp = {}
        style = ttk.Style()
        style.configure('My.TFrame', background='white')
        self.subFrame = ttk.Frame(self, style='My.TFrame')
        subFrame = ttk.Frame(self.subFrame, style='My.TFrame')
        option = StringVar()
        label = Label(subFrame, fg='black', bg='white', text="Alle Schermen")
        label.pack(fill=X) 
        inrol_button = Button(subFrame, text="Inrollen", command=lambda: self.inrollen(option.get()))
        inrol_button.pack(fill=X) 
        uitrol_button = Button(subFrame, text="Uitrollen", command=lambda: self.uitrollen(option.get()))
        uitrol_button.pack(fill=X) 
        stop_button = Button(subFrame, text="Onderbreek", command=self.stop)
        stop_button.pack(fill=X) 
        # optionMenu
        optionSubFrame = ttk.Frame(subFrame, style='My.TFrame') 
        optionLabel = Label(optionSubFrame, fg='black', bg='white', text="Tot:")
        optionLabel.pack(side=LEFT) 
        options = ["over 1 uur", "over 2 uur", "over 3 uur", "over 4 uur", "einde dag"]
        option.set(options[0])
        optionMenu = OptionMenu(optionSubFrame, option, *options)
        optionMenu.config(width=10)
        optionMenu.pack(side=RIGHT)
        optionSubFrame.pack(fill=X)
        ########################################
        auto_button = Button(subFrame, text="Automatisch", command=self.automatisch)
        auto_button.pack(fill=X)
        subFrame.pack(padx=5, side=LEFT)
        self.subFrame.place(relx=0.5, rely=0.5, anchor=CENTER)

    def update(self, aansturingen):
        # wanneer er nieuwe aansturingen worden aangesloten 
        # of een aansturinge wordt verwijderd wordt hier het frame geupdate.
        if aansturingen == self.aansturingen:
            return
        for widget in self.widgets:
            widget.destroy()
        for aansturing in aansturingen:
            option = StringVar()
            subFrame = ttk.Frame(self.subFrame, style='My.TFrame')
            label = Label(subFrame, fg='black', bg='white', text=aansturing.name)
            label.pack(fill=X)    
            inrol_button = Button(subFrame,  text="Inrollen", command=lambda: aansturing.inrollen(option.get()))
            inrol_button.pack(fill=X)
            uitrol_button = Button(subFrame,  text="Uitrollen", command=lambda: aansturing.uitrollen(option.get()))
            uitrol_button.pack(fill=X)
            stop_button = Button(subFrame, text="Onderbreek", command=aansturing.stop)
            stop_button.pack(fill=X) 
            optionSubFrame = ttk.Frame(subFrame, style='My.TFrame') 
            optionLabel = Label(optionSubFrame, fg='black', bg='white', text="Tot:")
            optionLabel.pack(side=LEFT) 
            options = ["over 1 uur", "over 2 uur", "over 3 uur", "over 4 uur", "einde dag"]
            option.set(options[0])
            #optionMenuLookUp[aansturing.id] = option
            optionMenu = OptionMenu(optionSubFrame, option, *options)
            optionMenu.config(width=10)
            optionMenu.pack(side=RIGHT)
            optionSubFrame.pack(fill=X)
            auto_button = Button(subFrame, text="Automatisch", command=aansturing.setTimeout)
            auto_button.pack(fill=X)
            self.widgets.append(subFrame)
            subFrame.pack(padx=5, side=LEFT)
        self.aansturingen = aansturingen.copy()
        
    def uitrollen(self, timeout=""):
        #definiteert de aansturing voor het uitrollen.
        for aansturing in self.aansturingen:
            aansturing.uitrollen(timeout)

    def inrollen(self, timeout=""):
        #definiteert de aansturing voor het inrollen.
        for aansturing in self.aansturingen:
            aansturing.inrollen(timeout)

    def stop(self):
        #definiteert de aansturing voor het stoppen.
        for aansturing in self.aansturingen:
            aansturing.stop()

    def automatisch(self):
        for aansturing in self.aansturingen:
            aansturing.setTimeout("")
