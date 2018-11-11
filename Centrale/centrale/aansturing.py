from serial import Serial, SerialException
import settings_editor
import threading
from time import sleep
from datetime import datetime, timedelta

class MotorControl():
    def __init__(self, my_serial, id):
        self.serial = my_serial
        self.serial.timeout = None
        self.port = my_serial.port
        self.id = id
        self.status = ""
        self.giveName()
        self.thread = threading.Thread(name=self.name + "CommandThread")

    def giveName(self):
        # Geeft een naam aan de aansturing op basis van wat in settings.json staat opgeslagen
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
        self.name = name

    def sendCommand(self, commands):
        # stuur een lijst met commands naar de aansturing
        # een command moet eerst verwerkt zijn voordat de volgende wordt gestuurd
        sleep(0.5)
        if len(commands) == 0:
            return
        command = commands[0]
        self.serial.write(command.encode("UTF-8") + b"\n")
        response = self.serial.readline().decode("UTF-8").strip('\n')
        if response == command:
            commands.remove(command)
            self.sendCommand(commands)
        else:
            self.sendCommand(commands)

    def rollOut(self, timeout=""):
        # Uitrollen van het scherm
        if not self.thread.isAlive():
            self.thread = threading.Thread(name=self.name + "CommandThread", target=self.sendCommand, args=(["_STOP", "_DWN"],))
            self.thread.start()
            self.setTimeout(timeout)
            self.status = "uitgerold"

    def rollIn(self, timeout=""):
        # Inrollen van het scherm
        if not self.thread.isAlive():
            self.thread = threading.Thread(name=self.name + "CommandThread", target=self.sendCommand, args=(["_STOP", "_UP"],))
            self.thread.start()
            self.setTimeout(timeout)
            self.status = "ingerold"

    def stopRolling(self):
        # Onderbrekken van het in/uitrollen
        if not self.thread.isAlive():
            self.thread = threading.Thread(name=self.name + "CommandThread", target=self.sendCommand, args=(["_STOP"],))
            self.thread.start()
            self.status = "onderbroken"

    def setTimeout(self, timeout=""):
        # Slaat een tijd op tot wanneer de aansturing getimed out is  
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
        # Zorgt er voor dat serial veilig worden afgesloten
        self.serial.close()

