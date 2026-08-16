#Imports
import tkinter as tk
import json


with open("data/vehicles.json", "r") as file:
    vehicles = json.load(file)

with open("data/parts.json", "r") as file:
    parts = json.load(file)


# Creating the main window
root = tk.Tk()
root.title("EuroPartPicker")

# Creating the event loop to keep the window visible
root.mainloop()

