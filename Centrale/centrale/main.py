import sys
from tkinter import Tk, Label, Entry, Button, Checkbutton, TclError, PhotoImage
from tkinter import ttk
from serial import Serial, SerialException
from serial.tools import list_ports
from aansturing import MotorControl
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


class Centrale(Tk):

    def __init__(self):
        # initialise a window.
        super().__init__()
        self.geometry("1000x700")
        self.title("Centrale")
        icon = PhotoImage(file='Centrale/centrale/icon.png')
        self.tk.call('wm', 'iconphoto', self._w, icon)

        # control variables
        self.alive = True
        self.loggedin = False
        self.sensors = []
        self.motorControls = []
        self.sensorsWithoutGraph = []
        self.framesToDelete = []
        self.other_com_ports = []
        self.frames = {}
        self.nb = ttk.Notebook(self)

        # Frames die nooit verdwijnen toevoegen
        self.frames['Home'] = Home(self.nb, self.motorControls)
        self.frames['Login'] = Login(self.nb)

        threading.Thread(target=self.checkForDevices, name="CheckForDeviceThread").start()
        
        self.applicationLoop()

    def controlMotors(self):
        settings = settings_editor.readSettings()
        command = "inrollen"
        for control in self.motorControls:
            current_date = datetime.now().strftime("%d-%m-%Y")
            # time wanneer ingerold moet worden
            time = ""
            if settings['aansturingen'][control.id]['up'] != "":
                time = settings['aansturingen'][control.id]['up']
            else:
                time = "23:59"
            up_time = datetime.strptime(current_date + " " + time, "%d-%m-%Y %H:%M")
            # time wanneer uitgerold moet worden
            time = ""
            if settings['aansturingen'][control.id]['down'] != "":
                time = settings['aansturingen'][control.id]['down']
            else:
                time = "00:00"
            down_time = datetime.strptime(current_date + " " + time, "%d-%m-%Y %H:%M")
            # timeout time
            time = ""
            if settings['aansturingen'][control.id]['timeout'] != "":
                time = settings['aansturingen'][control.id]['timeout']
            else:
                time = "00:00"
            timeout_time = datetime.strptime(current_date + " " + time, "%d-%m-%Y %H:%M")


            if datetime.now() <= up_time and datetime.now() >= down_time: 
                # als aansturing niet getimeout is bekijk de sensoren
                if datetime.now() >= timeout_time:
                    settings['aansturingen'][control.id]['timeout'] = ""
                    for sensor in self.sensors:
                        if sensor.current_value == None:
                            # Als de sensor nog geen waarde heeft doe niks
                            command = ""
                            continue
                        try:
                            value = settings['aansturingen'][control.id]['sensor_value'][sensor.id]
                            # Als waarde over een komt met een waarde uit setting.json
                            # set command op "uitrollen"
                            if value[0] == ">":
                                if sensor.current_value > float(value[1:]):
                                    command = "uitrollen"
                            elif value[0] == "<":
                                if sensor.current_value < float(value[1:]):
                                    command = "uitrollen"
                        except KeyError:
                            # Als voor de sensor geen waarde staat opgeslagen, doe niks
                            pass
                else:
                    command = ""
            # controleer status en voor zo nodig command uit
            if command == "uitrollen" and control.status != "uitgerold":
                control.rollOut()
            elif command == "inrollen" and control.status != "ingerold":
                control.rollIn()

    def applicationLoop(self):
        # loop waarin de GUI wordt geupdate
        while True:
            try:
                # Tkinter update functie op GUI bij te werken
                self.update()
                self.controlMotors()
                try:
                    self.frames['Properties'].update(self.motorControls, self.sensors)
                except KeyError:
                    pass
                self.frames['Home'].update(self.motorControls)
                # toevoegen van nieuw Graph frames
                for sensor in self.sensorsWithoutGraph:
                    self.frames[sensor.name] = Graph(sensor, self.nb)
                    self.sensorsWithoutGraph.remove(sensor)
                # verwijderen van onnodige Graph frames
                for frame in self.framesToDelete:
                    if self.loggedin:
                        self.frames[frame].deleteFrame()
                        del self.frames[frame]
                    self.framesToDelete.remove(frame)
                self.checkLoggedIn()
                self.nb.pack(expand=1, fill="both")
            except TclError:
                # Error is raised when application is closed
                # Application is closed safely
                try:
                    sys.exit(1)
                except SystemExit: 
                    self.alive = False
                    # Veilig afsluiten van sensoren en aansturingen
                    for sensor in self.sensors:
                        sensor.disconnect()
                    for control in self.motorControls:
                        control.disconnect()
                    for frame in self.frames.keys():
                        if "sensor" in frame:
                            self.frames[frame].stop() 
                    print("END")
                break

    def checkLoggedIn(self):
        # Controleert of er ingelogd is en neemt zo nodig actie
        if self.frames['Login'].loggedin == 'I':
            # Als er ingelogd is, maak Properties en LogFileReader Frame aan
            self.loggedin = True
            self.frames['Login'].loggedin = ''
            self.frames['Properties'] = Properties(self.sensors, self.motorControls, self.nb)
            self.frames['LogFileReader'] = LogFileReader(self.nb)
            # Een voor iedere sensor een nieuwe graph
            for sensor in self.sensors:
                self.frames[sensor.name] = Graph(sensor, self.nb)
        elif self.frames['Login'].loggedin == 'U':
            # Als er uitgelogd is verwijder alle frames
            self.loggedin = False
            self.frames['Login'].loggedin = ''
            for frame in self.frames.copy().keys():
                if frame not in ['Home', 'Login']:
                    try:
                        self.frames[frame].deleteFrame()
                        del self.frames[frame]
                    except:
                        print('FrameDestroyError :(')

    def checkForDevices(self):
        # Controleert of er nieuwe device zijn toegevoed of bestaande devices zijn verwijderd
        while self.alive:
            available_ports = list_ports.comports()
            for port in available_ports:
                # Als device niet in een list staat, voeg device toe
                if port.device not in [sensor.port for sensor in self.sensors] and \
                port.device not in [control.port for control in self.motorControls] and \
                port.device not in self.other_com_ports:
                    threadName = port.device + "-Thread"
                    if threadName not in [thread.name for thread in threading.enumerate()]:
                        threading.Thread(name=threadName, target=self.initDevice, args=(port.device, port.serial_number)).start()
            for sensor in self.sensors:
                # Als sensor niet meer aangesloten staat verwijder van sensor
                if sensor.port not in [port.device for port in available_ports]:
                    try:
                        self.frames[sensor.name].deleteFrame()
                        del self.frames[sensor.name]
                    except KeyError:
                        pass
                    sensor.disconnect()
                    self.sensors.remove(sensor)
            for control in self.motorControls:
                # Als aansturing niet meer aangesloten staat verwijder aansturing
                if control.port not in [port.device for port in available_ports]:
                    self.motorControls.remove(control)
            for other_port in self.other_com_ports:
                # Als een onbekende COM-poort niet meer aangesloten is, verwijder uit list
                if other_port not in [port.device for port in available_ports]:
                    self.other_com_ports.remove(other_port)
      
    def initDevice(self, comport, id):
        # Toevoegen van een nieuw device
        sleep(1)
        try:
            ser = Serial(comport, 19200, timeout=2)
            sleep(2)
            # Zolang er fout optreed stuur command "_INIT"
            while True:
                ser.write(b"_INIT\n")
                device_type = ser.readline().decode("UTF-8").strip('\n')
                if device_type != "_ERR":
                    break
            if device_type == "_MTR":
                # Device is een aansturing
                # Stuur command "_CONN" zolang er fout optreed
                while True:
                    ser.write(b"_CONN\n")
                    device_type = ser.readline().decode("UTF-8").strip('\n')
                    if device_type != "_ERR":
                        break
                # Maak nieuw aansturing (MotorControl) aan
                a = MotorControl(ser, id)
                self.motorControls.append(a)
            elif device_type == "_TEMP" or device_type == "_LGHT":
                # Maak nieuwe sensor aan
                sensor = Sensor(ser, device_type, id, self.sensors)
                if (self.loggedin):
                    self.sensorsWithoutGraph.append(sensor)
                self.sensors.append(sensor)
                ser.write(b"_CONN\n")
            else:
                # Als device type onbekend is,
                # voeg toe aan onbekende COM-porten
                self.other_com_ports.append(comport)
        except SerialException as E:
            print(E)
            # Als er een fout optreed,
            # voeg toe aan onbekende COM-porten 
            self.other_com_ports.append(comport)

if __name__ == '__main__':
    centrale = Centrale()