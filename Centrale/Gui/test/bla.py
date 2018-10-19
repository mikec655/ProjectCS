from serial import Serial, SerialException
from serial.tools import list_ports
from datetime import datetime

# only for code on the end of the page
from collections import Counter
from time import sleep

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

while True:
    available_ports = list_ports.comports()
    sensor_counter = Counter()
    for port in available_ports:
        try:
            ser = Serial(port.device, 19200)
            response = ser.read_until()
            response = response.decode("utf-8")
            sensor_type, value = response.split(":")
            value = int(value)
            sensor_counter.update([sensor_type])
            if sensor_type == "_TEMP":
                number = sensor_counter['_TEMP']
                print("Temperatuursensor " + str(number) + ": " + str(value) + " graden Celsius")
            elif sensor_type == "_LGHT":
                number = sensor_counter['_LGHT']
                print("Lichtsensor " + str(number) + ": " + str(value) + " lux")
            else:
                pass
            ser.close()
        except SerialException:
            pass
        except ValueError:
            pass
        if port == available_ports[-1]:
            break
    else:
        print("Geen sensoren gevonden!")
        sleep(2)