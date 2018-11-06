from tkinter import Entry, Label, Checkbutton, Button, StringVar, OptionMenu, ANCHOR, IntVar
from myframe import MyFrame
import settings_editor




class Properties(MyFrame):

    def __init__(self, sensors, aansturingen, nb):
        super().__init__(nb, "Properties")
        self.knoplijst=[]
        self.x= [1,2,3,4]
        self.sensors=sensors.copy()
        self.aansturingen=aansturingen.copy()
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
        """ 
        minuitroltitel = Label(self, text="minimale uitrol lengte:")
        minuitroltitel.grid(row = 3, column = 0, columnspan = 1,pady = 5)
        minuitroltitel.config(font=("Times new roman", 12))
        self.minuitrol = Entry(self)
        self.minuitrol.grid(row = 3, column= 12 , columnspan = 1, padx = 1, pady = 1)

        maxuitroltitel = Label(self, text="maximale uitrol lengte:")
        maxuitroltitel.grid(row = 4, column = 0, columnspan = 1,pady = 5)
        maxuitroltitel.config(font=("Times new roman", 12))
        self.maxuitrol = Entry(self)
        self.maxuitrol.grid(row = 4, column= 12 , columnspan = 1, padx = 1, pady = 1)
        """
        self.sensortitel = Label(self, text= 'Grenswaarde:')
        self.sensortitel.grid(row = 0, column = 80, columnspan = 1, padx = 1, pady = 5)
        self.sensortitel.config(font=("Times new roman", 14))

        self.sensortitel = Label(self, text= 'gebruiken:')
        self.sensortitel.grid(row = 0, column = 100, columnspan = 1, padx = 1, pady = 5)
        self.sensortitel.config(font=("Times new roman", 14))

        self.okbutton = Button(self, text="Opslaan", command=self.savesettings)
        self.okbutton.grid(row = 50, column = 100, columnspan = 1, padx = 1, pady = 5)

        i = 0
        while i < len(self.sensors):
            
            self.knoplijst.append(  sensorblok(self, self.sensors[i],i+1 )  )
            i += 1
        
          
    def savesettings(self):
        print("dikkesave")

        settings = settings_editor.readSettings()
        #min en max uitrol lengte
        #motor id voor json file
       
        # if self.var.get() != "Selecteer motor module":
        #     print(self.var.get())

        aansturing_id = "75435353138351F08050"
        for A in self.aansturingen:
            if str(self.var.get()) == A.name: #zoeken vanaf aansturing naam > aansturing id.
                aansturing_id = A.id
                print(A.id + "joooo") # aansturingid voor json file
        
        for x in self.knoplijst:
                if x.checkboxwaarde.get() == 1:
                    settings['aansturingen'][aansturing_id]['sensor_value'][x.sensor.id] = float(x.sensorwaardeblok.get())
                    print(x.sensor.name)    #sensor naam voor json file
                    print(x.sensor.id) #sensor id voor jsonfile
                    print(x.sensorwaardeblok.get())  #ingevulde waarde voor json file
            
        settings_editor.writeSettings(settings) 

class sensorblok():

    def __init__(self,frame,sensor,rij):
        self.frame=frame
     
        self.variabelevoorrijenaanpassen = rij

        self.sensor = sensor
        self.sensorwaarde =''
        self.checkboxwaarde = IntVar()
     
        self.sensortitel = ''
        self.sensortitel = Label( self.frame, text= str(self.sensor.name))
        self.sensortitel.grid(row = self.variabelevoorrijenaanpassen, column = 60, columnspan = 1, padx = 1, pady = 5)
        self.sensortitel.config(font=("Times new roman", 14))

        self.sensorwaardeblok = Entry( self.frame)
        self.sensorwaardeblok.grid(row=self.variabelevoorrijenaanpassen, column= 80, columnspan = 1, padx = 1, pady = 1)
        
        self.sensorwaardeblok.bind('<Return>', lambda _: self.setsensorwaarde())

        self.checkbox = Checkbutton( self.frame, variable= self.checkboxwaarde)
        self.checkbox.grid(row=self.variabelevoorrijenaanpassen, column= 100 , columnspan = 1, padx = 1, pady = 1)

        

    def setsensorwaarde(self):
        self.sensorwaarde = self.sensorwaardeblok.get()
        print(self.sensorwaarde)

   

