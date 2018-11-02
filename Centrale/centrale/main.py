import sys
from tkinter import Tk, Label, Entry, Button, Checkbutton, TclError
from tkinter import ttk
from serial import Serial, SerialException
from serial.tools import list_ports
from aansturing import Aansturing
from time import sleep
from sensors import Sensor, SerialException, list_ports
import loginscherm
import myframe
import properties as prprts
import time
import threading


class Application(Tk):

    def __init__(self):
        # initialise a window.
        super().__init__()
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

    def homeFrame(self):
        self.home = ttk.Frame(self.nb)
        inrol_button = Button(self.home, text="Inrollen", command=self.inrollen)
        uitrol_button = Button(self.home, text="Uitrollen", command=self.uitrollen)
        inrol_button.grid()
        uitrol_button.grid()
        self.nb.add(self.home, text='Home')
        # self.voegFrameToe(self.home, 'Home')
        # self.maakFrame()

    def apploop(self):
        login = loginscherm.Login(self.nb)   
        # login.(self.login0, self.nb)
        # self.nb.add(self.login0, text='Login')
        # self.voegFrameToe(self.login0, 'Login')
        # self.maakFrame()

        while True:
            try:
                self.update()
                self.check_for_devices()
                self.nb.pack(expand=1, fill="both")
                if login.loggedin == 'I':
	                login.loggedin = ''
	                self.rpropertie.propertieFrame(self.nb, self.properties, self.sensors, self.aansturingen)
                elif login.loggedin == 'U':
                    login.loggedin = ''
                    try:
                        self.rpropertie.destroy()
                        self.verwijderFrame(self.home, 'Home')
                    except:
                        print('error')
            except TclError:
                try:
                    sys.exit(1)
                except SystemExit:
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

    # def voegFrameToe(self, frame, name):
    #     self.frames.append(frame)
    #     self.naamFrame.append(name)

    # def maakFrame(self):
    #     for i in self.frames: 
    #         self.frame_name = i
    #     for x in self.naamFrame:
    #         self.nb.add(self.frame_name,text=x)
    
    # def verwijderFrame(self, naamFrame, naam):
    #     for x in self.frames:
    #         if x == naamFrame:
    #             self.frames.remove(x)
    #     for y in self.naamFrame:
    #         if y == naam:
    #             self.naamFrame.remove(y)

if __name__ == '__main__':
    app = Application()