from tkinter import Entry, Label, Checkbutton, Button, StringVar, OptionMenu, ANCHOR
from tkinter.ttk import Frame
import settings_editor

variabelevoorrijenaanpassen = 1 #wordt gebruikt om row aan te passen per sensor
knoplijst=[]

class Properties(Frame):

    def __init__(self, master=None):
        super().__init__(master)
        
        

    def propertieFrame(self, nb, sensors, aansturingen):
        self.x= [1,2,3,4]
        self.sensors=sensors.copy()
        print(sensors)

        if len(aansturingen)==0:
            pass
        else:
            self.x=[]
            for instantie in aansturingen:
                self.x.append(instantie.name)
                
        rolluiktitel = Label(self, text="Selecteer een rolluik:")
        rolluiktitel.grid(row = 0, column = 0, columnspan = 1, padx = 1, pady = 5)
        rolluiktitel.config(font=("Times new roman", 14))
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

        b = Button(self, text="OK")
        b.config(row = 50, column = 100, columnspan = 1, padx = 1, pady = 5)

        for sensorinstantie in self.sensors:
            knoplijst.append(sensorblok(sensorinstantie))

        for elke in knoplijst:
            elke.sensorlijst()

        print(knoplijst)

        
        """
        for sensorinstantie in self.sensors:

            

            self.sensortitel = Label(self, text= str(sensorinstantie.name))
            self.sensortitel.grid(row = self.variabelevoorrijenaanpassen, column = 60, columnspan = 1, padx = 1, pady = 5)
            self.sensortitel.config(font=("Times new roman", 14))
    

            self.sensorwaarde = Entry(self)
            self.sensorwaarde.grid(row=self.variabelevoorrijenaanpassen, column= 80, columnspan = 1, padx = 1, pady = 1)
            

            self.checkbox = Checkbutton(self)
            self.checkbox.grid(row=self.variabelevoorrijenaanpassen, column= 100 , columnspan = 1, padx = 1, pady = 1)

            self.variabelevoorrijenaanpassen +=1
        """


        nb.add(self, text='Properties')
        
       


            
                

class sensorblok():

    def __init__(self,sensor):
        global variabelevoorrijenaanpassen
        self.sensorwaarde = ''
        self.sensornaam = sensor.name
        
        self.sensorwaarde =''
        self.checkbox = ''
        self.sensortitel = ''
        
        

    def sensorlijst(self):
            global variabelevoorrijenaanpassen
            self.sensortitel = Label(self, text= str(self.sensornaam))
            self.sensortitel.grid(row = variabelevoorrijenaanpassen, column = 60, columnspan = 1, padx = 1, pady = 5)
            self.sensortitel.config(font=("Times new roman", 14))
    

            self.sensorwaarde = Entry(self)
            self.sensorwaarde.grid(row=variabelevoorrijenaanpassen, column= 80, columnspan = 1, padx = 1, pady = 1)
            

            self.checkbox = Checkbutton(self)
            self.checkbox.grid(row=variabelevoorrijenaanpassen, column= 100 , columnspan = 1, padx = 1, pady = 1)

            variabelevoorrijenaanpassen +=1
    
    

    """
    def checksensor(self, sensors):
        sensor_name = ""
        naming_dict = {
            "_TEMP": "Temperatuursensor", 
            "_LGHT": "Lichtsensor"
            } 
        settings = settings_editor.readSettings()
        try:
            sensor_name = settings["sensor_name"][self.id]["name"]
        except KeyError:
            if self.sensor_type in naming_dict.keys():
                sensor_number = len([sensor["name"] for sensor in settings["sensor_name"].values() if sensor["type"] == self.sensor_type]) + 1
                sensor_name += naming_dict[self.sensor_type] + str(sensor_number)
                settings["sensor_name"][self.id] = {}
                settings["sensor_name"][self.id]["name"] = sensor_name
                settings["sensor_name"][self.id]["type"] = self.sensor_type
                settings_editor.writeSettings(settings)      """    
