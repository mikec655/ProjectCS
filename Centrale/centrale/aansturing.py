from serial import Serial, SerialException
import threading
from time import sleep

class Aansturing():
    def __init__(self, my_serial):
        self.serial = my_serial
        self.port = my_serial.port
        self.name = "AansturingX"

    def uitrollen(self):
        sleep(1)
        self.serial.write(b"_DWN\n")

    def inrollen(self):
        sleep(1)
        self.serial.write(b"_UP\n")
   
    def disconnect(self):
        self.serial.close()
