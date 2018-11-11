import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

from myframe import MyFrame
from datetime import datetime
from time import sleep
import threading

class Graph(MyFrame):
    def __init__(self, sensor, master=None):
        #hier wordt het canvas voor de grafiek aangemaakt
        super().__init__(master, sensor.name)
        self.sensor = sensor

        # Aanmaken figure voor een grafiek
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(1,1,1)
        self.graph = FigureCanvasTkAgg(self.fig, master=self)
        self.graph.get_tk_widget().pack(side="top",fill='both',expand=1)

        self.alive = True # Thread control variabele
        threading.Thread(target=self.redrawAnimation, args=(1,), name=sensor.name + "GraphThread").start()  

    def redraw(self, i):
        # updaten van de grafiek
        self.ax.clear()
        self.ax.set_title(self.sensor.name) 
        self.ax.set_xlabel('Tijd')
        # bepalen van de label op de y-as
        if self.sensor.type == "_TEMP":
            self.ax.set_ylabel('Temperatuur (°C)') 
        elif self.sensor.type == "_LGHT":
            self.ax.set_ylabel('Lichtintensiteit (lux)')
        graph_data = open(self.sensor.logFilePath,"r").read()
        lines = graph_data.split('\n')
        xs = []
        ys = []
        for line in lines:
            # als de lijn <<break>> bevat wordt de grafiek tijdelijk onderbroken
            if line == "<<break>>":
                self.ax.plot(xs, ys, color='blue') 
                xs = []
                ys = []
            # lezen van de lijnen met data 
            elif len(line) > 1 and line[0] != '#':
                x, y = line.split(',') 
                xs.append(datetime.strptime(x, "%H:%M:%S"))
                ys.append(float(y))
        self.ax.plot(xs, ys, color='blue')        
    
    def redrawAnimation(self, i):
        # animatie voor de graph op een eigen thread
        ani = animation.FuncAnimation(self.fig, self.redraw, interval=5000)
        while self.alive:
            sleep(4)

    def stop(self):
        # zodra het graph niet meer nodig is, 
        # moet de thread stoppen met draaien
        self.alive = False  

    def deleteFrame(self):
        # hier wordt het frame verwijdert en de thread gestopt
        super().deleteFrame()
        self.stop()
        