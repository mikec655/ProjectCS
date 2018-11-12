from tkinter import Entry, Label, Checkbutton, Button, StringVar, OptionMenu, ANCHOR, IntVar, messagebox
from myframe import MyFrame
import settings_editor

#Maakt het properties frame aan.
#Hierin worden lijsten opgebouwd met daarin aangesloten ernsoren en aansturingen.
#De lijsten worden geupdate vanuit de mainloop door update() uit te voeren.

class Properties(MyFrame):

    def __init__(self, sensors, aansturingen, nb):
        super().__init__(nb, "Properties")
        #lijst van sensorblok objecten.
        self.knoplijst=[]
        #kopie lijst van aangesloten modules.
        self.sensors=sensors.copy()
        self.aansturingen=aansturingen.copy()
        
        self.waardeoption = StringVar(self)
        self.waardeoption.set("Selecteer motor module")
        self.aansturing_id = ''
        self.updownlength = 5

        #Maakt optiemenu voor aansturingen aan.
        self.optiemenu(self.aansturingen)  

        rolluiktitel = Label(self, text="Selecteer een rolluik:", background='white')
        rolluiktitel.grid(row = 0, column = 0, columnspan = 1, padx = 1, pady = 5)
        rolluiktitel.config(font=("Times new roman", 14, "bold"))

        hernoemtitel = Label(self, text="Hernoem de module:", background='white')
        hernoemtitel.grid(row = 2, column = 0, columnspan = 1,pady = 2)
        hernoemtitel.config(font=("Times new roman", 12))
        self.hernoemen = Entry(self)
        self.hernoemen.grid(row = 2, column= 12 , columnspan = 1, padx = 20, pady = 1)

        onzichtbaar = Label(self, text="", background='white')
        onzichtbaar.grid(row = 3, column = 0, columnspan = 1,pady = 2)

        autotitel = Label(self, text="Automatische besturing:", background='white')
        autotitel.grid(row = 5, column = 0, columnspan = 1,pady = 2)
        autotitel.config(font=("Times new roman", 12, "bold"))
        
        downtimertitel = Label(self, text="Omlaagtijd:", background='white')
        downtimertitel.grid(row = 6, column = 0, columnspan = 1,pady = 1)
        downtimertitel.config(font=("Times new roman", 12))
        self.down = Entry(self, validate="key")
        self.down.grid(row = 6, column= 12 , columnspan = 1, padx = 1, pady = 1)
        self.down['validatecommand'] = (self.down.register(self.testupdown),'%P','%d')

        uptimertitel = Label(self, text="Omhoogtijd:", background='white')
        uptimertitel.grid(row = 7, column = 0, columnspan = 1,pady = 1)
        uptimertitel.config(font=("Times new roman", 12))
        self.up = Entry(self, validate="key")
        self.up.grid(row = 7, column= 12 , columnspan = 1, padx = 1, pady = 1)
        self.up['validatecommand'] = (self.up.register(self.testupdown),'%P','%d')

        timerformatlabel = Label(self, text="Format: hh:mm ", background='white')
        timerformatlabel.grid(row = 8, column = 12, columnspan = 1,  sticky='w')

        self.sensortitel = Label(self, text= 'Uitrollen als: ', background='white')
        self.sensortitel.grid(row = 0, column = 80, columnspan = 1, padx = 1, pady = 5)
        self.sensortitel.config(font=("Times new roman", 14))
        
        self.sensortitel2 = Label(self, text= 'Aan/Uit', background='white')
        self.sensortitel2.grid(row = 0, column = 120, columnspan = 1, padx = 1, pady = 5)
        self.sensortitel2.config(font=("Times new roman", 14))

        self.okbutton = Button(self, text="Opslaan", command=self.savesettings)
        self.okbutton.grid(row = 50, column = 120, columnspan = 1, padx = 1, pady = 5)
        self.bouwsensorblok(self.sensors)

        waardelimiet = Label(self, text="*Max temp = 99°C, Max Lux = 9999.", background='white')
        waardelimiet.grid(row = 700, column = 0, columnspan = 1, padx = 1, pady = 5)
        waardelimiet.config(font=("Times new roman", 11))

        uitleg = Label(self, text="* indien gebruiken niet is aangevinkt:\n instelling verwijderd voor aansturing.", background='white')
        uitleg.grid(row = 701, column = 0, columnspan = 1, padx = 1, pady = 5)
        uitleg.config(font=("Times new roman", 11))


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
        self.selecteermotor = OptionMenu(self, self.waardeoption, *self.x, )
        self.selecteermotor.grid(row = 1, column = 0, columnspan = 1, padx = 1, pady = 1)

    #wordt vanuit de mainloop aangeroepen, dit zorgt voor het weergeven van verandering in aangesloten sensoren/aansturingen.
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
       
    #Hiermee worden de ingevulde waardes per sensor toegevoegd aan de .json file.
    #Dit gebeurt bij de geselecteerde aansturingsmodule.
    #Ook worden er errorbox aangemaakt indien er geen sensor is aangesloten of er geen aansturing is.
    #Ook is het hernoemen van de aansturingsmodule hierin verwerkt. 
    def savesettings(self):
        settings = settings_editor.readSettings()
        
        for A in self.aansturingen:
            if str(self.waardeoption.get()) == A.name: #zoeken vanaf aansturing naam > aansturing id.
                self.aansturing_id = A.id
                
                if len(self.hernoemen.get()) > 0:
                    settings['aansturingen'][self.aansturing_id]['name'] = self.hernoemen.get()
                    settings_editor.writeSettings(settings) 
                
                if len(self.up.get()) ==5 and len(self.down.get()) == 5:
                    settings['aansturingen'][self.aansturing_id]['down'] = self.down.get()
                    settings_editor.writeSettings(settings) 
                    settings['aansturingen'][self.aansturing_id]['up'] = self.up.get()
                    settings_editor.writeSettings(settings) 
        
        #schrijf en delete .json file entrys opbasis van aangevinkte checkbox en volledig ingevuld.
        for x in self.knoplijst:
            try:
                if x.checkboxwaarde.get() == 1 and len(x.sensorwaardeblok.get()) > 0:
                    settings['aansturingen'][self.aansturing_id]['sensor_value'][x.sensor.id] = x.functiewaardeblokwaarde + str(float(x.sensorwaardeblok.get()))
                else:
                    del settings['aansturingen'][self.aansturing_id]['sensor_value'][x.sensor.id]
            except KeyError:
                pass
    
        settings_editor.writeSettings(settings) 

    #invul limiet automatische besturing
    def testupdown(self,inStr,acttyp):
        if len(inStr) > self.updownlength:
            return False
        else:
            return True

#wordt per aangesloten sensor aangemaakt.
#dit bevat de sensornaam, een invul veld en een checkbox.
#de input worden gelimiteerd tot cijfer en een max lengte die afhangt van sensortype.
class sensorblok():

    def __init__(self,frame,sensor,rij):
        self.frame=frame
        self.widget=[]
        self.variabelevoorrijenaanpassen = rij
        self.functielength = 1
        self.maxlength = 0
        if sensor.type == '_TEMP':
            self.maxlength = 2
        else:
            self.maxlength = 4

        
        self.sensor = sensor
        self.sensorwaarde =''
        self.checkboxwaarde = IntVar()
        self.functiewaardeblokwaarde = ">"
     
        self.sensortitel = ''
        self.sensortitel = Label( self.frame, text= str(self.sensor.name), background='white')
        self.sensortitel.grid(row = self.variabelevoorrijenaanpassen, column = 60, columnspan = 1, padx = 1, pady = 5)
        self.sensortitel.config(font=("Times new roman", 14))

        self.functiewaardeblok = Button(self.frame, text="hoger is als", command=self.setfunctiewaardeblok)
        self.functiewaardeblok.grid(row=self.variabelevoorrijenaanpassen, column= 80, padx = 1, pady = 1)
        #self.functiewaardeblok.config(width = 1)
        self.vcmd = (self.functiewaardeblok.register(self.onValidate),'%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')

        self.sensorwaardeblok = Entry( self.frame, validate="key")
        self.sensorwaardeblok.grid(row=self.variabelevoorrijenaanpassen, column=98, columnspan = 1, padx = 1, pady = 1)
        self.sensorwaardeblok['validatecommand'] = (self.sensorwaardeblok.register(self.testVal),'%P','%d')
        self.sensorwaardeblok.bind('<Return>', lambda _: self.setsensorwaarde())

        vcmd = (self.frame.register(self.onValidate),
                    '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')

        # self.functiewaardeblok = Entry(self.frame, validate="key", validatecommand=vcmd)
        # self.functiewaardeblok.grid(row=self.variabelevoorrijenaanpassen, column= 98, columnspan = 1, padx = 1, pady = 1)
        # self.functiewaardeblok.config(width = 1)
        # self.vcmd = (self.functiewaardeblok.register(self.onValidate),'%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')

        self.checkbox = Checkbutton( self.frame, variable= self.checkboxwaarde, background='white')
        self.checkbox.grid(row=self.variabelevoorrijenaanpassen, column= 120 , columnspan = 1, padx = 1, pady = 1)

        self.widget.append(self.sensortitel)
        self.widget.append(self.sensorwaardeblok)
        self.widget.append(self.checkbox)
        self.widget.append(self.functiewaardeblok)

    def setfunctiewaardeblok(self):
        if self.functiewaardeblokwaarde == ">":
            self.functiewaardeblokwaarde = "<"
            self.functiewaardeblok['text'] = "lager is als"
        else:
            self.functiewaardeblokwaarde = ">"
            self.functiewaardeblok['text'] = "hoger is als"

    def setsensorwaarde(self):
        self.sensorwaarde = self.sensorwaardeblok.get()
    
    #wordt gebruikt om het sensorblok te verwijderen indien sensor wordt losgekoppeld
    def deletewidgets(self):
        for widget in self.widget:
            widget.destroy()

    #Hiermee limiteer je input op entry boxen tot cijfers only en bepaalde lengte.
    #Deze wordt aangeroept per cijfer die getypt wordt in het invulveld.
    def testVal(self,inStr,acttyp):
        if len(inStr) > self.maxlength:
            return False
        if acttyp == '1': #insert
            if not inStr.isdigit():
                return False
        return True
    
    #Dit is check voor het groter of kleiner dan blok.
    #Deze wordt aangeroept per < of > die getypt wordt in het invulveld.
    def onValidate(self, d, i, P, s, S, v, V, W):
        if i == "0":
            return True
        else:
            return False


