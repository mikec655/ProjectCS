
from random import randint
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from tkinter import Tk, Label, Button, Entry
 
# these two imports are important
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import time
import _thread
from sensors import SensorReader


class Application(tk.Tk):

    def __init__(self):
        # initialise a window.
        super().__init__()
        self.config(background='white')
        self.geometry("1000x700")
        self.title("Application")
        nb = ttk.Notebook(self)
        properties = ttk.Frame(nb)
        
        rolluiklabel = Label(properties, text="Rolluik:")
        rolluiklabel.config(font=("Times new roman", 18))
        
        maxuitrollabel = Label(properties, text="Maximale uitrol:")
        maxuitrolbox = Entry(properties)

        minuitrollabel = Label(properties, text="Maximale Inrol:")
        minuitrolbox = Entry(properties)

        grenswaardelabel = Label(properties, text="Grenswaarde")
        grenswaardebox1 = Entry(properties)
        grenswaardebox2 = Entry(properties)
        grenswaardebox3 = Entry(properties)
        grenswaardebox4 = Entry(properties)
        grenswaardebox5 = Entry(properties)

        aantimerlabel = Label(properties, text="Automatisch aan")
        uittimerlabel = Label(properties, text="Automatisch uit")

        aantimerbox = Entry(properties)
        uittimerbox = Entry(properties)

        aanuitlabel = Label(properties, text="Aan uit")

        sensor1label = Label(properties, text="Licht Sensor")
        sensor2label = Label(properties, text="Temperatuur Sensor")
        sensor3label = Label(properties, text="SensorNaam")
        sensor4label = Label(properties, text="SensorNaam")
        sensor5label = Label(properties, text="SensorNaam")

        luikopenlabel = Label(properties, text="Rol luik open")
        luikdichtlabel = Label(properties, text="Rol luik dicht")

        rolluiklabel.grid(row = 0, column = 0, columnspan = 50, padx = 1, pady = 20, sticky = 'w')

        maxuitrollabel.grid(row=5, column=0 , columnspan = 20, padx = 1, pady = 1, sticky = 'w')
        maxuitrolbox.grid(row = 5, column=30 , columnspan = 20, padx = 1, pady = 1, sticky = 'n')

        minuitrollabel.grid(row=25, column=0 , columnspan = 20, padx = 1, pady = 1, sticky = 'w')
        minuitrolbox.grid(row = 25, column=30 , columnspan = 20, padx = 1, pady = 1, sticky = 'n')

        sensor1label.grid(row = 55, column = 0, columnspan = 40, padx = 1, pady = 1, sticky = 'w')
        sensor2label.grid(row = 56, column = 0, columnspan = 40, padx = 1, pady = 1, sticky = 'w')
        sensor3label.grid(row = 57, column = 0, columnspan = 40, padx = 1, pady = 1, sticky = 'w')
        sensor4label.grid(row = 58, column = 0, columnspan = 40, padx = 1, pady = 1, sticky = 'w')
        sensor5label.grid(row = 59, column = 0, columnspan = 40, padx = 1, pady = 1, sticky = 'w')

        aantimerlabel.grid(row = 60, column = 0, columnspan = 40, padx = 1, pady = 1, sticky = 'w')
        uittimerlabel.grid(row = 61, column = 0, columnspan = 40, padx = 1, pady = 1, sticky = 'w')

        luikopenlabel.grid(row = 62, column = 0, columnspan = 40, padx = 1, pady = 1, sticky = 'w')
        luikdichtlabel.grid(row = 63, column = 0, columnspan = 40, padx = 1, pady = 1, sticky = 'w')

        grenswaardelabel.grid(row = 50, column = 45, columnspan = 40, padx = 1, pady = 1, sticky = 'w')
        grenswaardebox1.grid(row = 55, column=45 , columnspan = 20, padx = 1, pady = 1, sticky = 'n')
        grenswaardebox2.grid(row = 56, column=45 , columnspan = 20, padx = 1, pady = 1, sticky = 'n')
        grenswaardebox3.grid(row = 57, column=45 , columnspan = 20, padx = 1, pady = 1, sticky = 'n')
        grenswaardebox4.grid(row = 58, column=45 , columnspan = 20, padx = 1, pady = 1, sticky = 'n')
        grenswaardebox5.grid(row = 59, column=45 , columnspan = 20, padx = 1, pady = 1, sticky = 'n')

        aantimerbox.grid(row = 60, column=45 , columnspan = 20, padx = 1, pady = 1, sticky = 'n')
        uittimerbox.grid(row = 61, column=45 , columnspan = 20, padx = 1, pady = 1, sticky = 'n')

        aanuitlabel.grid(row = 50, column = 260, columnspan = 40, padx = 1, pady = 1, sticky = 'w')
        s1box = Checkbutton(properties)
        s1box.grid(row = 55, column=280 , columnspan = 40, padx = 1, pady = 1, sticky = 'n')
        s2box = Checkbutton(properties)
        s2box.grid(row = 56, column=280 , columnspan = 40, padx = 1, pady = 1, sticky = 'n')
        s3box = Checkbutton(properties)
        s3box.grid(row = 57, column=280 , columnspan = 40, padx = 1, pady = 1, sticky = 'n')
        s4box = Checkbutton(properties)
        s4box.grid(row = 58, column=280 , columnspan = 40, padx = 1, pady = 1, sticky = 'n')
        s5box = Checkbutton(properties)
        s5box.grid(row = 59, column=280 , columnspan = 40, padx = 1, pady = 1, sticky = 'n')
        s6box = Checkbutton(properties)
        s6box.grid(row = 60, column=280 , columnspan = 40, padx = 1, pady = 1, sticky = 'n')
        s7box = Checkbutton(properties)
        s7box.grid(row = 61, column=280 , columnspan = 40, padx = 1, pady = 1, sticky = 'n')
        s8box = Checkbutton(properties)
        s8box.grid(row = 62, column=280 , columnspan = 40, padx = 1, pady = 1, sticky = 'n')
        s9box = Checkbutton(properties)
        s9box.grid(row = 63, column=280 , columnspan = 40, padx = 1, pady = 1, sticky = 'n')


        # file = ttk.Frame(nb)

        # # second page
        # sensor1 = ttk.Frame(nb)
        # text = ScrolledText(sensor1)
        # text.pack(expand=1, fill="both")
        sensor2graph = Graph(nb)        
        # sensor3 = ttk.Frame(nb)
        # sensor4 = ttk.Frame(nb)


        nb.add(properties, text='properties')
        # nb.add(file, text='File')
        # nb.add(sensor1, text='Sensor1')
        nb.add(sensor2graph, text='Sensor2')
        # nb.add(sensor3, text='Sensor3')
        # nb.add(sensor4, text='Sensor4')



        
        nb.pack(expand=1, fill="both")
        ani = animation.FuncAnimation(sensor2graph.fig, sensor2graph.redraw, interval=5000)

        
        self.mainloop()

class Graph(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.sensor_reader1 = SensorReader("COM7", "data.txt")
        _thread.start_new_thread(self.sensor_reader1.log, tuple())
        self.fig = plt.figure()
        self.ax1 = self.fig.add_subplot(1,1,1)

        self.graph = FigureCanvasTkAgg(self.fig, master=self)
        self.graph.get_tk_widget().pack(side="top",fill='both',expand=1)

    def redraw(self, i):
        graph_data = open(self.sensor_reader1.log_file_path,"r").read()
        lines = graph_data.split('\n')
        xs = []
        ys = []
        for line in lines:
            if len(line) > 1:
                x, y = line.split(',')
                # xs.append(datetime.strptime(x, "%H:%M:%S"))
                xs.append(x)
                #xs.append(float(x))
                ys.append(float(y))
            self.ax1.clear()
            self.ax1.plot(xs, ys)

     
if __name__ == '__main__':
    app = Application()