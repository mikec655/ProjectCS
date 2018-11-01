from tkinter import Button, Entry, Label, W, E

class Login:

    def __init__(self):
        self.creds = 'Centrale/centrale/tempfile.temp'
        #'C:\\Users\\gerben\\Desktop\\school\\jaar 2\\Per 1\\project\\ProjectCS\\Centrale\\centrale\\tempfile.temp'
        self.pwordE = ''
        self.nameE = ''
        self.loginN = ''
        self.sNB = ''
        self.loggedin = False

        with open(self.creds, 'r+') as f:  # Creates a document using the variable we made at the top.
            f.write('Admin')
            # self.nameE.get())  # nameE is the variable we were storing the input to. Tkinter makes us use .get() to get the actual string.
            f.write('\n')  # Splits the line so both variables are on different lines.
            f.write('Admin1')  # Same as nameE just with pword var
        with open(self.creds, 'r') as f:
            initdata = f.readlines()
            self.nameE = initdata[0].rstrip()  # Data[0], 0 is the first line, 1 is the second and so on.
            self.pwordE = initdata[1].rstrip()  # Using .rstrip() will remove the \n (new line) word from before when we input it
            # f.close()  # Closes the file


    def frame(self, login, nb):
        self.loginN = login
        self.sNB = nb
        
        instruction = Label(login, text='Please login: ',background='white')
        instruction.grid(sticky=E)

        name = Label(login,text = 'Username: ',background='white')
        passw = Label(login, text='Password',background='white')

        name.grid(row=1,sticky=W)
        passw.grid(row=2,sticky=W)

        nameE = Entry(login)
        pwordE = Entry(login, show='*')
        nameE.grid(row=1, column=1)
        pwordE.grid(row=2, column=1)

        loginB = Button(login, text='Login',command=self.CheckLogin)
        loginB.grid(columnspan=2, sticky=W)


        nb.add(login, text='Login')

    def CheckLogin(self):
        with open(self.creds) as f:
            data = f.readlines()  # This takes the entire document we put the info into and puts it into the data variable
            uname = data[0].rstrip()  # Data[0], 0 is the first line, 1 is the second and so on.
            pword = data[1].rstrip()  # Using .rstrip() will remove the \n (new line) word from before when we input it

        if self.nameE == uname and self.pwordE == pword:  # Checks to see if you entered the correct data.        print('logedin')
            self.loggedin = True
            print('correct pass')


        else:
            print('foute login')