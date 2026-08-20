#Imports
import tkinter as tk
import json
import turtle as turtle

#loading the data from the JSON files

with open("databases/vehicles.json", "r") as file:
    vehicles = json.load(file)                 # used gemini seach assist to fully understand the sytax and what is and isnt needed

with open("databases/parts.json", "r") as file:
    parts = json.load(file)


# Creating the main window
root = tk.Tk()
root.title("SouthernEuroParts PartsPicker")
root.geometry("800x600")




header = tk.Frame(root, bg="#031E49", height=70)
header.pack(fill=tk.X)

header.grid_columnconfigure(0, weight=1)
header.grid_columnconfigure(1, weight=1)
header.grid_columnconfigure(2, weight=1)



brand = tk.Canvas(
    header,
    bg="#031E49",
    highlightthickness=0,
    height=40,
    width=300 #increased from 250 to 300 as the end of the word "Parts" was being cut off
)

brand.pack(side="left", padx=10)

southern = brand.create_text(
    0, 20,
    text="Southern",
    font=("Oswald", 20, "bold"),
    fill="white",
    anchor="w"
)

euro = brand.create_text(
    0, 20,
    text="Euro",
    font=("Oswald", 20, "bold"),
    fill="#4599fe",
    anchor="w"
)

parts = brand.create_text(
    0, 20,
    text="Parts",
    font=("Oswald", 20, "bold"),
    fill="white",
    anchor="w"
)

#making tkinter do the calc and placement work for me instead of playing round with coords
# Get the width of each text element
southern_width = brand.bbox(southern)[2] - brand.bbox(southern)[0]
euro_width = brand.bbox(euro)[2] - brand.bbox(euro)[0]

# Place the text elements one after the other
brand.coords(euro, southern_width, 20)
brand.coords(parts, southern_width + euro_width, 20)




centre = header_label = tk.Label( #New centredd logo to define separate the website from the partpicker app
    header,
    text="EuroPartsPicker",
    font=("Oswald", 20, "bold"),
    fg="white",
    bg="#031E49"
)
centre.place(relx=0.5, rely=0.5, anchor="center") #centering using the middle grid would not work with the empty column on the right, so I used place to center it instead





select_button = tk.Button( #button to select an existing project, if clicked while signed in it will take you to a project library, if not signed in it will prompt you to
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


create_button = tk.Button( #button for creating new project. if you clicked while not signed in, it will prompt you to sign in or be a guest before creating
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



footer = tk.Frame(root, bg="#031E49", height=70)
footer.pack(side=tk.BOTTOM, fill=tk.X)

footer_label = tk.Label(
    footer,
    text="© 2023 EuroPartPicker. All rights reserved.",
    font=("Oswald", 12),
    fg="white",
    bg="#031E49"
)

footer_label.pack(side='right', pady=10)





# Creating the event loop to keep the window visible
root.mainloop()

