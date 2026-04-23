import tkinter as tk

class Dashboard:
    def __init__(self, reader):
        self.reader = reader
        self.root = tk.Tk()
        self.root.title("CanSat Dashboard")
        self.root.geometry("400x300")

        self.alt_label = tk.Label(self.root, text="Altitude: --", font=("Arial", 14))
        self.alt_label.pack()

        self.status_label = tk.Label(self.root, text="Status: --", font=("Arial", 14))
        self.status_label.pack()

        self.deploy_label = tk.Label(self.root, text="Deploy: --", font=("Arial", 14))
        self.deploy_label.pack()

        self.update()

    def update(self):
        self.alt_label.config(text=f"Altitude: {self.reader.altitude} m")
        self.status_label.config(text=f"Status: {self.reader.status}")
        self.deploy_label.config(text=f"Deploy: {self.reader.deploy}")

        self.root.after(500, self.update)

    def run(self):
        self.root.mainloop()