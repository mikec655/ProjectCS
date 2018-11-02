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
        self.login = login
        self.nb = nb
        instruction = Label(self.login, text='Please login: ',background='white')
        instruction.grid(sticky=E)

        name = Label(self.login,text = 'Username: ',background='white')
        passw = Label(self.login, text='Password',background='white')

        name.grid(row=1,sticky=W)
        passw.grid(row=2,sticky=W)

        self.nameE = Entry(self.login)
        self.pwordE = Entry(self.login, show='*')
        self.nameE.bind('<Return>', lambda _: self.CheckLogin())
        self.pwordE.bind('<Return>', lambda _: self.CheckLogin())
        self.nameE.grid(row=1, column=1)
        self.pwordE.grid(row=2, column=1)
        

        loginB = Button(self.login, text='Login',command=self.CheckLogin)
        loginB.grid(columnspan=2, sticky=W)
        

        logoutB = Button(self.login, text='Logout',command=self.logout)
        logoutB.grid(columnspan=2, sticky=W)


    def CheckLogin(self):
        with open(self.creds) as f:
            data = f.readlines()
            username = data[0].rstrip()
            password = data[1].rstrip()



        if not self.nameE.get() == username or not self.pwordE.get() == password:
            print('foute login')
            self.loginFault = Label(self.login, text='Fout wachtwoord',background='white')
            self.loginFault.grid(row=5,sticky=W)
        else:
            self.loggedin = "I"          
            print('correct pass')
            self.nameE.delete(0, 'end')
            self.pwordE.delete(0, 'end')
            self.loginFault.destroy()


    def logout(self):
        self.loggedin = "U"
