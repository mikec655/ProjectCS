#guiplotdinges
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

from tkinter.ttk import Frame
from datetime import datetime
from time import sleep
import threading

class Graph(Frame):
    def __init__(self, log_file_path, master=None):
        super().__init__(master)
        self.log_file_path = log_file_path

        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(1,1,1)
       
        self.graph = FigureCanvasTkAgg(self.fig, master=self)
        self.graph.get_tk_widget().pack(side="top",fill='both',expand=1)

        self.alive = True
        threading.Thread(target=self.redraw_animation, args=(1,), daemon=True).start()

    def redraw(self, i):
        self.ax.clear()
        self.ax.set_title('SENSOR')
        self.ax.set_xlabel('Tijd')
        self.ax.set_ylabel('Temperatuur (°C)')
        # self.ax.tick_params(axis='x', labelrotation=45)
        graph_data = open(self.log_file_path,"r").read()
        lines = graph_data.split('\n')
        xs = []
        ys = []
        xx = 0
        for line in lines:
            if len(line) > 1 and line[0] != '#':
                x, y = line.split(',')
                xs.append(datetime.strptime(x, "%H:%M:%S"))
                ys.append(float(y))
                xx += 1
        # xs = xs[-10:]
        # ys = ys[-10:]
        self.ax.plot(xs, ys)
    
    def redraw_animation(self, i):
        ani = animation.FuncAnimation(self.fig, self.redraw, interval=5000)
        while self.alive:
            sleep(4)

    def stop(self):
        self.alive = False
        
        