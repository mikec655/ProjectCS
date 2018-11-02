from tkinter import Entry, Label, Checkbutton, Button, StringVar, OptionMenu
from tkinter.ttk import Frame

class Properties(Frame):

    def __init__(self, master=None):
        super().__init__(master)

    def propertieFrame(self, nb, properties, sensors, aansturingen):
        self.properties = properties
        rolluiktitel = Label(self.properties, text="Selecteer een rolluik:")
        rolluiktitel.grid(row = 0, column = 0, columnspan = 25, padx = 1, pady = 5, sticky = 'w')
        rolluiktitel.config(font=("Times new roman", 14))
        #sensors.append("moooi")
        hernoemtitel = Label(self.properties, text="hernoem de module:")
        hernoemtitel.grid(row = 2, column = 0, columnspan = 25, padx = 1, pady = 5, sticky = 'w')
        hernoemtitel.config(font=("Times new roman", 12))
        
        self.var = StringVar(self.properties)
        self.var.set("Selecteer motor module")
        self.w = OptionMenu(self.properties, self.var, sensors)### hier moet motormodulelijst komen
        self.w.grid(row = 1, column = 0, columnspan = 40, padx = 1, pady = 1, sticky = 'w')
        
        
        for x in sensors:
            
            grenswaardelabel = Label(self.properties, text="Grenswaarde")
            grenswaardebox1 = Entry(self.properties)
            grenswaardebox2 = Entry(self.properties)
            grenswaardebox3 = Entry(self.properties)
            grenswaardebox4 = Entry(self.properties)
            grenswaardebox5 = Entry(self.properties)

            aantimerlabel = Label(self.properties, text="Automatisch aan")
            uittimerlabel = Label(self.properties, text="Automatisch uit")

            aantimerbox = Entry(self.properties)
            uittimerbox = Entry(self.properties)

            aanuitlabel = Label(self.properties, text="Aan uit")

            sensor1label = Label(self.properties, text="Licht Sensor",background='white')
            sensor2label = Label(self.properties, text="Temperatuur Sensor")
            sensor3label = Label(self.properties, text="SensorNaam")
            sensor4label = Label(self.properties, text="SensorNaam")
            sensor5label = Label(self.properties, text="SensorNaam")

          

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
            s1box = Checkbutton(self.properties)
            s1box.grid(row = 55, column=280 , columnspan = 40, padx = 1, pady = 1, sticky = 'n')
            s2box = Checkbutton(self.properties)
            s2box.grid(row = 56, column=280 , columnspan = 40, padx = 1, pady = 1, sticky = 'n')
            s3box = Checkbutton(self.properties)
            s3box.grid(row = 57, column=280 , columnspan = 40, padx = 1, pady = 1, sticky = 'n')
            s4box = Checkbutton(self.properties)
            s4box.grid(row = 58, column=280 , columnspan = 40, padx = 1, pady = 1, sticky = 'n')
            s5box = Checkbutton(self.properties)
            s5box.grid(row = 59, column=280 , columnspan = 40, padx = 1, pady = 1, sticky = 'n')
            s6box = Checkbutton(self.properties)
            s6box.grid(row = 60, column=280 , columnspan = 40, padx = 1, pady = 1, sticky = 'n')
            s7box = Checkbutton(self.properties)
            s7box.grid(row = 61, column=280 , columnspan = 40, padx = 1, pady = 1, sticky = 'n')
            print(x)

        nb.add(self.properties, text='Properties')
        
        print(sensors)

