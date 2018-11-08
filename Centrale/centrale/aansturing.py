from serial import Serial, SerialException
import settings_editor
import threading
from time import sleep

class Aansturing():
    def __init__(self, my_serial, id):
        self.serial = my_serial
        self.serial.timeout = None
        self.serial.reset_input_buffer()
        self.port = my_serial.port
        self.id = id
        self.name = self.get_name()
        self.thread = threading.Thread()

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

    def send_command(self, commands):
        sleep(1)
        if len(commands) == 0:
            return
        command = commands[0]
        print(command)
        self.serial.write(command.encode("UTF-8") + b"\n")
        response = self.serial.readline().decode("UTF-8").strip('\n')
        print(response)
        if response == command:
            commands.remove(command)
            self.send_command(commands)
        else:
            self.send_command(commands)


    def uitrollen(self):
        if not self.thread.isAlive():
            threading.Thread(target=self.send_command, args=(["_STOP", "_DWN"],)).start()


    def inrollen(self):
        if not self.thread.isAlive():
            threading.Thread(target=self.send_command, args=(["_STOP", "_UP"],)).start()

    def stop(self):
        if not self.thread.isAlive():
            threading.Thread(target=self.send_command, args=(["_STOP"],)).start()
   
    def disconnect(self):
        self.serial.close()
