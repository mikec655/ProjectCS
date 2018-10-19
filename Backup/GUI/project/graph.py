#guiplotdinges

import matplotlib.pyplot as plt
import matplotlib.animation as animation

from sensors import SensorReader

import _thread
from datetime import datetime

# sensor_reader1 = SensorReader("COM3", "Centrale/centrale/data.txt")
# _thread.start_new_thread(sensor_reader1.log)
class test:

    fig = plt.figure()
    ax1 = fig.add_subplot(1,1,1)

    def animate (self,i) :
        graph_data = open("C:/Users/bernt/OneDrive/Jaar2/Project/GUI/data.txt","r").read()
        lines = graph_data.split('\n')
        xs = []
        ys = []
        for line in lines:
            if len(line) > 1:
                x, y = line.split(',')
                xs.append(datetime.strptime(x, "%H:%M:%S"))
                #xs.append(float(x))
                ys.append(float(y))
            self.ax1.clear()
            self.ax1.plot(xs, ys)
    ani = animation.FuncAnimation(fig, animate, interval=5000)
    plt.show()

test = test()
test.animate(1)

