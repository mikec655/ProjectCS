from tkinter import ttk
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from sensors import SensorReader
import _thread
from datetime import datetime
from tkinter import Tk, Label, Button

class Gui:
	fig = plt.figure()
	ax1 = fig.add_subplot(1,1,1)

	def demo(self):
		root = tk.Tk()
		root.title("Project")
		root.geometry("800x600")

		nb = ttk.Notebook(root)

		properties = ttk.Frame(nb)
		file = ttk.Frame(nb)

		# second page
		sensor1 = ttk.Frame(nb)
		text = ScrolledText(sensor1)
		text.pack(expand=1, fill="both")
		sensor2 = ttk.Frame(nb)
		
		btn = Button(nb, text="Click Me", bg="orange", fg="red")
		btn.pack(expand=0, fill="both")
		
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

	def animate(self,i):

		graph_data = open("Centrale/centrale/data.txt","r").read()
		lines = graph_data.split('\n')
		xs = []
		ys = []
		for line in lines:
			if len(line) > 1:
				x, y = line.split(',')
				xs.append(datetime.strptime(x, "%H:%M:%S"))
				ys.append(float(y))
				ax1.clear()
				ax1.plot(xs, ys)

if __name__ == "__main__":
	gui = Gui()
	gui.demo()


