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
            f.write(str(i) + "," + str(celsius) + '\n')
        i += 1

#guiplotdinges

import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate (i) :
    graph_data = open("data.txt","r").read()
    lines = graph_data.split('\n')
    xs = []
    ys = []
    for line in lines:
        if len(line) > 1:
            x, y = line.split(',')
            xs.append(float(x))
            ys.append(float(y))
        ax1.clear()
        ax1.plot(xs, ys)

ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()
