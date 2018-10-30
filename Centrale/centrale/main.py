from tkinter import Tk, Label, Entry, Button, Checkbutton
from tkinter import ttk
from sensors import Sensor, SerialException, list_ports
import login
import properties as prprts
import time
import threading



class Application(Tk):

    def __init__(self):
        # initialise a window.
        super().__init__()
        self.sensors = []
        self.threads = []
        self.frames = []
        self.makeFrame()

    def makeFrame(self):
        self.config(background='white')
        self.geometry("1000x700")
        self.title("Application")
        self.nb = ttk.Notebook(self)

        login0 = ttk.Frame(self.nb)
        rpropertie = prprts.properties()
        loginFrame = login.Login()    
        loginFrame.frame(login0, self.nb)

        while True:
            self.update()
            self.check_for_sensors(self.nb)
            print(loginFrame.loggedin)

            if loginFrame.loggedin == True:
                print(908876)
                loginFrame.loggedin = False
                instellingen = ttk.Frame(self.nb)
                rpropertie.propertieFrame(self.nb ,instellingen)

            self.nb.pack(expand=1, fill="both")



    def check_for_sensors(self, nb):
        available_ports = list_ports.comports()
        for port in available_ports:
            # Als sensor niet in de sensors staat voeg toe
            if port.device not in [sensor.port for sensor in self.sensors]:
                time.sleep(1)
                s = Sensor(port.device, self.sensors)
                self.sensors.append(s)
                nb.add(s.graph, text=s.name)
        for sensor in self.sensors:
            # Als sensor niet meer aangesloten staat verwijder van sensor
            if sensor.port not in [port.device for port in available_ports]:
                sensor.graph.destroy()
                sensor.stop()
                self.sensors.remove(sensor)
                
    
if __name__ == '__main__':
    app = Application()