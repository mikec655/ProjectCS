from tkinter import Button, Label, OptionMenu, StringVar, CENTER, LEFT, RIGHT, X
from tkinter import ttk
from myframe import MyFrame

class Home(MyFrame):
    def __init__(self, nb, motorControls):
        #hier wordt het homeframe gemaakt met de verschillende functionele knoppen voor het startscherm
        super().__init__(nb, "Home")
        self.motorControls = motorControls.copy()
        self.widgets = []
        style = ttk.Style()
        style.configure('My.TFrame', background='white')
        # gui widgets voor het aansturen van alle schermen ter gelijke tijd
        self.subFrame = ttk.Frame(self, style='My.TFrame')
        subFrame = ttk.Frame(self.subFrame, style='My.TFrame')
        option = StringVar()
        label = Label(subFrame, fg='black', bg='white', text="Alle Schermen")
        label.pack(fill=X) 
        inrol_button = Button(subFrame, text="Inrollen", command=lambda: self.rollIn(option.get()))
        inrol_button.pack(fill=X) 
        uitrol_button = Button(subFrame, text="Uitrollen", command=lambda: self.rollOut(option.get()))
        uitrol_button.pack(fill=X) 
        stop_button = Button(subFrame, text="Onderbreek", command=self.stopRolling)
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
        auto_button = Button(subFrame, text="Automatisch", command=self.automatic)
        auto_button.pack(fill=X)
        subFrame.pack(padx=5, side=LEFT)
        self.subFrame.place(relx=0.5, rely=0.5, anchor=CENTER)

    def update(self, motorControls):
        # wanneer er nieuwe aansturingen worden aangesloten 
        # of een aansturing wordt verwijderd wordt hier het frame geupdate.
        if motorControls == self.motorControls:
            return
        for widget in self.widgets:
            widget.destroy()
        for control in motorControls:
            option = StringVar()
            subFrame = ttk.Frame(self.subFrame, style='My.TFrame')
            label = Label(subFrame, fg='black', bg='white', text=control.name)
            label.pack(fill=X)    
            inrol_button = Button(subFrame,  text="Inrollen", command=lambda: control.rollIn(option.get()))
            inrol_button.pack(fill=X)
            uitrol_button = Button(subFrame,  text="Uitrollen", command=lambda: control.rollOut(option.get()))
            uitrol_button.pack(fill=X)
            stop_button = Button(subFrame, text="Onderbreek", command=control.stopRolling)
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
            auto_button = Button(subFrame, text="Automatisch", command=lambda: control.setTimeout('auto'))
            auto_button.pack(fill=X)
            self.widgets.append(subFrame)
            subFrame.pack(padx=5, side=LEFT)
        self.motorControls = motorControls.copy()
        
    def rollOut(self, timeout=""):
        # Rolt alle aangesloten aanstringen uit
        for control in self.motorControls:
            control.rollOut(timeout)

    def rollIn(self, timeout=""):
        # Rolt alle aangesloten aanstringen in
        for control in self.motorControls:
            control.rollIn(timeout)

    def stopRolling(self):
        # Onderbreekt het uitrollen van alle 
        for control in self.motorControls:
            control.stopRolling()

    def automatic(self):
        # Zet de control weer op automatisch
        for control in self.motorControls:
            control.setTimeout("auto")
