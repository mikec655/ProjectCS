from tkinter import Button, Entry, Label, W, E
from tkinter import ttk

class Login(ttk.Frame):


    def __init__(self,master=None):
        super().__init__(master)
        self.creds = 'Centrale/centrale/tempfile.temp'
        #'C:\\Users\\gerben\\Desktop\\school\\jaar 2\\Per 1\\project\\ProjectCS\\Centrale\\centrale\\tempfile.temp'

        self.loggedin = ""

        with open(self.creds, 'w+') as f:
            f.write('Admin')
            f.write('\n')
            f.write('Admin1') 


    def frame(self, login, nb):
        instruction = Label(login, text='Please login: ',background='white')
        instruction.grid(sticky=E)

        name = Label(login,text = 'Username: ',background='white')
        passw = Label(login, text='Password',background='white')

        name.grid(row=1,sticky=W)
        passw.grid(row=2,sticky=W)

        self.nameE = Entry(login)
        self.pwordE = Entry(login, show='*')
        self.nameE.bind('<Return>', lambda _: self.CheckLogin())
        self.pwordE.bind('<Return>', lambda _: self.CheckLogin())
        self.nameE.grid(row=1, column=1)
        self.pwordE.grid(row=2, column=1)
        

        loginB = Button(login, text='Login',command=self.CheckLogin)
        loginB.grid(columnspan=2, sticky=W)
        

        logoutB = Button(login, text='Logout',command=self.logout)
        logoutB.grid(columnspan=2, sticky=W)


    def CheckLogin(self):
        with open(self.creds) as f:
            data = f.readlines()
            username = data[0].rstrip()
            password = data[1].rstrip()

        if self.nameE.get() == username and self.pwordE.get() == password:
            self.loggedin = "I"          
            print('correct pass')
            self.nameE.delete(0, 'end')
            self.pwordE.delete(0, 'end')
        else:
            print('foute login')

    def logout(self):
        self.loggedin = "U"
