import serial

ser = serial.Serial("COM3", 19200)
print(ser)
while True:
    s = ser.read()
    value = int.from_bytes(s, byteorder='little', signed=False)
   
    '''
    # test for temperture sensor
    v_out = value * (5.0 / 256)
    celsius = (v_out - 0.5) * 100
    print(celsius)
    '''
    print(value)