import sys
from tkinter import Tk, Label, Entry, Button, Checkbutton, TclError
from tkinter import ttk
from serial import Serial, SerialException
from serial.tools import list_ports
from aansturing import Aansturing
from time import sleep
from sensors import Sensor, SerialException, list_ports
import loginscherm
import properties as prprts
import time
import threading


class Application(Tk):
    __instance = None

    def __init__(self):
        # initialise a window.
        super().__init__()
        if not Application.__instance:
            print("Ik heb al een instantie.")
        else:
            print('Ik heb nog geen instantie')
        self.sensors = []
        self.aansturingen = []
        self.threads = []
        self.frames = []
        self.naamFrame = []
        self.config(background='white')
        self.geometry("1000x700")
        self.title("Application")
        self.nb = ttk.Notebook(self)
        self.homeFrame()
        self.apploop()
   
    @classmethod 
    def getInstance(cls):
        if not cls.__instance:
            cls.__instance = Application()
        return cls.__instance

    def homeFrame(self):
        self.home = ttk.Frame(self.nb)
        inrol_button = Button(self.home, text="Inrollen", command=self.inrollen)
        uitrol_button = Button(self.home, text="Uitrollen", command=self.uitrollen)
        inrol_button.grid()
        uitrol_button.grid()
        # self.nb.add(home, text='Home')
        self.voegFrameToe(self.home, 'Home')
        self.maakFrame()

    def apploop(self):
        self.login0 = ttk.Frame(self.nb)
        self.rpropertie = prprts.Properties()
        self.rproperte = prprts.Properties()
        loginFrame = loginscherm.Login()    
        loginFrame.frame(self.login0, self.nb)
        self.voegFrameToe(self.login0, 'Login')
        self.maakFrame()

        while True:
            try:
                self.update()
                self.check_for_devices()
                self.nb.pack(expand=1, fill="both")
                if loginFrame.loggedin == 'I':
	                loginFrame.loggedin = ''
	                self.rpropertie.propertieFrame(self.nb, self.sensors, self.aansturingen)
                elif loginFrame.loggedin == 'U':
                    loginFrame.loggedin = ''
                    try:
                        self.rpropertie.destroy()
                        self.verwijderFrame(self.home, 'Home')
                    except:
                        print('error')
            except TclError:
                try:
                    sys.exit(1)
                except Exception:
                    print("programma afgesloten")
                break

    def check_for_devices(self):
        available_ports = list_ports.comports()
        for port in available_ports:
            # Als sensor niet in de sensors staat voeg toe
            if port.device not in [sensor.port for sensor in self.sensors] and \
            port.device not in [aansturing.port for aansturing in self.aansturingen]:
                self.init_device(port.device)
        for sensor in self.sensors:
            # Als sensor niet meer aangesloten staat verwijder van sensor
            if sensor.port not in [port.device for port in available_ports]:
                sensor.graph.destroy()
                sensor.stop()
                self.sensors.remove(sensor)
        for aansturing in self.aansturingen:
            # Als aansturing niet meer aangesloten staat verwijder aansturing
            if aansturing.port not in [port.device for port in available_ports]:
                self.aansturingen.remove(aansturing)
                
    def init_device(self, comport):
        ser = Serial(comport, 19200, timeout=5)
        sleep(2)
        ser.write(b"_INIT\n")
        device_type = ser.readline().decode("UTF-8")
        ser.write(b"_CONN\n")
        if device_type == "_MTR\n":
            a = Aansturing(ser)
            self.aansturingen.append(a)
        elif device_type == "":
            pass
        else:
            s = Sensor(ser, device_type, self.sensors)
            self.sensors.append(s)
            self.nb.add(s.graph, text=s.name)
        

    def uitrollen(self):
        for aansturing in self.aansturingen:
            aansturing.uitrollen()

    def inrollen(self):
        for aansturing in self.aansturingen:
            aansturing.inrollen()

    def voegFrameToe(self, frame, name):
        self.frames.append(frame)
        self.naamFrame.append(name)

    def maakFrame(self):
        for i in self.frames: 
            self.frame_name = i
        for x in self.naamFrame:
            self.nb.add(self.frame_name,text=x)
    
    def verwijderFrame(self, naamFrame, naam):
        for x in self.frames:
            if x == naamFrame:
                self.frames.remove(x)
        for y in self.naamFrame:
            if y == naam:
                self.naamFrame.remove(y)

if __name__ == '__main__':
    app = Application()
    app2 = Application()
    print("app: %s, app2: %s" % (app.getInstance(),app2.getInstance()))
