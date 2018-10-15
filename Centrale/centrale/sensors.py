from serial import Serial
from datetime import datetime

class SensorReader(Serial):
    def __init__(self, port, log_file_path):
        super().__init__(port, 19200)
        self.log_file_path = log_file_path

    def log(self):
        while True:
            value = self.read()
            value = int.from_bytes(value, byteorder='little', signed=False)
            if value > 0:
                v_out = value * (5.0 / 256)
                celsius = round((v_out - 0.5) * 100)
                
                with open (self.log_file_path, "a") as f:
                    f.write(datetime.now().strftime("%H:%M:%S") + "," + str(celsius) + '\n')
