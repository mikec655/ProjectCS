from tkinter import Entry, Label, Checkbutton, Button

class properties:

    def __init__(self):
        pass

    def propertieFrame(self, nb, properties):
        rolluiklabel = Label(properties, text="Rolluik:")
        rolluiklabel.config(font=("Times new roman", 18))
        
        maxuitrollabel = Label(properties, text="Maximale uitrol:")
        maxuitrolbox = Entry(properties)

        minuitrollabel = Label(properties, text="Maximale Inrol:")
        minuitrolbox = Entry(properties)

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

        sensor1label = Label(properties, text="Licht Sensor")
        sensor2label = Label(properties, text="Temperatuur Sensor")
        sensor3label = Label(properties, text="SensorNaam")
        sensor4label = Label(properties, text="SensorNaam")
        sensor5label = Label(properties, text="SensorNaam")

        luikopenlabel = Label(properties, text="Rol luik open")
        luikdichtlabel = Label(properties, text="Rol luik dicht")

        rolluiklabel.grid(row = 0, column = 0, columnspan = 50, padx = 1, pady = 20, sticky = 'w')

        maxuitrollabel.grid(row=5, column=0 , columnspan = 20, padx = 1, pady = 1, sticky = 'w')
        maxuitrolbox.grid(row = 5, column=30 , columnspan = 20, padx = 1, pady = 1, sticky = 'n')

        minuitrollabel.grid(row=25, column=0 , columnspan = 20, padx = 1, pady = 1, sticky = 'w')
        minuitrolbox.grid(row = 25, column=30 , columnspan = 20, padx = 1, pady = 1, sticky = 'n')

        sensor1label.grid(row = 55, column = 0, columnspan = 40, padx = 1, pady = 1, sticky = 'w')
        sensor2label.grid(row = 56, column = 0, columnspan = 40, padx = 1, pady = 1, sticky = 'w')
        sensor3label.grid(row = 57, column = 0, columnspan = 40, padx = 1, pady = 1, sticky = 'w')
        sensor4label.grid(row = 58, column = 0, columnspan = 40, padx = 1, pady = 1, sticky = 'w')
        sensor5label.grid(row = 59, column = 0, columnspan = 40, padx = 1, pady = 1, sticky = 'w')

        aantimerlabel.grid(row = 60, column = 0, columnspan = 40, padx = 1, pady = 1, sticky = 'w')
        uittimerlabel.grid(row = 61, column = 0, columnspan = 40, padx = 1, pady = 1, sticky = 'w')

        luikopenlabel.grid(row = 62, column = 0, columnspan = 40, padx = 1, pady = 1, sticky = 'w')
        luikdichtlabel.grid(row = 63, column = 0, columnspan = 40, padx = 1, pady = 1, sticky = 'w')

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
        s8box = Checkbutton(properties)
        s8box.grid(row = 62, column=280 , columnspan = 40, padx = 1, pady = 1, sticky = 'n')
        s9box = Checkbutton(properties)
        s9box.grid(row = 63, column=280 , columnspan = 40, padx = 1, pady = 1, sticky = 'n')

        nb.add(properties, text='properties')