from tkinter import Entry, Label, Checkbutton, Button, StringVar, OptionMenu, ANCHOR
from tkinter.ttk import Frame

class Properties(Frame):

    def __init__(self, master=None):
        super().__init__(master)

    def propertieFrame(self, nb, sensors, aansturingen):
        self.x= [1,2,3,4]


        if len(aansturingen)==0:
            pass
        else:
            self.x=[]
            for instantie in aansturingen:
                self.x.append(instantie.name)
                
        rolluiktitel = Label(self, text="Selecteer een rolluik:")
        rolluiktitel.grid(row = 0, column = 0, columnspan = 1, padx = 1, pady = 5)
        rolluiktitel.config(font=("Times new roman", 14))
        #sensors.append("moooi")
        hernoemtitel = Label(self, text="hernoem de module:")
        hernoemtitel.grid(row = 2, column = 0, columnspan = 1,pady = 5)
        hernoemtitel.config(font=("Times new roman", 12))
        
        self.var = StringVar(self)
        self.var.set("Selecteer motor module")
        self.selecteermotor = OptionMenu(self, self.var, *self.x)### hier moet motormodulelijst komen
        self.selecteermotor.grid(row = 1, column = 0, columnspan = 1, padx = 1, pady = 1)
        
        self.hernoemen = Entry(self)
        self.hernoemen.grid(row = 2, column= 12 , columnspan = 1, padx = 1, pady = 1)

        self.sensortitel = Label(self, text= 'Grenswaarde:')
        self.sensortitel.grid(row = 0, column = 80, columnspan = 1, padx = 1, pady = 5)
        self.sensortitel.config(font=("Times new roman", 14))

        self.sensortitel = Label(self, text= 'gebruiken:')
        self.sensortitel.grid(row = 0, column = 100, columnspan = 1, padx = 1, pady = 5)
        self.sensortitel.config(font=("Times new roman", 14))

        self.variabelevoorrijenaanpassen = 1 #wordt gebruikt om row aan te passen per sensor
        """
        for sensorinstantie in sensors:

            

            self.sensortitel = Label(self, text= str(sensorinstantie.name))
            self.sensortitel.grid(row = self.variabelevoorrijenaanpassen, column = 60, columnspan = 1, padx = 1, pady = 5)
            self.sensortitel.config(font=("Times new roman", 14))
    

            self.sensorwaarde = Entry(self)
            self.sensorwaarde.grid(row=self.variabelevoorrijenaanpassen, column= 80, columnspan = 1, padx = 1, pady = 1)
            

            self.checkbox = Checkbutton(self)
            self.checkbox.grid(row=self.variabelevoorrijenaanpassen, column= 100 , columnspan = 1, padx = 1, pady = 1)

            self.variabelevoorrijenaanpassen +=1
            """

        def sensorlijst(self, sensors):
            for sensorinstantie in sensors:

            self.sensortitel = Label(self, text= str(sensorinstantie.name))
            self.sensortitel.grid(row = self.variabelevoorrijenaanpassen, column = 60, columnspan = 1, padx = 1, pady = 5)
            self.sensortitel.config(font=("Times new roman", 14))
    

            self.sensorwaarde = Entry(self)
            self.sensorwaarde.grid(row=self.variabelevoorrijenaanpassen, column= 80, columnspan = 1, padx = 1, pady = 1)
            

            self.checkbox = Checkbutton(self)
            self.checkbox.grid(row=self.variabelevoorrijenaanpassen, column= 100 , columnspan = 1, padx = 1, pady = 1)

            self.variabelevoorrijenaanpassen +=1

            

        """
        for x in sensors:
            
            grenswaardelabel = Label(self, text="Grenswaarde")
            grenswaardebox1 = Entry(self)
            grenswaardebox2 = Entry(self)
            grenswaardebox3 = Entry(self)
            grenswaardebox4 = Entry(self)
            grenswaardebox5 = Entry(self)

            aantimerlabel = Label(self, text="Automatisch aan")
            uittimerlabel = Label(self, text="Automatisch uit")

            aantimerbox = Entry(self)
            uittimerbox = Entry(self)

            aanuitlabel = Label(self, text="Aan uit")

            sensor1label = Label(self, text="Licht Sensor",background='white')
            sensor2label = Label(self, text="Temperatuur Sensor")
            sensor3label = Label(self, text="SensorNaam")
            sensor4label = Label(self, text="SensorNaam")
            sensor5label = Label(self, text="SensorNaam")

          

            sensor1label.grid(row = 55, column = 0, columnspan = 40, padx = 1, pady = 1, sticky = 'w')
            sensor2label.grid(row = 56, column = 0, columnspan = 40, padx = 1, pady = 1, sticky = 'w')
            sensor3label.grid(row = 57, column = 0, columnspan = 40, padx = 1, pady = 1, sticky = 'w')
            sensor4label.grid(row = 58, column = 0, columnspan = 40, padx = 1, pady = 1, sticky = 'w')
            sensor5label.grid(row = 59, column = 0, columnspan = 40, padx = 1, pady = 1, sticky = 'w')

            aantimerlabel.grid(row = 60, column = 0, columnspan = 40, padx = 1, pady = 1, sticky = 'w')
            uittimerlabel.grid(row = 61, column = 0, columnspan = 40, padx = 1, pady = 1, sticky = 'w')

            grenswaardelabel.grid(row = 50, column = 45, columnspan = 40, padx = 1, pady = 1, sticky = 'w')
            grenswaardebox1.grid(row = 55, column=45 , columnspan = 20, padx = 1, pady = 1, sticky = 'n')
            grenswaardebox2.grid(row = 56, column=45 , columnspan = 20, padx = 1, pady = 1, sticky = 'n')
            grenswaardebox3.grid(row = 57, column=45 , columnspan = 20, padx = 1, pady = 1, sticky = 'n')
            grenswaardebox4.grid(row = 58, column=45 , columnspan = 20, padx = 1, pady = 1, sticky = 'n')
            grenswaardebox5.grid(row = 59, column=45 , columnspan = 20, padx = 1, pady = 1, sticky = 'n')

            aantimerbox.grid(row = 60, column=45 , columnspan = 20, padx = 1, pady = 1, sticky = 'n')
            uittimerbox.grid(row = 61, column=45 , columnspan = 20, padx = 1, pady = 1, sticky = 'n')

            aanuitlabel.grid(row = 50, column = 260, columnspan = 40, padx = 1, pady = 1, sticky = 'w')
            s1box = Checkbutton(self)
            s1box.grid(row = 55, column=280 , columnspan = 40, padx = 1, pady = 1, sticky = 'n')
            s2box = Checkbutton(self)
            s2box.grid(row = 56, column=280 , columnspan = 40, padx = 1, pady = 1, sticky = 'n')
            s3box = Checkbutton(self)
            s3box.grid(row = 57, column=280 , columnspan = 40, padx = 1, pady = 1, sticky = 'n')
            s4box = Checkbutton(self)
            s4box.grid(row = 58, column=280 , columnspan = 40, padx = 1, pady = 1, sticky = 'n')
            s5box = Checkbutton(self)
            s5box.grid(row = 59, column=280 , columnspan = 40, padx = 1, pady = 1, sticky = 'n')
            s6box = Checkbutton(self)
            s6box.grid(row = 60, column=280 , columnspan = 40, padx = 1, pady = 1, sticky = 'n')
            s7box = Checkbutton(self)
            s7box.grid(row = 61, column=280 , columnspan = 40, padx = 1, pady = 1, sticky = 'n')
            print(x)
        """
        nb.add(self, text='Properties')
        
        print(sensors)

