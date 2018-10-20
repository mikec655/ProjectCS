#guiplotdinges
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

from tkinter.ttk import Frame

from datetime import datetime

# sensor_reader1 = SensorReader("COM5", "Centrale/centrale/data.txt")
# _thread.start_new_thread(sensor_reader1.log, ())

class Graph(Frame):
    def __init__(self, log_file_path, master=None):
        super().__init__(master)
        self.log_file_path = log_file_path

        self.fig = plt.figure()
        self.ax1 = self.fig.add_subplot(1,1,1)

        self.graph = FigureCanvasTkAgg(self.fig, master=self)
        self.graph.get_tk_widget().pack(side="top",fill='both',expand=1)

    def redraw(self, i):
        graph_data = open(self.log_file_path,"r").read()
        lines = graph_data.split('\n')
        xs = []
        ys = []
        for line in lines:
            if len(line) > 1 and line[0] != '#':
                x, y = line.split(',')
                # xs.append(datetime.strptime(x, "%H:%M:%S"))
                xs.append(x)
                #xs.append(float(x))
                ys.append(float(y))
            self.ax1.clear()
            self.ax1.plot(xs, ys)