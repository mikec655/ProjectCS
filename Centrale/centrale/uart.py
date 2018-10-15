import serial
i = 0
ser = serial.Serial("COM3", 19200)
print(ser)
while True:
    s = ser.read()
    value = int.from_bytes(s, byteorder='little', signed=False)
   
    if value > 0:
        # test for temperture sensor
        v_out = value * (5.0 / 256)
        celsius = round((v_out - 0.5) * 100)
        
        with open ("data.txt", "r+") as f:
            data = f.read()
            f.write(data)
            f.write(str(i) + "," + str(celsius) + '\n')
        i += 1