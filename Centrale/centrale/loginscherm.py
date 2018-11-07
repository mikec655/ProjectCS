from tkinter import Button, Entry, Label, W, E, X, CENTER
from tkinter import ttk
from myframe import MyFrame
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
       
        style = ttk.Style()
        style.configure('My.TFrame', background='white')
        self.subFrame = ttk.Frame(self, style='My.TFrame')

        try:  
            self.path = Image.open("Centrale/centrale/zeng_logo.png")
        except IOError: 
            pass

        Photo = ImageTk.PhotoImage(self.path)
        Logo = Label(self.subFrame, background="white", image=Photo)
        Logo.image = Photo
        Logo.grid(columnspan=2, pady=15) 

        instruction = Label(self.subFrame, fg= 'black',bg='white', text='Please login: ')
        instruction.grid(row=2, sticky=W)

        name = Label(self.subFrame,fg='black',bg='white', text = 'Username:')
        passw = Label(self.subFrame, fg='black',bg='white', text='Password:')

        name.grid(row=3,sticky=W)
        passw.grid(row=4,sticky=W)

        self.nameE = Entry(self.subFrame)
        self.pwordE = Entry(self.subFrame, show='*')
        self.nameE.bind('<Return>', lambda _: self.CheckLogin())
        self.pwordE.bind('<Return>', lambda _: self.CheckLogin())
        self.nameE.grid(row=3, column=1, sticky="EW")
        self.pwordE.grid(row=4, column=1, sticky="EW")
        
        self.loginB = Button(self.subFrame, text='Login',command=self.CheckLogin)
        self.loginB.grid(row=7, column=1, columnspan=2, pady=15, sticky="EW")

        self.inlogError = Label(self.subFrame, text='',background='white', foreground="red")
        self.inlogError.grid(row=7, sticky=W)
        self.subFrame.place(relx=0.5, rely=0.5, anchor=CENTER) 

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
            self.loginB['text'] = "Logout"
            self.loginB['command'] = self.logout

    def logout(self):
        self.loggedin = "U"
        self.loginB['text'] = "Login"
        self.loginB['command'] = self.CheckLogin
