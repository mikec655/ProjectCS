from tkinter import Entry, Label, Checkbutton, Button, StringVar, OptionMenu
from tkinter.ttk import Frame

class properties(Frame):

    def __init__(self, master=None):
        super().__init__(master)

    def propertieFrame(self, nb, properties,sensors, aansturingen):
        rolluiktitel = Label(properties, text="Selecteer een rolluik:")
        rolluiktitel.grid(row = 0, column = 0, columnspan = 25, padx = 1, pady = 5, sticky = 'w')
        rolluiktitel.config(font=("Times new roman", 14))
        #sensors.append("moooi")
        hernoemtitel = Label(properties, text="hernoem de module:")
        hernoemtitel.grid(row = 2, column = 0, columnspan = 25, padx = 1, pady = 5, sticky = 'w')
        hernoemtitel.config(font=("Times new roman", 12))
        
        self.var = StringVar(properties)
        self.var.set("Selecteer motor module")
        self.w = OptionMenu(properties, self.var, sensors)### hier moet motormodulelijst komen
        self.w.grid(row = 1, column = 0, columnspan = 40, padx = 1, pady = 1, sticky = 'w')
        
        
        for x in sensors:
            
            grenswaardelabel = Label(properties, text="Grenswaarde")
            grenswaardebox1 = Entry(properties)
            grenswaardebox2 = Entry(properties)
            grenswaardebox3 = Entry(properties)
            grenswaardebox4 = Entry(properties)
            grenswaardebox5 = Entry(properties)

            aantimerlabel = Label(properties, text="Automatisch aan")
            uittimerlabel = Label(properties, text="Automatisch uit")

            aantimerbox = Entry(properties)
            uittimerbox = Entry(properties)

            aanuitlabel = Label(properties, text="Aan uit")

            sensor1label = Label(properties, text="Licht Sensor",background='white')
            sensor2label = Label(properties, text="Temperatuur Sensor")
            sensor3label = Label(properties, text="SensorNaam")
            sensor4label = Label(properties, text="SensorNaam")
            sensor5label = Label(properties, text="SensorNaam")

          

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
            s1box = Checkbutton(properties)
            s1box.grid(row = 55, column=280 , columnspan = 40, padx = 1, pady = 1, sticky = 'n')
            s2box = Checkbutton(properties)
            s2box.grid(row = 56, column=280 , columnspan = 40, padx = 1, pady = 1, sticky = 'n')
            s3box = Checkbutton(properties)
            s3box.grid(row = 57, column=280 , columnspan = 40, padx = 1, pady = 1, sticky = 'n')
            s4box = Checkbutton(properties)
            s4box.grid(row = 58, column=280 , columnspan = 40, padx = 1, pady = 1, sticky = 'n')
            s5box = Checkbutton(properties)
            s5box.grid(row = 59, column=280 , columnspan = 40, padx = 1, pady = 1, sticky = 'n')
            s6box = Checkbutton(properties)
            s6box.grid(row = 60, column=280 , columnspan = 40, padx = 1, pady = 1, sticky = 'n')
            s7box = Checkbutton(properties)
            s7box.grid(row = 61, column=280 , columnspan = 40, padx = 1, pady = 1, sticky = 'n')
            print(x)

        nb.add(properties, text='properties')
        
        print(sensors)

