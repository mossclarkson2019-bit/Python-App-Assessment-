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


# Functions section

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


def select_create_project(): # function to select the create project page, it checks if the user is signed in and if not, it prompts them to sign in before allowing them to create a project
    if current_user is None:
        show_sign_in(show_create_project)
    else:
        show_create_project()


def clear_window(): #function to clear the window of all widgets for swithcing pages, I used gemini search assist to help me understand the syntax and what is and isnt needed
    for widget in content.winfo_children():  #was set to root.winfo_children() which destrwoyed evrything including the header and footer, so I changed it to content.winfo_children() to only destroy the content
        widget.destroy()


def make_back_button(destination): #reusable function to create a back button that takes the user to the specified destination page
        back_button = tk.Button(
            content,
            text="BACK",
            command=destination
        )
        back_button.pack(pady=10)


def show_home(): # function to show the home page with options to select or create a project
    clear_window()

    select_button = tk.Button(            # button to select a project
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

    create_button = tk.Button(              # button to create a new project
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


def show_create_project():                 # function to show the create project page
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


def create_project(project_name, vehicle, error_label): # function to create a new project, it checks for empty fields and saves the new project data to the projects.json file. i extrapolated my knowledge of the create_account function to create this function

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


def show_sign_in(destination=show_projects):  # function to show the sign in page, it takes an optional destination parameter that defines where the user will be taken after signing in i swapped to this as i had everything hardcoded which lead to my create project function taking the user to the project library instead of the create project page after signing in, so now it takes the user to the page they were trying to access before being prompted to sign in
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


def show_create_account(): # create account page, adapted from the sign in page
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

    confirm_label = tk.Label(           #label for the confirm password entry box, this is to ensure the user hasnt made a typo when entering their password
        content,
        text="Confirm Password",
        bg="white"
    )
    confirm_label.pack(pady=(15, 0))

    confirm_entry = tk.Entry(             # added confirm password entry box compared to the sign in page
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

    create_button = tk.Button(             # button to create the account, it calls the create_account function when clicked 
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


def create_account(username, password, confirm_password, error_label): # function to create a new user account, it checks for empty fields, password confirmation, and existing usernames before saving the new user data to the users.json file. I used claude ai to understand how to create the first if/return statement and then adapted this to the rest of the function

    if username == "":                                          # checks if the username field is empty and displays an error message if it is
        error_label.config(text="Please enter a username")
        return

    if password == "":                                          # checks if the password field is empty and displays an error message if it is
        error_label.config(text="Please enter a password")
        return

    if password != confirm_password:                            # checks if the password and confirm password fields match and displays an error message if they don't
        error_label.config(text="Passwords do not match")
        return

    for user in users:
        if user["username"] == username:                        # checks if the username already exists in the users list and displays an error message if it does
            error_label.config(text="Username already exists")
            return

    new_user = {
        "username": username,
        "password": password
    }

    users.append(new_user)

    with open("databases/users.json", "w") as file: # writes the new user data to the users.json file, ensuring that the new account is saved 
        json.dump(users, file, indent=4)

    error_label.config(                        # displays a success message to the user after successfully creating an account
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

        part_frame.bind("<Button-1>", lambda e, p=part: show_part_info(p, project)) #binds a click event to the part frame, so when the user clicks on a part, it will show the part info page for that part

        name_label = tk.Label(
            part_frame,
            text=part["name"],
            font=("Arial", 14, "bold"),
            bg="#eeeeee"
        )
        name_label.pack(side="left", padx=10)
        name_label.bind("<Button-1>", lambda e, p=part: show_part_info(p, project))
        
        
        price_label = tk.Label(
            part_frame,
            text="$" + str(part["price"]),
            bg="#eeeeee"
        )
        price_label.pack(side="left", padx=10)
        price_label.bind("<Button-1>", lambda e, p=part: show_part_info(p, project))


        if compatible:                             #if the part is compatible with the project, display a green "Compatible" label
            compatibility_label = tk.Label(
                part_frame,
                text="Compatible",
                fg="green",
                bg="#eeeeee"
            )
            
        else:
            compatibility_label = tk.Label(       #if not, the pragram will display a red "Not confirmed" label, this is because there are some circumstances where it may be compatible but not confirmed
                part_frame,
                text="Not confirmed",
                fg="red",
                bg="#eeeeee"
            )

        compatibility_label.pack(side="left", padx=10)
        compatibility_label.bind("<Button-1>", lambda e, p=part: show_part_info(p, project))
    make_back_button(lambda: open_project(project))






def get_part_by_id(part_id): #fetches a part from the database based on its id number, claude ai was used to help me understand how the following syntax throughout the part library and project functions could work
    for part in parts:
        if part["id"] == part_id:
            return part
    return None


def save_projects(): #saves the current state of the projects data to the projects.json file, ensuring that any changes made to the projects are maintained across sessions
    with open("databases/projects.json", "w") as file:
        json.dump(projects, file, indent=4)


def add_part_to_project(part, project): #function to add a part to the current project, it ads the part id to the projects parts list and saves the updated projects data to projects.json, then shows the part info page for the added part
    project.setdefault("parts", [])
    if part["id"] not in project["parts"]:
        project["parts"].append(part["id"])
        save_projects()
    show_part_info(part, project)


def remove_part_from_project(part_id, project): #function to remove a part frm the current project, it takes the part id being referenced by the user and the project, then removes the part from the projects parts list and saves the updated projects data to projects.json
    project["parts"].remove(part_id)
    save_projects()
    show_selected_parts(project)


def show_part_info(part, project): # function to display detailed information about a specific part
    clear_window()

    compatible = check_compatibility(part, project) # checks if the part is compatible with the project and stores the result in the variable 'compatible'
    already_added = part["id"] in project.get("parts", [])

    title = tk.Label(content, text=part["name"], font=("Oswald", 24, "bold"), bg="white")
    title.pack(pady=20)

    details_label = tk.Label(
        content,
        text=part.get("category", "Unknown") + " \u2013 $" + str(part["price"]),
        bg="white"
    )
    details_label.pack(pady=5)

    compatibility_label = tk.Label( # label that displays the compatibility status of the part with the current project, changing color based on compatibility
        content,
        text="Compatible" if compatible else "Not confirmed compatible",
        fg="green" if compatible else "red",
        bg="white"
    )
    compatibility_label.pack(pady=10)

    if already_added:
        status_label = tk.Label(content, text="Already in this project", fg="green", bg="white")
        status_label.pack()
    else:
        add_button = tk.Button(
            content,
            text="ADD TO PROJECT",
            command=lambda: add_part_to_project(part, project)
        )
        add_button.pack(pady=10)

    make_back_button(lambda: show_part_library(project))


def show_selected_parts(project): # function to display all parts selected for the current project
    clear_window()

    title = tk.Label(content, text="My Selected Parts", font=("Oswald", 24, "bold"), bg="white")
    title.pack(pady=20)

    total = 0

    for part_id in project.get("parts", []):
        part = get_part_by_id(part_id)
        if part is None:
            continue

        total = total + part["price"]

        part_frame = tk.Frame(content, bg="#eeeeee")
        part_frame.pack(fill="x", padx=50, pady=5)

        label = tk.Label(part_frame, text=part["name"] + " \u2013 $" + str(part["price"]), bg="#eeeeee")
        label.pack(side="left", padx=10)

        remove_button = tk.Button(
            part_frame,
            text="REMOVE",
            command=lambda pid=part_id: remove_part_from_project(pid, project)
        )
        remove_button.pack(side="right", padx=10)

    total_label = tk.Label(content, text="TOTAL: $" + str(total), font=("Arial", 14, "bold"), bg="white")
    total_label.pack(pady=20)

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

    selected_parts_button = tk.Button(
    content,
    text="MY SELECTED PARTS",
    command=lambda: show_selected_parts(project)
)
    selected_parts_button.pack(pady=10)
    
    make_back_button(show_projects)


# GUI Layout section

header = tk.Frame(root, bg="#031E49", height=70)
header.pack(fill=tk.X)
# header grid configuration, very similar to the html website header grid. its split into 3 columns, the first for the logo
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
    text="© 2026 EuroPartPicker. All rights reserved.", #changed to current
    font=("Noto Sans Chakma", 12),
    fg="white",
    bg="#031E49"
)

footer_label.pack(side='right', pady=10)



show_home() # shows the home page when the app is first opened

# Creating the event loop to keep the window visible
root.mainloop()


