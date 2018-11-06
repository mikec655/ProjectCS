import sys
from tkinter import Tk, Label, Entry, Button, Checkbutton, TclError
from tkinter import ttk
from serial import Serial, SerialException
from serial.tools import list_ports
from aansturing import Aansturing
from time import sleep
from sensors import Sensor, SerialException, list_ports
from loginscherm import Login
from home import Home
from properties import Properties
from linegraph import Graph
import time
import threading


class Application(Tk):

    def __init__(self):
        # initialise a window.
        super().__init__()
        self.config(background='white')
        self.geometry("1000x700")
        self.title("Application")

        # control variables
        self.loggedin = False
        self.sensors = []
        self.old_sensors = []
        self.aansturingen = []
        self.threads = []
        self.frames = {}
        self.nb = ttk.Notebook(self)

        # Frames die nooit verdwijnen toevoegen
        self.frames['Home'] = Home(self.nb, self.aansturingen)
        self.frames['Login'] = Login(self.nb)
        self.applicationLoop()

    def applicationLoop(self):
        while True:
            try:
                self.update()
                self.check_for_devices()
                self.check_logged_in()
                self.nb.pack(expand=1, fill="both")
            except TclError:
                try:
                    sys.exit(1)
                except SystemExit:
                    print("programma afgesloten")
                break

    def check_logged_in(self):
        if self.frames['Login'].loggedin == 'I':
            self.loggedin = True
            self.frames['Login'].loggedin = ''
            self.frames['Properties'] = Properties(self.sensors, self.nb)
            for sensor in self.sensors:
                self.frames[sensor.name] = Graph(sensor, self.nb)
        elif self.frames['Login'].loggedin == 'U':
            self.loggedin = False
            self.frames['Login'].loggedin = ''
            for frame in self.frames.copy().keys():
                if frame not in ['Home', 'Login']:
                    try:
                        self.frames[frame].deleteFrame()
                        del self.frames[frame]
                    except:
                        print('FrameDestroyError :(')


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
                self.frames[sensor.name].deleteFrame()
                del self.frames[sensor.name]
                sensor.stop()
                self.sensors.remove(sensor)
        for aansturing in self.aansturingen:
            # Als aansturing niet meer aangesloten staat verwijder aansturing
            if aansturing.port not in [port.device for port in available_ports]:
                self.aansturingen.remove(aansturing)
                
    def init_device(self, comport):
        sleep(1)
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
            sensor = Sensor(ser, device_type, self.sensors)
            if (self.loggedin):
                self.frames[sensor.name] = Graph(sensor, self.nb)
            self.sensors.append(sensor)

if __name__ == '__main__':
    app = Application()