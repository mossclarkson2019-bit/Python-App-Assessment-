#Imports
import tkinter as tk
import json


#loading the data from the JSON files

with open("databases/vehicles.json", "r") as file:
    vehicles = json.load(file)                 # used gemini seach assist to fully understand the sytax and what is and isnt needed

with open("databases/parts.json", "r") as file:
    parts = json.load(file)

 



def select_project(): # first function of my app
 if current_user is None: #if not signed in
    show_sign_in()       #ask to sign in
 else:
    show_projects() #otherwise go to the current users project library



def clear_window(): #function to clear the window of all widgets for swithcing pages, I used gemini search assist to help me understand the syntax and what is and isnt needed
    for widget in content.winfo_children():  #was set to root.winfo_children() which destrwoyed evrything including the header and footer, so I changed it to content.winfo_children() to only destroy the content 
        widget.destroy()



def make_back_button(destination):
        back_button = tk.Button(
            content,
            text="BACK",
            command=destination
        )
        back_button.pack(pady=10)


def show_home():
    clear_window()

    select_button = tk.Button(
        content,
        font=("Oswald", 14, "bold"),
        fg="#031E49",
        bg="#4599fe",
        activebackground="#1e75df",
        text="SELECT PROJECT",
        width=25,
        height=3,
        command=select_project
    )
    select_button.pack(pady=10)

    create_button = tk.Button(
        content,
        font=("Oswald", 14, "bold"),
        fg="#031E49",
        bg="#4599fe",
        activebackground="#1e75df",
        text="CREATE PROJECT",
        width=25,
        height=3
    )
    create_button.pack(pady=10)


def show_sign_in():
    clear_window()

  
            

    title = tk.Label(
        content,
        text="Sign In",
        font=("Oswald", 24, "bold"),
        bg="white"
    )
    title.pack(pady=40)

    username_label = tk.Label(
        content,
        text="Username",
        bg="white"
    )
    username_label.pack()

    username_entry = tk.Entry(content)
    username_entry.pack(pady=5)

    password_label = tk.Label( #label above the password entry box
        content,
        text="Password",
        bg="white"
    )
    password_label.pack(pady=(15, 0))

    password_entry = tk.Entry(
        content,
        show="*" #wont display anything typed in the box, will laer be an option to show the password in plain text if the user wants
    )
    password_entry.pack(pady=5)

    sign_in_button = tk.Button(
        content,
        text="SIGN IN"
    )
    sign_in_button.pack(pady=25)

    make_back_button(show_home)




def sign_in(): 
    global current_user
    current_user = "user"
    show_projects()


def show_projects():
    clear_window()

    title = tk.Label(
            content,
            text="Select Project",
            font=("Arial", 24)
        )
    title.pack(pady=50)

    project_button = tk.Button(
            content,
            text="My Project"
        )
    project_button.pack()





root = tk.Tk() #moved to the top as it is the main window and should be created before any other widgets, then realized this structure is unintuitive as it should just be before the first widget is created not before the functions section
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




content = tk.Frame(root, bg="white") #moved up to top to test if this fixed my issues with the widgets that ref content, it fixed it but moved everything above the header so just moved it below the header and now everthign works corrctly
content.pack(fill="both", expand=True)

current_user = None  # Variable to store the current user for my sign in feature under the select project button











footer = tk.Frame(root, bg="#031E49", height=70)
footer.pack(side=tk.BOTTOM, fill=tk.X)

footer_label = tk.Label(
    footer,
    text="© 2023 EuroPartPicker. All rights reserved.",
    font=("Noto Sans Chakma", 12),
    fg="white",
    bg="#031E49"
)

footer_label.pack(side='right', pady=10)



show_home()  

# Creating the event loop to keep the window visible
root.mainloop()

