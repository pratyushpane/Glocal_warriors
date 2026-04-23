import serial
from config import PORT, BAUD
from utils.parser import parse_line

class SerialReader:
    def __init__(self):
        self.ser = serial.Serial(PORT, BAUD, timeout=1)
        self.altitude = 0
        self.status = "INIT"
        self.deploy = "NO"
        self.time = 0
        self.alt_data = []
        self.time_data = []

    def read(self):
        line = self.ser.readline().decode().strip()

        if line:
            data = parse_line(line)

            if "altitude" in data:
                self.altitude = data["altitude"]
                self.alt_data.append(self.altitude)
                self.time_data.append(self.time)
                self.time += 1

            if "status" in data:
                self.status = data["status"]

            if "deploy" in data:
                self.deploy = data["deploy"]