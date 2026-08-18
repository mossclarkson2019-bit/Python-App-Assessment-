#Imports
import tkinter as tk
import json
from turtle import title

#loading the data from the JSON files

with open("databases/vehicles.json", "r") as file:
    vehicles = json.load(file)                 # used gemini seach assist to fully understand the sytax and what is and isnt needed

with open("databases/parts.json", "r") as file:
    parts = json.load(file)


# Creating the main window
root = tk.Tk()
root.title("EuroPartPicker")









select_button = tk.Button(
    root,
    font=("Oswald", 14, "bold"),
    fg= "#031E49",
    bg="#4599fe",
    activebackground="#1e75df",
    text="SELECT PROJECT",
    width=25,
    height=3,
)

select_button.pack(pady=10)


create_button = tk.Button(
    root,
    font=("Oswald", 14, "bold"),
    fg= "#031E49",
    bg="#4599fe",
    activebackground="#1e75df",
    text="CREATE PROJECT",
    width=25,
    height=3,
)

create_button.pack(pady=10)



# Creating the event loop to keep the window visible
root.mainloop()

