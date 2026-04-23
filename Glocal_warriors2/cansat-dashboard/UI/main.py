from threading import Thread
from serial_reader import SerialReader
from gui import Dashboard
from plotter import Plotter

reader = SerialReader()

# Start serial reading in background
def serial_loop():
    while True:
        reader.read()

Thread(target=serial_loop, daemon=True).start()

# Start graph in another thread
plotter = Plotter(reader)
Thread(target=plotter.start, daemon=True).start()

# Start GUI
app = Dashboard(reader)
app.run()