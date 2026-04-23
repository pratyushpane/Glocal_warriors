import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class Plotter:
    def __init__(self, reader):
        self.reader = reader
        self.fig, self.ax = plt.subplots()

    def update(self, frame):
        self.ax.clear()
        self.ax.plot(self.reader.time_data, self.reader.alt_data)
        self.ax.set_title("Altitude vs Time")
        self.ax.set_xlabel("Time")
        self.ax.set_ylabel("Altitude (m)")

    def start(self):
        FuncAnimation(self.fig, self.update, interval=1000)
        plt.show()