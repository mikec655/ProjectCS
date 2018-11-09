from tkinter import Entry, Label, Checkbutton, Button, StringVar, OptionMenu, ANCHOR, IntVar
from myframe import MyFrame
import settings_editor

class Properties(MyFrame):

    def __init__(self, sensors, aansturingen, nb):
        super().__init__(nb, "Properties")
        
        self.knoplijst=[]
        
        self.x=[1,2,3,4]
        self.sensors=sensors.copy()
        self.aansturingen=aansturingen.copy()

        self.waardeoption = StringVar(self)
        self.waardeoption.set("Selecteer motor module")
        print(sensors)

        self.aansturing_id = ''

        
        self.optiemenu(self.aansturingen)  

        rolluiktitel = Label(self, text="Selecteer een rolluik:", background='white')
        rolluiktitel.grid(row = 0, column = 0, columnspan = 1, padx = 1, pady = 5)
        rolluiktitel.config(font=("Times new roman", 14))

        hernoemtitel = Label(self, text="hernoem de module:", background='white')
        hernoemtitel.grid(row = 2, column = 0, columnspan = 1,pady = 5)
        hernoemtitel.config(font=("Times new roman", 12))
        
        
        self.hernoemen = Entry(self)
        self.hernoemen.grid(row = 2, column= 12 , columnspan = 1, padx = 1, pady = 1)

        self.sensortitel = Label(self, text= 'Grenswaarde:', background='white')
        self.sensortitel.grid(row = 0, column = 80, columnspan = 1, padx = 1, pady = 5)
        self.sensortitel.config(font=("Times new roman", 14))

        self.sensortitel = Label(self, text= 'gebruiken:', background='white')
        self.sensortitel.grid(row = 0, column = 100, columnspan = 1, padx = 1, pady = 5)
        self.sensortitel.config(font=("Times new roman", 14))

        self.okbutton = Button(self, text="Opslaan", command=self.savesettings)
        self.okbutton.grid(row = 50, column = 100, columnspan = 1, padx = 1, pady = 5)
        self.bouwsensorblok(self.sensors)

    #vult knoplijst met sensorobjecten, deze objecten bevatten de invulvelden.
    def bouwsensorblok(self, sensors):
        i = 0 # wordt gebruikt voor het itereren door de sensors lijst en om de rijen aan te passen waarop de invulvelden staan.
        while i < len(sensors):
            
            self.knoplijst.append(  sensorblok(self, self.sensors[i],i+1 )  )
            i += 1
    
    #maakt het optiemenu voor het aansturingsmodule aan.
    def optiemenu(self, aansturingen):
        
        if len(aansturingen)==0:
            self.x=["Sluit een motormodule aan"]
        else:
            self.x=[]
            for instantie in aansturingen:
                self.x.append(instantie.name)

        self.waardeoption.set("Selecteer motor module")
        self.selecteermotor = OptionMenu(self, self.waardeoption, *self.x, )### hier moet motormodulelijst komen
        self.selecteermotor.grid(row = 1, column = 0, columnspan = 1, padx = 1, pady = 1)

    #wordt vanuit de mainloop aangeroepen, dit zorgt voor het weergeven van verandering in aangesloten sensoren/aansturing
    def update(self, aansturingen, sensors):
        

        if aansturingen == self.aansturingen and sensors == self.sensors:
            return
        else:
            self.aansturingen = aansturingen.copy()
            self.sensors = sensors.copy()
            for instantie in self.knoplijst:
                instantie.deletewidgets()

            if self.selecteermotor:
                self.selecteermotor.destroy()

            self.bouwsensorblok(sensors)
            self.optiemenu(aansturingen)
       
          
    def savesettings(self):
        
        settings = settings_editor.readSettings()
        
        for A in self.aansturingen:
            if str(self.waardeoption.get()) == A.name: #zoeken vanaf aansturing naam > aansturing id.

                self.aansturing_id = A.id
                print("aansturing id = " + A.id ) # aansturingid voor json file
                
                if len(self.hernoemen.get()) > 0:
                    settings['aansturingen'][self.aansturing_id]['name'] = self.hernoemen.get()
                    settings_editor.writeSettings(settings) 
        
        if not self.aansturing_id:
            print('geen aansturing om sensor mee te geven')
####################
            #self.error = Label( self.frame, text= "Geen motor aangesloten")
            #self.error.grid(row = 300, column = 60, columnspan = 1, padx = 1, pady = 5)
            #self.error.config(font=("Times new roman", 14))
#################### klasse maken en in widgets zooi gooien
        
        
        for x in self.knoplijst:
                if x.checkboxwaarde.get() == 1:
                    settings['aansturingen'][self.aansturing_id]['sensor_value'][x.sensor.id] = float(x.sensorwaardeblok.get())
                    print(x.sensor.name)    #sensor naam voor json file
                    print(x.sensor.id) #sensor id voor jsonfile
                    print(x.sensorwaardeblok.get())  #ingevulde waarde voor json file
                else:
                    del settings['aansturingen'][self.aansturing_id]['sensor_value'][x.sensor.id]

            
        settings_editor.writeSettings(settings) 

class sensorblok():

    def __init__(self,frame,sensor,rij):
        self.frame=frame
        self.widget=[]
        self.variabelevoorrijenaanpassen = rij

        self.sensor = sensor
        self.sensorwaarde =''
        self.checkboxwaarde = IntVar()
     
        self.sensortitel = ''
        self.sensortitel = Label( self.frame, text= str(self.sensor.name), background='white')
        self.sensortitel.grid(row = self.variabelevoorrijenaanpassen, column = 60, columnspan = 1, padx = 1, pady = 5)
        self.sensortitel.config(font=("Times new roman", 14))

        self.sensorwaardeblok = Entry( self.frame)
        self.sensorwaardeblok.grid(row=self.variabelevoorrijenaanpassen, column= 80, columnspan = 1, padx = 1, pady = 1)
        
        self.sensorwaardeblok.bind('<Return>', lambda _: self.setsensorwaarde())

        self.checkbox = Checkbutton( self.frame, variable= self.checkboxwaarde, background='white')
        self.checkbox.grid(row=self.variabelevoorrijenaanpassen, column= 100 , columnspan = 1, padx = 1, pady = 1)

        self.widget.append(self.sensortitel)
        self.widget.append(self.sensorwaardeblok)
        self.widget.append(self.checkbox)

    def setsensorwaarde(self):
        self.sensorwaarde = self.sensorwaardeblok.get()
        print(self.sensorwaarde)
    
    def deletewidgets(self):
        for widget in self.widget:
            widget.destroy()
