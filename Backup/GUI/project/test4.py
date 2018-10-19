
from random import randint
from tkinter import ttk
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import matplotlib.pyplot as plt
import matplotlib.animation as animation
 
# these two imports are important
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import time
import threading

class Project:

     
    
    def __init__(self,i, sensor):
        self.sensor = sensor
        self.fig = Figure()
        
        ax = self.fig.add_subplot(111)
        ax.set_xlabel("X axis")
        ax.set_ylabel("Y axis")
        ax.grid()
     
        graph = FigureCanvasTkAgg(self.fig, master=self.sensor)
        graph.get_tk_widget().pack(side="top",fill='both',expand=1)

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
#####################################################################
        # graph = FigureCanvasTkAgg(fig, master=self.sensor)
        # graph.get_tk_widget().pack(side="top",fill='both',expand=1)
        # graph = FigureCanvasTkAgg(fig, master=self.sensor)
    
    # ani = animation.FuncAnimation(fig, grafiek, interval=5000)
            # graph.get_tk_widget().pack(side="top",fill='both',expand=1)
  ############################################################################################
        # graph_data = open("C:/Users/bernt/OneDrive/Jaar2/Project/GUI/data.txt","r").read()
        # lines = graph_data.split('\n')
        # xs = []
        # ys = []
        # for line in lines:
        #     if len(line) > 1:
        #         x, y = line.split(',')
        #         xs.append(datetime.strptime(x, "%H:%M:%S"))
        #         #xs.append(float(x))
        #         ys.append(float(y))
        #     self.ax1.clear()
        #     self.ax1.plot(xs, ys)
        # graph = FigureCanvasTkAgg(fig, master=self.sensor)
        # graph.get_tk_widget().pack(side="top",fill='both',expand=1)
        # graph = FigureCanvasTkAgg(fig, master=self.sensor)
    # ani = animation.FuncAnimation(fig, grafiek, interval=5000)

    # plt.show()



root = tk.Tk()
root.config(background='white')
root.geometry("1000x700")
root.title("Project")
nb = ttk.Notebook(root)
properties = ttk.Frame(nb)
file = ttk.Frame(nb)

# second page
sensor1 = ttk.Frame(nb)
text = ScrolledText(sensor1)
text.pack(expand=1, fill="both")
sensor2 = ttk.Frame(nb)

app = Project(1, sensor1)

ani = animation.FuncAnimation(app.fig, animate, interval=5000)
plt.show()   

sensor3 = ttk.Frame(nb)
sensor4 = ttk.Frame(nb)


nb.add(properties, text='properties')
nb.add(file, text='File')
nb.add(sensor1, text='Sensor1')
nb.add(sensor2, text='Sensor2')
nb.add(sensor3, text='Sensor3')
nb.add(sensor4, text='Sensor4')

nb.pack(expand=1, fill="both")

root.mainloop()
     
ani = animation.FuncAnimation(app.fig, animate, interval=5000)
plt.show()