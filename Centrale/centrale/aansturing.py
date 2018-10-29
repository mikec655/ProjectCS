from serial import Serial, SerialException
import threading
from time import sleep

class Aansturing():
    def __init__(self, comport):
        self.serial = Serial(comport, 19200)
        sleep(2)
        self.serial.write(b"_INIT\n")
        self.type = self.serial.readline()
        self.serial.write(b"_CONN\n")
        self.port = comport
        self.name = "AansturingX"


    def uitrollen(self):
        sleep(1)
        self.serial.write(b"_DWN\n")

    def inrollen(self):
        sleep(1)
        self.serial.write(b"_UP\n")
   
    def disconnect(self):
        self.serial.close()
