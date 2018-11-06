from serial import Serial, SerialException
import settings_editor
import threading
from time import sleep

class Aansturing():
    def __init__(self, my_serial, id):
        self.serial = my_serial
        self.port = my_serial.port
        self.id = id
        self.name = self.get_name()
        self.uitgerold = None 

    def get_name(self):
        name = "Aansturing"
        settings = settings_editor.readSettings()
        try:
            name = settings["aansturingen"][self.id]["name"]
        except KeyError:
            sensor_number = len(settings["aansturingen"].values()) + 1
            name += str(sensor_number)
            settings["aansturingen"][self.id] = {}
            settings["aansturingen"][self.id]["name"] = name
            settings["aansturingen"][self.id]["sensor_value"] = {}
            settings_editor.writeSettings(settings)
        return name

    def uitrollen(self):
        sleep(1)
        self.serial.write(b"_DWN\n")

    def inrollen(self):
        sleep(1)
        self.serial.write(b"_UP\n")
   
    def disconnect(self):
        self.serial.close()
