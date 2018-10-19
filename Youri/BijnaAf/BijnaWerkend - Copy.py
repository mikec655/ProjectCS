
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
import threading

class Project:

    fig = plt.figure()
    ax1 = fig.add_subplot(1,1,1)
     
    
    def grafiek(self, sensor):
        self.sensor = sensor
        fig = Figure()
        
        ax = fig.add_subplot(111)
        ax.set_xlabel("X axis")
        ax.set_ylabel("Y axis")
        ax.grid()
     
        graph = FigureCanvasTkAgg(fig, master=self.sensor)
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

        # graph = FigureCanvasTkAgg(fig, master=self.sensor)
        # graph.get_tk_widget().pack(side="top",fill='both',expand=1)
        # graph = FigureCanvasTkAgg(fig, master=self.sensor)
    
    ani = animation.FuncAnimation(fig, grafiek, interval=5000)
            # graph.get_tk_widget().pack(side="top",fill='both',expand=1)


    def app(self):
        # initialise a window.
        root = tk.Tk()
        root.config(background='white')
        root.geometry("1000x700")
        root.title("Project")
        nb = ttk.Notebook(root)
        properties = ttk.Frame(nb)
        
        label = Label(properties, text="Rolluik:")
        label.config(width=20)
        label.config(font=("Times new roman", 18))
        
        label1 = Label(properties, text="Maximale uitrol:")
        entry_1 = Entry(properties)

        label2 = Label(properties, text="Maximale Inrol:")
        entry_2 = Entry(properties)

        label3 = Label(properties, text="Minimale waarde")
        label4 = Label(properties, text="Maximale waarde")
        label5 = Label(properties, text="Uitrol percentage")
        label6 = Label(properties, text="Aan uit")

        label7 = Label(properties, text="Licht Sensor")
        label8 = Label(properties, text="Temperatuur Sensor")
        label9 = Label(properties, text="SensorNaam")
        label10 = Label(properties, text="SensorNaam")
        label11 = Label(properties, text="SensorNaam")
        label12 = Label(properties, text="Manueel")

        # label.pack(fill=Y,padx=10)

        # label.pack(expand=1, fill="both")
        label.grid(row = 0, column = 0, columnspan = 50, padx = 1, pady = 20, sticky = 'w')
       

        label1.grid(row=5, column=20 , columnspan = 20, padx = 1, pady = 1, sticky = 'w')
        entry_1.grid(row = 15, column=20 , columnspan = 20, padx = 1, pady = 1, sticky = 'n')

        label2.grid(row=25, column=20 , columnspan = 20, padx = 1, pady = 1, sticky = 'w')
        entry_2.grid(row = 35, column=20 , columnspan = 20, padx = 1, pady = 1, sticky = 'n')

        c = Checkbutton(properties, text="Automatisch")
        c.grid(row = 45, column=27 , columnspan = 40, padx = 1, pady = 1, sticky = 'n')

        label3.grid(row = 50, column = 50, columnspan = 40, padx = 1, pady = 1, sticky = 'w')
        label4.grid(row = 50, column = 100, columnspan = 40, padx = 1, pady = 1, sticky = 'w')
        label5.grid(row = 50, column = 150, columnspan = 40, padx = 1, pady = 1, sticky = 'w')
        label6.grid(row = 50, column = 200, columnspan = 40, padx = 1, pady = 1, sticky = 'w')
        c1 = Checkbutton(properties)
        c1.grid(row = 55, column=300 , columnspan = 40, padx = 1, pady = 1, sticky = 'n')
        c2 = Checkbutton(properties)
        c2.grid(row = 56, column=300 , columnspan = 40, padx = 1, pady = 1, sticky = 'n')
        c3 = Checkbutton(properties)
        c3.grid(row = 57, column=300 , columnspan = 40, padx = 1, pady = 1, sticky = 'n')
        c4 = Checkbutton(properties)
        c4.grid(row = 58, column=300 , columnspan = 40, padx = 1, pady = 1, sticky = 'n')
        c5 = Checkbutton(properties)
        c5.grid(row = 59, column=300 , columnspan = 40, padx = 1, pady = 1, sticky = 'n')

        label7.grid(row = 55, column = 20, columnspan = 40, padx = 1, pady = 1, sticky = 'w')
        label8.grid(row = 56, column = 20, columnspan = 40, padx = 1, pady = 1, sticky = 'w')
        label9.grid(row = 57, column = 20, columnspan = 40, padx = 1, pady = 1, sticky = 'w')
        label10.grid(row = 58, column = 20, columnspan = 40, padx = 1, pady = 1, sticky = 'w')
        label11.grid(row = 59, column = 20, columnspan = 40, padx = 1, pady = 1, sticky = 'w')
        label12.grid(row = 100, column = 20, columnspan = 40, padx = 1, pady = 1, sticky = 'w')


        file = ttk.Frame(nb)

        # second page
        sensor1 = ttk.Frame(nb)
        text = ScrolledText(sensor1)
        text.pack(expand=1, fill="both")
        sensor2 = ttk.Frame(nb)
        app.grafiek(sensor2)        
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
     
if __name__ == '__main__':
    app = Project()
    app.app()

    ani = animation.FuncAnimation(fig, animate, interval=5000)
    plt.show()