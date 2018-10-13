import serial

ser = serial.Serial("COM3", 19200)
print(ser)
while True:
    s = ser.read()
    print(s.hex())