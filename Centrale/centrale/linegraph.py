#guiplotdinges
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
        super().__init__(master, sensor.name)
        self.sensor = sensor
        self.log_file_path = self.sensor.log_file_path      #zet de variabele voor het pad van de logfile

        self.fig = plt.figure()                 #maakt een figuur aan
        self.ax = self.fig.add_subplot(1,1,1)   #geeft dimensies mee aan het figuur
       
        self.graph = FigureCanvasTkAgg(self.fig, master=self)   #maakt een canvas aan voor de grafiek
        self.graph.get_tk_widget().pack(side="top",fill='both',expand=1)    #packed de grafiek

        self.alive = True       #zodra het programma niet meer nodig is , stopt de thread met draaien
        threading.Thread(target=self.redraw_animation, args=(1,), name=sensor.name + "GraphThread").start()  

    def redraw(self, i):
        self.ax.clear()
        self.ax.set_title(self.sensor.name) #geeft de titel mee voor de grafiek
        self.ax.set_xlabel('Tijd')  #geeft de x-as label mee
        if self.sensor.type == "_TEMP":
            self.ax.set_ylabel('Temperatuur (°C)')  #geeft de y-as label mee
        elif self.sensor.type == "_LGHT":
            self.ax.set_ylabel('Lichtintensiteit (lux)')
        # self.ax.tick_params(axis='x', labelrotation=45)
        graph_data = open(self.log_file_path,"r").read()    #haalt de data uit het log bestand
        lines = graph_data.split('\n')  #split de data uit het log bestand per lijn
        xs = []
        ys = []
        xx = 0
        for line in lines:  #voor iedere lijn in het bestand
            if len(line) > 1 and line[0] != '#':    #zolang de lengte groter is dan 1
                x, y = line.split(',')  #split de waardes op de komma
                xs.append(datetime.strptime(x, "%H:%M:%S")) #geeft de huidige tijd weer op de x-as 
                ys.append(float(y)) #voegt de y as toe
                xx += 1
        # xs = xs[-10:]
        # ys = ys[-10:]
        self.ax.plot(xs, ys)        
    
    def redraw_animation(self, i):
        ani = animation.FuncAnimation(self.fig, self.redraw, interval=5000) #zorgt voor een interval
        while self.alive:
            sleep(4)    #zorgt voor een interval

    def stop(self):
        self.alive = False  #zodra het programma niet meer nodig is , stopt de thread met draaien

    def deleteFrame(self):
        super().deleteFrame()
        self.stop()
        
        