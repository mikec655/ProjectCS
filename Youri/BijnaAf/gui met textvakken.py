
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

        graph_data = open("C:\\Users\\youri\\OneDrive\\Documenten\\ProjectCS\\Centrale\\centrale\\data.txt","r").read()
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
        
        rolluiklabel = Label(properties, text="Rolluik:")
        rolluiklabel.config(font=("Times new roman", 18))
        
        maxuitrollabel = Label(properties, text="Maximale uitrol:")
        maxuitrolbox = Entry(properties)

        minuitrollabel = Label(properties, text="Maximale Inrol:")
        minuitrolbox = Entry(properties)

        minwaardelabel = Label(properties, text="Minimale waarde")
        minwaardebox1 = Entry(properties)
        minwaardebox2 = Entry(properties)
        minwaardebox3 = Entry(properties)
        minwaardebox4 = Entry(properties)
        minwaardebox5 = Entry(properties)

        maxwaardelabel = Label(properties, text="Maximale waarde")
        maxwaardebox1 = Entry(properties)
        maxwaardebox2 = Entry(properties)
        maxwaardebox3 = Entry(properties)
        maxwaardebox4 = Entry(properties)
        maxwaardebox5 = Entry(properties)

        uitrolpercentagelabel = Label(properties, text="Uitrol percentage")
        uitrolpercentagebox1 = Entry(properties)
        uitrolpercentagebox2 = Entry(properties)
        uitrolpercentagebox3 = Entry(properties)
        uitrolpercentagebox4 = Entry(properties)
        uitrolpercentagebox5 = Entry(properties)

        aanuitlabel = Label(properties, text="Aan uit")

        sensor1label = Label(properties, text="Licht Sensor")
        sensor2label = Label(properties, text="Temperatuur Sensor")
        sensor3label = Label(properties, text="SensorNaam")
        sensor4label = Label(properties, text="SensorNaam")
        sensor5label = Label(properties, text="SensorNaam")
        manueellabel = Label(properties, text="Manueel")

        # label.pack(fill=Y,padx=10)

        # label.pack(expand=1, fill="both")
        rolluiklabel.grid(row = 0, column = 0, columnspan = 50, padx = 1, pady = 20, sticky = 'w')
       

        maxuitrollabel.grid(row=5, column=0 , columnspan = 20, padx = 1, pady = 1, sticky = 'w')
        maxuitrolbox.grid(row = 15, column=0 , columnspan = 20, padx = 1, pady = 1, sticky = 'n')

        minuitrollabel.grid(row=25, column=0 , columnspan = 20, padx = 1, pady = 1, sticky = 'w')
        minuitrolbox.grid(row = 35, column=0 , columnspan = 20, padx = 1, pady = 1, sticky = 'n')

        autobox = Checkbutton(properties, text="Automatisch")
        autobox.grid(row = 45, column=1, padx = 1, pady = 1, sticky = 'n')

        sensor1label.grid(row = 55, column = 0, columnspan = 40, padx = 1, pady = 1, sticky = 'w')
        sensor2label.grid(row = 56, column = 0, columnspan = 40, padx = 1, pady = 1, sticky = 'w')
        sensor3label.grid(row = 57, column = 0, columnspan = 40, padx = 1, pady = 1, sticky = 'w')
        sensor4label.grid(row = 58, column = 0, columnspan = 40, padx = 1, pady = 1, sticky = 'w')
        sensor5label.grid(row = 59, column = 0, columnspan = 40, padx = 1, pady = 1, sticky = 'w')

        minwaardelabel.grid(row = 50, column = 30, columnspan = 40, padx = 1, pady = 1, sticky = 'w')
        minwaardebox1.grid(row = 55, column=30 , columnspan = 20, padx = 1, pady = 1, sticky = 'n')
        minwaardebox2.grid(row = 56, column=30 , columnspan = 20, padx = 1, pady = 1, sticky = 'n')
        minwaardebox3.grid(row = 57, column=30 , columnspan = 20, padx = 1, pady = 1, sticky = 'n')
        minwaardebox4.grid(row = 58, column=30 , columnspan = 20, padx = 1, pady = 1, sticky = 'n')
        minwaardebox5.grid(row = 59, column=30 , columnspan = 20, padx = 1, pady = 1, sticky = 'n')
        
        maxwaardelabel.grid(row = 50, column = 70, columnspan = 40, padx = 1, pady = 1, sticky = 'w')
        maxwaardebox1.grid(row = 55, column=70 , columnspan = 20, padx = 1, pady = 1, sticky = 'n')
        maxwaardebox2.grid(row = 56, column=70 , columnspan = 20, padx = 1, pady = 1, sticky = 'n')
        maxwaardebox3.grid(row = 57, column=70 , columnspan = 20, padx = 1, pady = 1, sticky = 'n')
        maxwaardebox4.grid(row = 58, column=70 , columnspan = 20, padx = 1, pady = 1, sticky = 'n')
        maxwaardebox5.grid(row = 59, column=70 , columnspan = 20, padx = 1, pady = 1, sticky = 'n')

        uitrolpercentagelabel.grid(row = 50, column = 130, columnspan = 40, padx = 1, pady = 1, sticky = 'w')
        uitrolpercentagebox1.grid(row = 55, column=130 , columnspan = 20, padx = 1, pady = 1, sticky = 'n')
        uitrolpercentagebox2.grid(row = 56, column=130 , columnspan = 20, padx = 1, pady = 1, sticky = 'n')
        uitrolpercentagebox3.grid(row = 57, column=130 , columnspan = 20, padx = 1, pady = 1, sticky = 'n')
        uitrolpercentagebox4.grid(row = 58, column=130 , columnspan = 20, padx = 1, pady = 1, sticky = 'n')
        uitrolpercentagebox5.grid(row = 59, column=130 , columnspan = 20, padx = 1, pady = 1, sticky = 'n')

        aanuitlabel.grid(row = 50, column = 180, columnspan = 40, padx = 1, pady = 1, sticky = 'w')
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

        manueellabel.grid(row = 100, column = 0, columnspan = 40, padx = 1, pady = 1, sticky = 'w')


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