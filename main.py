# Creating a simple password manager using python. 

# Importing modules. 
import password_generator
import tkinter as tk
from tkinter import messagebox

# Creating the main application window.
root = tk.Tk()

# Defining window size and adding cusomization. 
root.geometry("800x600")
root.overrideredirect(True)
darkmode = False

# Function to handle settings menu selections.
def settings_menu_selection(option):
    if option == "Import using a .csv file":
        messagebox.showinfo("This option is not implemented yet.")
      
    if option == "Dark Mode":
        if darkmode == False:
          pass
        if darkmode == True:
          pass
    elif option == "Exit":
        root.quit()

# Function to create settings menu
def create_settings_menu(event):
    settings_menu = tk.Menu(root, tearoff=0)
    settings_menu.add_command(label="Import using a .csv file", command=lambda: settings_menu_selection("Import using a .csv file"))
    settings_menu.add_separator()
    settings_menu.add_command(label="Toggle Dark Mode", command=toggle_dark_mode)
    settings_menu.post(event.x_root, event.y_root)
    settings_menu.add_separator()
    settings_menu.add_command(label="Exit", command=lambda: settings_menu_selection("Exit"))
    settings_menu.post(event.x_root, event.y_root)

# Creating widgets.
def create_widgets():
    # Display the title
    title_label = tk.Label(root, text="Password Manager by xobash", font=("Arial", 12), bg="light gray", padx=10, pady=10)
    title_label.grid(row=0, column=0, columnspan=1, sticky="nsew")

    # Left side (Buttons)
    left_frame = tk.Frame(root, width=100, bg="light gray", padx=10, pady=10)
    left_frame.grid(row=1, column=0, sticky="nsew")

    # Middle (Password Display)
    middle_frame = tk.Frame(root, bg="white", padx=10, pady=10)
    middle_frame.grid(row=1, column=1, sticky="nsew")

    # Right side (Output)
    right_frame = tk.Frame(root, bg="light gray", padx=10, pady=10)
    right_frame.grid(row=1, column=2, sticky="nsew")

    # Create buttons
    all_settings_button = tk.Button(left_frame, text="All Settings", bg="white", relief="flat", padx=10, pady=5)
    all_settings_button.pack(fill="x", padx=10, pady=(20, 5))

    favorites_button = tk.Button(left_frame, text="Favorites", bg="white", relief="flat", padx=10, pady=5)
    favorites_button.pack(fill="x", padx=10, pady=5)

    notes_button = tk.Button(left_frame, text="Notes", bg="white", relief="flat", padx=10, pady=5)
    notes_button.pack(fill="x", padx=10, pady=5)

    passwords_button = tk.Button(left_frame, text="Passwords", bg="white", relief="flat", padx=10, pady=5)
    passwords_button.pack(fill="x", padx=10, pady=5)

    tags_button = tk.Button(left_frame, text="Tags", bg="white", relief="flat", padx=10, pady=5)
    tags_button.pack(fill="x", padx=10, pady=5)

    # Search bar
    search_label = tk.Label(middle_frame, text="Search:", font=("Arial", 10), bg="white")
    search_label.grid(row=0, column=0, padx=(10, 5), pady=10)

    search_entry = tk.Entry(middle_frame, width=30, font=("Arial", 10))
    search_entry.grid(row=0, column=1, padx=(0, 10), pady=10)

    # Right side (Output)
    right_frame = tk.Frame(root, bg="light gray", padx=10, pady=10)
    right_frame.grid(row=1, column=2, sticky="nsew")

    # Settings button
    settings_button = tk.Button(root, text="\u2630", font=("Arial", 10), bg="light gray", bd=0)
    settings_button.grid(row=0, column=2, padx=10, pady=10, sticky="ne")
    settings_button.bind("<Button-1>", create_settings_menu)
   
# Configure grid layout to make columns resizable
root.columnconfigure(0, weight=0)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=0)
root.rowconfigure(1, weight=1)

# Create widgets
create_widgets()

root.mainloop()