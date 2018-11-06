from tkinter import Button, Label
from myframe import MyFrame

class Home(MyFrame):
    def __init__(self, nb, aansturingen):
        super().__init__(nb, "Home")
        self.aansturingen = aansturingen.copy()
        self.widgets = []

        label = Label(self, text="Alle Schermen")
        label.grid()
        inrol_button = Button(self, text="Inrollen", command=self.inrollen)
        inrol_button.grid()
        uitrol_button = Button(self, text="Uitrollen", command=self.uitrollen)
        uitrol_button.grid()

    def update(self, aansturingen):
        if aansturingen == self.aansturingen:
            return
        for widget in self.widgets:
            widget.destroy()
        for aansturing in aansturingen:
            label = Label(self, text=aansturing.name)
            self.widgets.append(label)
            label.grid()
            inrol_button = Button(self, text="Inrollen", command=aansturing.inrollen)
            self.widgets.append(inrol_button)
            inrol_button.grid()
            uitrol_button = Button(self, text="Uitrollen", command=aansturing.uitrollen)
            self.widgets.append(uitrol_button)
            uitrol_button.grid()
        self.aansturingen = aansturingen.copy()
        

    def uitrollen(self):
        for aansturing in self.aansturingen:
            aansturing.uitrollen()

    def inrollen(self):
        for aansturing in self.aansturingen:
            aansturing.inrollen()
