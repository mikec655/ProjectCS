import sys
from tkinter import Tk, Label, Entry, Button, Checkbutton, TclError, PhotoImage
from tkinter import ttk
from serial import Serial, SerialException
from serial.tools import list_ports
from aansturing import Aansturing
from time import sleep
from sensors import Sensor, SerialException, list_ports
import settings_editor
from loginscherm import Login
from home import Home
from properties import Properties
from logfileframe import LogFileReader
from linegraph import Graph
import time
from datetime import datetime
import threading


class Application(Tk):

    def __init__(self):
        # initialise a window.
        super().__init__()
        self.geometry("1000x700")
        self.title("Application")
        icon = PhotoImage(file='Centrale/centrale/icon.png')
        self.tk.call('wm', 'iconphoto', self._w, icon)

        # control variables
        self.alive = True
        self.loggedin = False
        self.sensors = []
        self.sensorsWithoutGraph = []
        self.framesToDelete = []
        self.aansturingen = []
        self.other_com_ports = []
        self.threads = []
        self.frames = {}
        self.nb = ttk.Notebook(self)

        # Frames die nooit verdwijnen toevoegen
        self.frames['Home'] = Home(self.nb, self.aansturingen)
        self.frames['Login'] = Login(self.nb)

        threading.Thread(target=self.check_for_devices, name="CheckForDeviceThread").start()
        
        self.applicationLoop()

    def stuur_aan(self):
        # print([sensor.current_value for sensor in self.sensors])
        settings = settings_editor.readSettings()
        command = "inrollen"
        for aansturing in self.aansturingen:
            current_date = datetime.now().strftime("%d-%m-%Y")
            up_time = datetime.strptime(current_date + " " + settings['aansturingen'][aansturing.id]['up'], "%d-%m-%Y %H:%M")
            down_time = datetime.strptime(current_date + " " + settings['aansturingen'][aansturing.id]['down'], "%d-%m-%Y %H:%M")
            if datetime.now() < up_time and datetime.now() > down_time:
                for sensor in self.sensors:
                    if sensor.current_value == None:
                        # Als de sensor nog geen waarde heeft doe niks
                        command = ""
                        continue
                    try:
                        value = settings['aansturingen'][aansturing.id]['sensor_value'][sensor.id]
                        if value[0] == ">":
                            if sensor.current_value > float(value[1:]):
                                command = "uitrollen"
                        elif value[0] == "<":
                            if sensor.current_value < float(value[1:]):
                                command = "uitrollen"
                    except KeyError:
                        # Als voor de sensor geen waarde staat opgeslagen, doe niks
                        pass
            if command == "uitrollen" and aansturing.status != "uitgerold":
                aansturing.uitrollen()
            elif command == "inrollen" and aansturing.status != "ingerold":
                aansturing.inrollen()

    def applicationLoop(self):
        while True:
            try:
                self.update()
                self.stuur_aan()
                try:
                    self.frames['Properties'].update(self.aansturingen, self.sensors)
                except KeyError:
                    pass
                self.frames['Home'].update(self.aansturingen)
                for sensor in self.sensorsWithoutGraph:
                    self.frames[sensor.name] = Graph(sensor, self.nb)
                    self.sensorsWithoutGraph.remove(sensor)
                for frame in self.framesToDelete:
                    if self.loggedin:
                        self.frames[frame].deleteFrame()
                        del self.frames[frame]
                    self.framesToDelete.remove(frame)
                self.check_logged_in()
                self.nb.pack(expand=1, fill="both")
            except TclError:
                try:
                    sys.exit(1)
                except SystemExit: 
                    self.alive = False
                    for sensor in self.sensors:
                        sensor.stop()
                    for frame in self.frames.keys():
                        if "sensor" in frame:
                            self.frames[frame].stop() 
                    print("programma afgesloten")
                break

    def check_logged_in(self):
        if self.frames['Login'].loggedin == 'I':
            self.loggedin = True
            self.frames['Login'].loggedin = ''
            self.frames['Properties'] = Properties(self.sensors, self.aansturingen, self.nb)
            self.frames['LogFileReader'] = LogFileReader(self.nb)
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
        while self.alive:
            available_ports = list_ports.comports()
            for port in available_ports:
                # Als sensor niet in de sensors staat voeg toe
                if port.device not in [sensor.port for sensor in self.sensors] and \
                port.device not in [aansturing.port for aansturing in self.aansturingen] and \
                port.device not in self.other_com_ports:
                    threadName = port.device + "-Thread"
                    if threadName not in [thread.name for thread in threading.enumerate()]:
                        threading.Thread(name=threadName, target=self.init_device, args=(port.device, port.serial_number)).start()
            for sensor in self.sensors:
                # Als sensor niet meer aangesloten staat verwijder van sensor
                if sensor.port not in [port.device for port in available_ports]:
                    try:
                        self.frames[sensor.name].deleteFrame()
                        del self.frames[sensor.name]
                    except KeyError:
                        pass
                    sensor.stop()
                    self.sensors.remove(sensor)
            for aansturing in self.aansturingen:
                # Als aansturing niet meer aangesloten staat verwijder aansturing
                if aansturing.port not in [port.device for port in available_ports]:
                    self.aansturingen.remove(aansturing)
            for other_port in self.other_com_ports:
                if other_port not in [port.device for port in available_ports]:
                    self.other_com_ports.remove(other_port)
      
    def init_device(self, comport, id):
        sleep(1)
        try:
            ser = Serial(comport, 19200, timeout=5)
            sleep(2)
            while True:
                ser.write(b"_INIT\n")
                device_type = ser.readline().decode("UTF-8").strip('\n')
                if device_type != "_ERR":
                    break
            if device_type == "_MTR":
                while True:
                    ser.write(b"_CONN\n")
                    device_type = ser.readline().decode("UTF-8").strip('\n')
                    if device_type != "_ERR":
                        break
                a = Aansturing(ser, id)
                self.aansturingen.append(a)
            elif device_type == "_TEMP" or device_type == "_LGHT":
                sensor = Sensor(ser, device_type, id, self.sensors)
                if (self.loggedin):
                    self.sensorsWithoutGraph.append(sensor)
                self.sensors.append(sensor)
                ser.write(b"_CONN\n")
            else:
                self.other_com_ports.append(comport)
        except SerialException as E:
            print (E)
            self.other_com_ports.append(comport)

if __name__ == '__main__':
    app = Application()