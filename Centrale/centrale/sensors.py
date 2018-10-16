from serial import Serial
from serial.tools import list_ports
from datetime import datetime

class SensorReader(Serial):
    def __init__(self, port, log_file_path):
        super().__init__(port, 19200)
        self.log_file_path = log_file_path

    def log(self):
        while True:
            value = self.read()
            value = int.from_bytes(value, byteorder='little', signed=False)
            # WARNING: onderstaande conditie is incorrect
            if value > 0:
                with open (self.log_file_path, "a") as f:
                    f.write(datetime.now().strftime("%H:%M:%S") + "," + str(value) + '\n')

''' 
ports_list = list_ports.comports()
for port in ports_list:
    print("device:", port.device)
    print("name:", port.product)
    print("description:", port.description)
    print("hwid:", port.hwid)
    print("vid:", port.vid)
    print("pid:", port.pid)
    print("serial_number", port.serial_number)
    print("location:", port.location)
    print("manufacturer:", port.manufacturer)
    print("product:", port.product)
    print("interface:", port.interface)
    print("----------------------------------")
'''