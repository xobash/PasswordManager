# Creating a password manager using python. 

# Importing modules. 
import password_generator
import tkinter as tk
from tkinter import Button, messagebox
import sqlite3 # Importing sqlite3

# Setting up sqlite3 database
conn = sqlite3.connect('db1.db')
# cursor = conn.cursor()

# Creating tables for users and passwords
# cursor.execute()

# Commit and close connection
conn.commit()
conn.close()

# Creating the main application window.
root = tk.Tk() # TKKKKK 
root.geometry("800x600")
root.overrideredirect(True)
darkmode = False

# Why i need a global title_label, I will never know.
title_label = None

# Function to toggle dark mode
def toggle_dark_mode():
    global darkmode
    darkmode = not darkmode # CURSED CODE
    print(darkmode) # Debugging
    if darkmode:
        # Enable dark mode
        root.configure(bg="black", fg="white") 
    else:
        # Enable light mode
        root.configure(bg="white", fg="black")  

    # Update the appearance of widgets
    update_widgets()

# Function to update the appearance of widgets
def update_widgets():
    if darkmode:
        # Apply dark mode styles to widgets
        title_label.config(bg="black", fg="white")
    else:
        # Apply light mode styles to widgets
        title_label.config(bg="light gray", fg="black")
        # Additional settings will be implemented later. 

# Creating widgets.
def create_widgets():
    global title_label
    title_label = tk.Label(root, text="Password Manager by xobash", font=("Arial", 12), bg="light gray", padx=10, pady=10)
    title_label.grid(row=0, column=0, columnspan=1, sticky="nsew")

    # Left side (Buttons)
    left_frame = tk.Frame(root, width=100, bg="light gray", padx=10, pady=10)
    left_frame.grid(row=1, column=0, sticky="nsew")

    # Middle (Main Display)
    middle_frame = tk.Frame(root, bg="white", padx=10, pady=10)
    middle_frame.grid(row=1, column=1, sticky="nsew")

    # Right side (Output)
    right_frame = tk.Frame(root, bg="light gray", padx=10, pady=10)
    right_frame.grid(row=1, column=2, sticky="nsew")

    # Creating buttons
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

# Function to handle settings menu selections.
def settings_menu_selection(option):
    if option == "Import using a .csv file":
        messagebox.showinfo("This option is not implemented yet.") 
    if option == "Dark Mode":
        toggle_dark_mode()
    elif option == "Exit":
        root.quit()

# Configure grid layout to make columns resizable
root.columnconfigure(0, weight=0)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=0)
root.rowconfigure(1, weight=1)

# Creating widgets
create_widgets()

# Me RN
root.mainloop()
