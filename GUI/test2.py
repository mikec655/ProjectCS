from tkinter import ttk
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from sensors import SensorReader
import _thread
from datetime import datetime
from random import randint
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import time
import threading

class Gui:
	fig = plt.figure()
	ax1 = fig.add_subplot(1,1,1)

	def demo(self):
		root = tk.Tk()
		root.title("Project")
		# root.configure(background='black')
		root.geometry("800x600")

		nb = ttk.Notebook(root)

		# adding Frames as pages for the ttk.Notebook 
		# first page, which would get widgets gridded into it
		file = ttk.Frame(nb)

		# second page
		sensor1 = ttk.Frame(nb)
		text = ScrolledText(sensor1)
		text.pack(expand=1, fill="both")
		sensor2 = ttk.Frame(nb)
		# fig = plt.figure()
		# ax1 = fig.add_subplot(1,1,1)
		# ani = animation.FuncAnimation(self.fig,self.animate, interval=5000)
		# ani.pack(expand=1, fill="both")
	    graph = FigureCanvasTkAgg(fig, master=root)
		graph.get_tk_widget().pack(side="top",fill='both',expand=True)

		sensor3 = ttk.Frame(nb)
		sensor4 = ttk.Frame(nb)
		properties = ttk.Frame(nb)


		nb.add(file, text='File')
		nb.add(sensor1, text='Sensor1')
		nb.add(sensor2, text='Sensor2')
		nb.add(sensor3, text='Sensor3')
		nb.add(sensor4, text='Sensor4')
		nb.add(properties, text='properties')


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

if __name__ == "__main__":
	gui = Gui()
	gui.demo()

