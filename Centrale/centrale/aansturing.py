from serial import Serial, SerialException
import settings_editor
import threading
from time import sleep
from datetime import datetime, timedelta

class Aansturing():
    def __init__(self, my_serial, id):
        self.serial = my_serial
        self.serial.timeout = None
        self.port = my_serial.port
        self.id = id
        self.name = self.get_name()
        self.status = ""
        self.thread = threading.Thread(name=self.name + "CommandThread")

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
            settings["aansturingen"][self.id]["up"] = ""
            settings["aansturingen"][self.id]["down"] = ""
            settings["aansturingen"][self.id]["timeout"] = ""
            settings["aansturingen"][self.id]["sensor_value"] = {}
            settings_editor.writeSettings(settings)
        return name

    def send_command(self, commands):
        sleep(0.5)
        if len(commands) == 0:
            return
        command = commands[0]
        self.serial.write(command.encode("UTF-8") + b"\n")
        response = self.serial.readline().decode("UTF-8").strip('\n')
        if response == command:
            commands.remove(command)
            self.send_command(commands)
        else:
            self.send_command(commands)

    def uitrollen(self, timeout=""):
        if not self.thread.isAlive():
            self.thread = threading.Thread(name=self.name + "CommandThread", target=self.send_command, args=(["_STOP", "_DWN"],))
            self.thread.start()
            self.setTimeout(timeout)
            self.status = "uitgerold"

    def inrollen(self, timeout=""):
        if not self.thread.isAlive():
            self.thread = threading.Thread(name=self.name + "CommandThread", target=self.send_command, args=(["_STOP", "_UP"],))
            self.thread.start()
            self.setTimeout(timeout)
            self.status = "ingerold"

    def stop(self):
        if not self.thread.isAlive():
            self.thread = threading.Thread(name=self.name + "CommandThread", target=self.send_command, args=(["_STOP"],))
            self.thread.start()
            self.status = "onderbroken"

    def setTimeout(self, timeout=""):
        settings = settings_editor.readSettings()
        if timeout == "auto":
            settings["aansturingen"][self.id]["timeout"] = ""
        elif timeout == "einde dag":
            time = settings["aansturingen"][self.id]["down"]
            settings["aansturingen"][self.id]["timeout"] = time
        elif timeout != "":
            hours = int(timeout[5])
            time = datetime.now() + timedelta(hours=hours)
            settings["aansturingen"][self.id]["timeout"] = datetime.strftime(time, "%H:%M")
        settings_editor.writeSettings(settings)
   
    def disconnect(self):
        self.serial.close()

