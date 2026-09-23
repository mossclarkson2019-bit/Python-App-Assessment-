#Imports
import tkinter as tk
import json
from tkinter import ttk

#loading the data from the JSON files

with open("databases/vehicles.json", "r") as file:
    vehicles = json.load(file)                 # used gemini seach assist to fully understand the sytax and what is and isnt needed

with open("databases/parts.json", "r") as file:
    parts = json.load(file)

with open("databases/projects.json", "r") as file:
    projects = json.load(file)

with open("databases/users.json", "r") as file:
    users = json.load(file)


current_user = None  # Variable to store the current user for my sign in feature under the select project button

root = tk.Tk() #moved to the top as it is the main window and should be created before any other widgets, then realized this structure is unintuitive as it should just be before the first widget is created not before the functions section
root.title("SouthernEuroParts PartsPicker")
root.geometry("800x600")


def show_projects():
    clear_window()

    title = tk.Label(
        content,
        text="My Projects",
        font=("Arial", 24),
        bg="white"

    )
    title.pack(pady=30)

    for project in projects:                   #function to show the current users projects, i uised gemini search assist
        if project["owner"] == current_user:

            project_button = tk.Button(
                content,
                text=project["name"],
                command=lambda p=project: open_project(p)
            )
            project_button.pack(pady=5)

    make_back_button(show_home)


def select_project(): # first function of my app
    if current_user is None:#if not signed in
        show_sign_in(show_projects)#ask to sign in
    else:
        show_projects() #otherwise go to the current users project library


def select_create_project():
    if current_user is None:
        show_sign_in(show_create_project)
    else:
        show_create_project()


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
    height=3,
    command=select_create_project
)
    create_button.pack(pady=10)


def show_create_project():
    clear_window()

    title = tk.Label(
        content,
        text="Create Project",
        font=("Oswald", 24, "bold"),
        bg="white"
    )
    title.pack(pady=30)

    name_label = tk.Label(
        content,
        text="Project Name",
        bg="white"
    )
    name_label.pack()

    name_entry = tk.Entry(content)
    name_entry.pack(pady=5)

    vehicle_label = tk.Label(
        content,
        text="Vehicle",
        bg="white"
    )
    vehicle_label.pack(pady=(15, 0))

    vehicle_options = []
    for vehicle in vehicles:
        vehicle_options.append(vehicle["make"] + " " + vehicle["model"])

    vehicle_combobox = ttk.Combobox(
        content,
        values=vehicle_options,
        state="readonly",  # stops users typing something not in the list
        width=30
    )
    vehicle_combobox.pack(pady=5)

    error_label = tk.Label(
        content,
        text="",
        fg="red",
        bg="white"
    )
    error_label.pack()

    create_button = tk.Button(
        content,
        text="CREATE PROJECT",
        command=lambda: create_project(
            name_entry.get(),
            vehicle_combobox.get(),
            error_label
        )
    )
    create_button.pack(pady=20)

    make_back_button(show_home)


def create_project(project_name, vehicle, error_label):

    if project_name == "":
        error_label.config(text="Please enter a project name")
        return

    if vehicle == "":
        error_label.config(text="Please select a vehicle")
        return

    new_project = {
        "name": project_name,
        "owner": current_user,
        "vehicle": vehicle
    }

    projects.append(new_project)

    with open("databases/projects.json", "w") as file:
        json.dump(projects, file, indent=4)

    show_projects()


def show_sign_in(destination=show_projects):
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

    error_label = tk.Label( #the error label variable
    content,
    text="",
    fg="red",
    bg="white"
    )
    error_label.pack()

    sign_in_button = tk.Button(
    content,
    text="SIGN IN",
    command=lambda: sign_in(
        username_entry.get(),
        password_entry.get(),
        error_label,
        destination
    )
 )
    sign_in_button.pack(pady=20)


    create_account_button = tk.Button(
    content,
    text="CREATE ACCOUNT",
    command=show_create_account
    )

    create_account_button.pack(pady=5)


    make_back_button(show_home)


def sign_in(username, password, error_label, destination=show_projects):
    global current_user #holds the the current user that has signed in

    for user in users:
        if user["username"] == username and user["password"] == password:   #i used claude ai to fully understand how this syntax works and what is and isnt needed
            current_user = username
            destination()  # Call the destination function after successful sign-in, was hardcoded to show_projects() but now it takes the user to the page they were trying to access before being prompted to sign in (the create project page in this case)
            return

    error_label.config(text="Incorrect username or password. Please try again.") #error label that identifies to users that they entered somehting incorrectly


def show_create_account():
    clear_window()

    title = tk.Label(
        content,
        text="Create Account",
        font=("Oswald", 24, "bold"),
        bg="white"
    )
    title.pack(pady=30)

    username_label = tk.Label(
        content,
        text="Username",
        bg="white"
    )
    username_label.pack()

    username_entry = tk.Entry(content)
    username_entry.pack(pady=5)

    password_label = tk.Label(
        content,
        text="Password",
        bg="white"
    )
    password_label.pack(pady=(15, 0))

    password_entry = tk.Entry(
        content,
        show="*"
    )
    password_entry.pack(pady=5)

    confirm_label = tk.Label(
        content,
        text="Confirm Password",
        bg="white"
    )
    confirm_label.pack(pady=(15, 0))

    confirm_entry = tk.Entry(
        content,
        show="*"
    )
    confirm_entry.pack(pady=5)

    error_label = tk.Label(
        content,
        text="",
        fg="red",
        bg="white"
    )
    error_label.pack()

    create_button = tk.Button(
        content,
        text="CREATE ACCOUNT",
        command=lambda: create_account(
            username_entry.get(),
            password_entry.get(),
            confirm_entry.get(),
            error_label
        )
    )
    create_button.pack(pady=20)

    make_back_button(show_sign_in)


def create_account(username, password, confirm_password, error_label):

    if username == "":
        error_label.config(text="Please enter a username")
        return

    if password == "":
        error_label.config(text="Please enter a password")
        return

    if password != confirm_password:
        error_label.config(text="Passwords do not match")
        return

    for user in users:
        if user["username"] == username:
            error_label.config(text="Username already exists")
            return

    new_user = {
        "username": username,
        "password": password
    }

    users.append(new_user)

    with open("databases/users.json", "w") as file:
        json.dump(users, file, indent=4)

    error_label.config(
        text="Account created successfully",
        fg="green"
    )


def get_project_vehicle(project):

    for vehicle in vehicles: #

        full_name = vehicle["make"] + " " + vehicle["model"] # combines the make and model of the vehicle to match the format stored in the project data

        if full_name == project["vehicle"]: #
            return vehicle #

    return None




def check_compatibility(part, project): # checks compatability between a part and a project based on the vehicle and engine
    vehicle = get_project_vehicle(project) # fetches the vehicle data for the current project

    if vehicle is None: # if the vehicle isnt found, it returns false indicating incompatibility
        return False

    # checks if the part is directly compatible with the vehicle
    if project["vehicle"] in part["compatible_vehicles"]:
        return True

    # checks if the part is compatible with the vehicle's engine
    if vehicle["engine"] in part["compatible_engines"]:
        return True

    return False


def show_part_library(project): # part library page that displays all parts, their compatibility status with the current project and their price. I used claude ai to understand how to refer to the compability check and display it and used a combination of my html/css knowledge, my grok learning and claude ai to figure out the syntax for the price and name labels

    clear_window()

    title = tk.Label(
        content,
        text="Part Library",
        font=("Oswald", 24, "bold"),
        bg="white"
    )
    title.pack(pady=20)

    for part in parts:

        compatible = check_compatibility(part, project) # checks if the part is compatible with the project and stores the result in the variable 'compatible'
        part_frame = tk.Frame(
            content,
            bg="#eeeeee"
        )
        part_frame.pack(
            fill="x",
            padx=50,
            pady=5
        )

        name_label = tk.Label(
            part_frame,
            text=part["name"],
            font=("Arial", 14, "bold"),
            bg="#eeeeee"
        )
        name_label.pack(side="left", padx=10)

        price_label = tk.Label(
            part_frame,
            text="$" + str(part["price"]),
            bg="#eeeeee"
        )
        price_label.pack(side="left", padx=10)

        if compatible:
            compatibility_label = tk.Label(
                part_frame,
                text="Compatible",
                fg="green",
                bg="#eeeeee"
            )
        else:
            compatibility_label = tk.Label(
                part_frame,
                text="Not confirmed",
                fg="red",
                bg="#eeeeee"
            )

        compatibility_label.pack(side="left", padx=10)

    make_back_button(lambda: open_project(project))


def open_project(project):
    clear_window()

    title = tk.Label(
        content,
        text=project["name"],
        font=("Arial", 24),
        bg="white"
    )
    title.pack(pady=30)

    vehicle_label = tk.Label(
        content,
        text="Vehicle: " + project.get("vehicle", "Not set"),
    font=("Arial", 14),
    bg="white"
    )
    vehicle_label.pack(pady=10)

    browse_button = tk.Button(
        content,
        text="BROWSE PARTS",
        command=lambda: show_part_library(project)
    )
    browse_button.pack(pady=20)

    make_back_button(show_projects)


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

southern_text = brand.create_text(
    0, 20,
    text="Southern",
    font=("Oswald", 20, "bold"),
    fill="white",
    anchor="w"
)

euro_text = brand.create_text(
    0, 20,
    text="Euro",
    font=("Oswald", 20, "bold"),
    fill="#4599fe",
    anchor="w"
)

parts_text = brand.create_text(
    0, 20,
    text="Parts",
    font=("Oswald", 20, "bold"),
    fill="white",
    anchor="w"
)

#making tkinter do the calc and placement work for me instead of playing round with coords
# Get the width of each text element
southern_width = brand.bbox(southern_text)[2] - brand.bbox(southern_text)[0]
euro_width = brand.bbox(euro_text)[2] - brand.bbox(euro_text)[0]

# Place the text elements one after the other
brand.coords(euro_text, southern_width, 20)
brand.coords(parts_text, southern_width + euro_width, 20)


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


