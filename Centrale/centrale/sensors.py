from serial import Serial, SerialException
from serial.tools import list_ports
from datetime import datetime
from linegraph import Graph
import threading

class Sensor():
    def __init__(self, comport, device_type, existing_sensors):
        self.serial = Serial(comport, 19200)
        self.port = comport
        self.sensor_type = device_type.split(":")[0]
        self.name = self.get_name(existing_sensors)
        # self.log_file_path = "Centrale/logs/" + self.name + "_" + datetime.now().strftime("%d-%m-%Y") + ".txt"
        self.log_file_path = "../logs/" + self.name + "_" + datetime.now().strftime("%d-%m-%Y") + ".txt"
        self.graph = Graph(self.log_file_path)
        log_file = open(self.log_file_path, "w+")
        log_file.write("# WARNING: DO NOT EDIT THIS FILE!\n")
        log_file.write("# File created: " + datetime.now().strftime("%d-%m-%Y %H:%M:%S") + "\n")
        log_file.write("# Log file for " + self.name + "\n")
        log_file.write("# Time,Value\n")
        log_file.close()
        self.alive = True
        self.thread = threading.Thread(target=self.log, name=self.name + "Thread")
        self.thread.start()

    def get_name(self, existing_sensors):
        sensor_name = ""
        naming_dict = {
            "_TEMP": "Temperatuursensor", 
            "_LGHT": "Lichtsensor"
            }
        while True:
            if self.sensor_type in naming_dict.keys():
                sensor_number = len([sensor for sensor in existing_sensors if sensor.sensor_type == self.sensor_type]) + 1
                sensor_name += naming_dict[self.sensor_type] + str(sensor_number)
                break
        return sensor_name
            
    def log(self):
        while self.alive:
            try: 
                response = self.serial.readline()
                response = response.decode("utf-8")
                sensor_type, value = response.split(":")
                value = int(value)
                if sensor_type == self.sensor_type:
                    with open (self.log_file_path, "a") as f:
                        f.write(datetime.now().strftime("%H:%M:%S") + "," + str(value) + '\n')
            except ValueError:
                pass
            except AttributeError:
                pass
            except SerialException:
                pass

        
    def stop(self):
        self.serial.close()
        self.graph.stop()
        self.alive = False
        
        