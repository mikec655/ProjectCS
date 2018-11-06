from tkinter import Button, Entry, Label, W, E
from myframe import MyFrame
from tkinter import *
import os
from PIL import Image, ImageTk

class Login(MyFrame):


    def __init__(self, nb):
        super().__init__(nb, "Login")
        self.creds = 'Centrale/centrale/tempfile.temp'
        #'C:\\Users\\gerben\\Desktop\\school\\jaar 2\\Per 1\\project\\ProjectCS\\Centrale\\centrale\\tempfile.temp'

        self.loggedin = ""
        self.loggedout = ""

        with open(self.creds, 'w+') as f:
            f.write('Admin')
            f.write('\n')
            f.write('Admin1') 
       
        
        instruction = Label(self, text='Please login: ',background='white')
        instruction.grid(sticky=E)

        name = Label(self,text = 'Username: ',background='white')
        passw = Label(self, text='Password',background='white')

        name.grid(row=1,sticky=W)
        passw.grid(row=2,sticky=W)

        self.nameE = Entry(self)
        self.pwordE = Entry(self, show='*')
        self.nameE.bind('<Return>', lambda _: self.CheckLogin())
        self.pwordE.bind('<Return>', lambda _: self.CheckLogin())
        self.nameE.grid(row=1, column=1)
        self.pwordE.grid(row=2, column=1)
        
        loginB = Button(self, text='Login',command=self.CheckLogin)
        loginB.grid(columnspan=2, sticky=W)

        self.inlogError = Label(self, text='',background='white', foreground="red")
        self.inlogError.grid(row=5,sticky=W)

        try:  
            self.path = Image.open("Centrale/centrale/zeng_logo.png")
        except IOError: 
            pass

        Photo = ImageTk.PhotoImage(self.path)
        Logo = Label(self, image=Photo)
        Logo.image = Photo
        Logo.place(x=300, y=100)    


    def CheckLogin(self):
        with open(self.creds) as f:
            data = f.readlines()
            username = data[0].rstrip()
            password = data[1].rstrip()
        if not self.nameE.get() == username or not self.pwordE.get() == password:
            self.inlogError['text'] = "Incorrect inlog!"
        else:
            self.loggedin = "I"          
            self.nameE.delete(0, 'end')
            self.pwordE.delete(0, 'end')
            self.inlogError['text'] = ""
            self.logoutB = Button(self, text='Logout',command=self.logout)
            self.logoutB.grid(columnspan=2, row=5, sticky=W)
            
           


    def logout(self):
        self.loggedin = "U"
        self.logoutB.destroy()
