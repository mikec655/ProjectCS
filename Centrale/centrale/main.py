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

    def __init__(self):
        # initialise a window.
        super().__init__()
        self.sensors = []
        self.aansturingen = []
        self.threads = []
        self.frames = []
        self.config(background='white')
        self.geometry("1000x700")
        self.title("Application")
        self.nb = ttk.Notebook(self)
        self.home()
        self.apploop()

    def home(self):
        home = ttk.Frame(self.nb)
        inrol_button = Button(home, text="Inrollen", command=self.inrollen)
        uitrol_button = Button(home, text="Uitrollen", command=self.uitrollen)
        inrol_button.grid()
        uitrol_button.grid()
        self.nb.add(home, text='Home')

    def apploop(self):
        login0 = ttk.Frame(self.nb)
        self.rpropertie = prprts.Properties()
        loginFrame = loginscherm.Login()    
        loginFrame.frame(login0, self.nb)

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
                    print(1)
                    self.rpropertie.destroy()
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

if __name__ == '__main__':
    app = Application()