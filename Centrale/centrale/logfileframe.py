from tkinter import Entry, Label, Checkbutton, Button, StringVar, OptionMenu, INSERT, NORMAL, DISABLED, BOTH, RIGHT
from myframe import MyFrame
from tkinter.filedialog import askopenfilename
import tkinter.scrolledtext as tkst
import os
import os.path

class LogFileReader(MyFrame):
    def __init__(self, nb):
        super().__init__(nb, "Log Files")
        self.textBox = tkst.ScrolledText(master=self)
        self.textBox.pack(padx=10, pady=10, fill=BOTH, expand=True)
        self.textBox.config(state=DISABLED)
        openButton = Button(self, text="Open Log File", command=self.openLogFile)
        openButton.pack(padx=25, pady=5, side=RIGHT)

    def openLogFile(self):
        path = os.path.dirname(os.path.abspath(__file__))
        path = askopenfilename(initialdir = path + "/../logs", title = "Select Log File", filetypes=[("Text files","*.txt")])
        with open(path, "r") as log_file:
            self.textBox.config(state=NORMAL)
            self.textBox.insert(INSERT, log_file.read())
            self.textBox.config(state=DISABLED)