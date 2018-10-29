from tkinter import Tk, Label, Entry, Button, Checkbutton
from tkinter import ttk
from serial import Serial, SerialException
from serial.tools import list_ports
from sensors import Sensor
from aansturing import Aansturing
from time import sleep
import threading


class Application(Tk):

    def __init__(self):
        # initialise a window.
        super().__init__()
        self.sensors = []
        self.aansturingen = []
        self.threads = []
        self.config(background='white')
        self.geometry("1000x700")
        self.title("Application")
        nb = ttk.Notebook(self)
        properties = ttk.Frame(nb)
        
        rolluiklabel = Label(properties, text="Rolluik:")
        rolluiklabel.config(font=("Times new roman", 18))
        
        maxuitrollabel = Label(properties, text="Maximale uitrol:")
        maxuitrolbox = Entry(properties)

        minuitrollabel = Label(properties, text="Maximale Inrol:")
        minuitrolbox = Entry(properties)

        grenswaardelabel = Label(properties, text="Grenswaarde")
        grenswaardebox1 = Entry(properties)
        grenswaardebox2 = Entry(properties)
        grenswaardebox3 = Entry(properties)
        grenswaardebox4 = Entry(properties)
        grenswaardebox5 = Entry(properties)

        aantimerlabel = Label(properties, text="Automatisch aan")
        uittimerlabel = Label(properties, text="Automatisch uit")

        aantimerbox = Entry(properties)
        uittimerbox = Entry(properties)

        aanuitlabel = Label(properties, text="Aan uit")

        sensor1label = Label(properties, text="Licht Sensor")
        sensor2label = Label(properties, text="Temperatuur Sensor")
        sensor3label = Label(properties, text="SensorNaam")
        sensor4label = Label(properties, text="SensorNaam")
        sensor5label = Label(properties, text="SensorNaam")

        luikopenlabel = Label(properties, text="Rol luik open")
        luikdichtlabel = Label(properties, text="Rol luik dicht")

        rolluiklabel.grid(row = 0, column = 0, columnspan = 50, padx = 1, pady = 20, sticky = 'w')

        maxuitrollabel.grid(row=5, column=0 , columnspan = 20, padx = 1, pady = 1, sticky = 'w')
        maxuitrolbox.grid(row = 5, column=30 , columnspan = 20, padx = 1, pady = 1, sticky = 'n')

        minuitrollabel.grid(row=25, column=0 , columnspan = 20, padx = 1, pady = 1, sticky = 'w')
        minuitrolbox.grid(row = 25, column=30 , columnspan = 20, padx = 1, pady = 1, sticky = 'n')

        sensor1label.grid(row = 55, column = 0, columnspan = 40, padx = 1, pady = 1, sticky = 'w')
        sensor2label.grid(row = 56, column = 0, columnspan = 40, padx = 1, pady = 1, sticky = 'w')
        sensor3label.grid(row = 57, column = 0, columnspan = 40, padx = 1, pady = 1, sticky = 'w')
        sensor4label.grid(row = 58, column = 0, columnspan = 40, padx = 1, pady = 1, sticky = 'w')
        sensor5label.grid(row = 59, column = 0, columnspan = 40, padx = 1, pady = 1, sticky = 'w')

        aantimerlabel.grid(row = 60, column = 0, columnspan = 40, padx = 1, pady = 1, sticky = 'w')
        uittimerlabel.grid(row = 61, column = 0, columnspan = 40, padx = 1, pady = 1, sticky = 'w')

        luikopenlabel.grid(row = 62, column = 0, columnspan = 40, padx = 1, pady = 1, sticky = 'w')
        luikdichtlabel.grid(row = 63, column = 0, columnspan = 40, padx = 1, pady = 1, sticky = 'w')

        grenswaardelabel.grid(row = 50, column = 45, columnspan = 40, padx = 1, pady = 1, sticky = 'w')
        grenswaardebox1.grid(row = 55, column=45 , columnspan = 20, padx = 1, pady = 1, sticky = 'n')
        grenswaardebox2.grid(row = 56, column=45 , columnspan = 20, padx = 1, pady = 1, sticky = 'n')
        grenswaardebox3.grid(row = 57, column=45 , columnspan = 20, padx = 1, pady = 1, sticky = 'n')
        grenswaardebox4.grid(row = 58, column=45 , columnspan = 20, padx = 1, pady = 1, sticky = 'n')
        grenswaardebox5.grid(row = 59, column=45 , columnspan = 20, padx = 1, pady = 1, sticky = 'n')

        aantimerbox.grid(row = 60, column=45 , columnspan = 20, padx = 1, pady = 1, sticky = 'n')
        uittimerbox.grid(row = 61, column=45 , columnspan = 20, padx = 1, pady = 1, sticky = 'n')

        aanuitlabel.grid(row = 50, column = 260, columnspan = 40, padx = 1, pady = 1, sticky = 'w')
        s1box = Checkbutton(properties)
        s1box.grid(row = 55, column=280 , columnspan = 40, padx = 1, pady = 1, sticky = 'n')
        s2box = Checkbutton(properties)
        s2box.grid(row = 56, column=280 , columnspan = 40, padx = 1, pady = 1, sticky = 'n')
        s3box = Checkbutton(properties)
        s3box.grid(row = 57, column=280 , columnspan = 40, padx = 1, pady = 1, sticky = 'n')
        s4box = Checkbutton(properties)
        s4box.grid(row = 58, column=280 , columnspan = 40, padx = 1, pady = 1, sticky = 'n')
        s5box = Checkbutton(properties)
        s5box.grid(row = 59, column=280 , columnspan = 40, padx = 1, pady = 1, sticky = 'n')
        s6box = Checkbutton(properties)
        s6box.grid(row = 60, column=280 , columnspan = 40, padx = 1, pady = 1, sticky = 'n')
        s7box = Checkbutton(properties)
        s7box.grid(row = 61, column=280 , columnspan = 40, padx = 1, pady = 1, sticky = 'n')
        s8box = Checkbutton(properties)
        s8box.grid(row = 62, column=280 , columnspan = 40, padx = 1, pady = 1, sticky = 'n')
        s9box = Checkbutton(properties)
        s9box.grid(row = 63, column=280 , columnspan = 40, padx = 1, pady = 1, sticky = 'n')

        nb.add(properties, text='properties')

        while True:
            self.update()
            print(self.aansturingen)
            self.check_for_devices(nb)
            nb.pack(expand=1, fill="both")

    def check_for_devices(self, nb):
        available_ports = list_ports.comports()
        for port in available_ports:
            # Als sensor niet in de sensors staat voeg toe
            if port.device not in [sensor.port for sensor in self.sensors] and \
            port.device not in [aansturing.port for aansturing in self.aansturingen]:
                device_type = self.init_device(port.device)
                if device_type == "_MTR\n":
                    a = Aansturing(port.device)
                    self.aansturingen.append(a)
                else:
                    s = Sensor(port.device, device_type, self.sensors)
                    self.sensors.append(s)
                    nb.add(s.graph, text=s.name)
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
        ser = Serial(comport, 19200)
        sleep(2)
        ser.write(b"_INIT\n")
        device_type = ser.readline().decode("UTF-8")
        ser.write(b"_CONN\n")
        ser.close()
        return device_type

if __name__ == '__main__':
    app = Application()