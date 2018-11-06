from tkinter import Button
from myframe import MyFrame

class Home(MyFrame):
    def __init__(self, nb, aansturingen):
        super().__init__(nb, "Home")
        self.aansturingen = aansturingen
        inrol_button = Button(self, text="Inrollen", command=self.inrollen)
        uitrol_button = Button(self, text="Uitrollen", command=self.uitrollen)
        inrol_button.grid()
        uitrol_button.grid()

    def uitrollen(self):
        for aansturing in self.aansturingen:
            aansturing.uitrollen()

    def inrollen(self):
        for aansturing in self.aansturingen:
            aansturing.inrollen()
