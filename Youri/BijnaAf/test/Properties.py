from tkinter import ttk
from tkinter import Tk, Label, Button
import tkinter as tk
from tkinter import *
# from tkinter.scrolledtext import ScrolledText
# import matplotlib.pyplot as plt
# import matplotlib.animation as animation
# from sensors import SensorReader
# import _thread
# from datetime import datetime

class Gui:

    # gui = Gui(root)

    def __init__(self):
        pass

    def app(self,master):
        root.title("Project")
        root.configure(background='black')
        root.geometry("800x600")

        nb = ttk.Notebook(root)
        
        instellingen = ttk.Frame(nb)

        gui.instellingen()

        sensor1 = ttk.Frame(nb)
        sensor2 = ttk.Frame(nb)
        sensor3 = ttk.Frame(nb)
        sensor4 = ttk.Frame(nb)
        
        nb.add(instellingen, text='instellingen')

        nb.add(sensor1, text='Sensor1')
        nb.add(sensor2, text='Sensor2')
        nb.add(sensor3, text='Sensor3')
        nb.add(sensor4, text='Sensor4')


        nb.pack(expand=1, fill="both")
        # plt.show()
        root.mainloop()

    def animate(self,i):

        graph_data = open("Centrale/centrale/data.txt","r").read()
        lines = graph_data.split('\n')
        xs = []
        ys = []
        for line in lines:
            if len(line) > 1:
                x, y = line.split(',')
                xs.append(datetime.strptime(x, "%H:%M:%S"))
                #xs.append(float(x))
                ys.append(float(y))
                ax1.clear()
                ax1.plot(xs, ys)

    
    def instellingen(self):
        
        label_1 = Label(root, text="Name")
        label_2 = Label(root, text="Password")

        entry_1 = Entry(root)
        entry_2 = Entry(root)

        # label_1.grid(row=0, sticky=E)
        # label_2.grid(row=1, sticky=E)

        # entry_1.grid(row=0,column=1)
        # entry_2.grid(row=1,column=1)

        c = Checkbutton(root, text="Hou me ingelogd")
        # c.grid(columnspan=2)
        # root.mainloop()


if __name__ == "__main__":
    root = Tk()
    gui = Gui()
    gui.app(root)