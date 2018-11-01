from tkinter import Button, Entry, Label, W, E
from tkinter import ttk

class Login(ttk.Frame):

    def __init__(self,master=None):
        super().__init__(master)
        self.creds = 'Centrale/centrale/tempfile.temp'
        #'C:\\Users\\gerben\\Desktop\\school\\jaar 2\\Per 1\\project\\ProjectCS\\Centrale\\centrale\\tempfile.temp'
        self.loggedin = False

        with open(self.creds, 'w+') as f:
            f.write('Admin')
            f.write('\n')
            f.write('Admin1') 


    def frame(self, login, nb):
        instruction = Label(login, text='Please login: ')
        instruction.grid(sticky=E)

        name = Label(login,text = 'Username: ')
        passw = Label(login, text='Password')

        name.grid(row=1,sticky=W)
        passw.grid(row=2,sticky=W)

        self.nameE = Entry(login)
        self.pwordE = Entry(login, show='*')
        self.nameE.grid(row=1, column=1)
        self.pwordE.grid(row=2, column=1)

        loginB = Button(login, text='Login',command=self.CheckLogin)
        loginB.grid(columnspan=2, sticky=W)
        

        logoutB = Button(login, text='Logout',command=self.logout)
        logoutB.grid(columnspan=2, sticky=W)
        # logoutB.grid(columnspan=2, sticky=W)
        nb.add(login, text='Login')

    def CheckLogin(self):
        with open(self.creds) as f:
            data = f.readlines()  # This takes the entire document we put the info into and puts it into the data variable
            username = data[0].rstrip()  # Data[0], 0 is the first line, 1 is the second and so on.
            password = data[1].rstrip()  # Using .rstrip() will remove the \n (new line) word from before when we input it
        print(self.nameE)
        print(self.pwordE)

        if self.nameE.get() == username and self.pwordE.get() == password:  # Checks to see if you entered the correct data.        print('logedin')
            self.loggedin = True
            
            print('correct pass')


        else:
            print('foute login')
    
    def logout(self):
        self.loggedin = False
