# Creating a simple password manager using python and sqlite3.
import password_generator
import tkinter as tk
from tkinter import Button, Label, messagebox, Entry
import sqlite3
import cryptography.fernet
from cryptography.fernet import Fernet

# Setting up sqlite3 database
conn = sqlite3.connect('db1.db')
conn.commit()

# Perform any database setup tasks, such as creating tables or indexes
# cursor = conn.cursor()
# cursor.execute("CREATE TABLE IF NOT EXISTS ...")

# Function to toggle dark mode
def toggle_dark_mode():
    global darkmode
    darkmode = not darkmode # CURSED CODE
    update_widgets()

# Function to update widgets
def update_widgets():
    if darkmode:
        # Dark Mode
        root.config(bg="black")
        title_label.config(bg="black", fg="white")
        left_frame.config(bg="black")
        middle_frame.config(bg="black")
        right_frame.config(bg="black")
        all_settings_button.config(bg="gray", fg="white")
        favorites_button.config(bg="gray", fg="white")
        notes_button.config(bg="gray", fg="white")
        passwords_button.config(bg="gray", fg="white")
        tags_button.config(bg="gray", fg="white")
        search_label.config(bg="black", fg="white")
        search_entry.config(bg="gray", fg="white")
        settings_button.config(bg="black", fg="white")
    else:
        # Light Mode
        root.config(bg="white")
        title_label.config(bg="light gray", fg="black")
        left_frame.config(bg="light gray")
        middle_frame.config(bg="white")
        right_frame.config(bg="light gray")
        all_settings_button.config(bg="white", fg="black")
        favorites_button.config(bg="white", fg="black")
        notes_button.config(bg="white", fg="black")
        passwords_button.config(bg="white", fg="black")
        tags_button.config(bg="white", fg="black")
        search_label.config(bg="white", fg="black")
        search_entry.config(bg="white", fg="black")
        settings_button.config(bg="light gray", fg="black")

# Creating application window
root = tk.Tk()
root.geometry("800x600")
# Removing Title Bar
root.overrideredirect(True)
darkmode = False

# Make columns resizable
root.columnconfigure(0, weight=0)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=0)
root.rowconfigure(1, weight=1)


# Function to handle adding a new password entry
def add_password_entry():
  website_label = tk.Label(middle_frame, text="Website:", font=("Arial", 12), padx=10, pady=10)
  website_label.grid(row=2, column=0, sticky="e")

  website_entry = Entry(middle_frame, width=30)
  website_entry.grid(row=2, column=1, padx=10, pady=10)

  username_label = tk.Label(middle_frame, text="Username:", font=("Arial", 12), padx=10, pady=10)
  username_label.grid(row=3, column=0, sticky="e")

  username_entry = Entry(middle_frame, width=30)
  username_entry.grid(row=3, column=1, padx=10, pady=10)

  password_label = tk.Label(middle_frame, text="Password:", font=("Arial", 12), padx=10, pady=10)
  password_label.grid(row=4, column=0, sticky="e")

  password_entry = Entry(middle_frame, width=30, show="*")
  password_entry.grid(row=4, column=1, padx=10, pady=10)

  store_button = Button(middle_frame, text="Store Securely using AES", command=store_password)
  store_button.grid(row=5, column=1, padx=10, pady=10)

# Display the decryption key
  key_button = Button(middle_frame, text="Display Decryption Key") #, command=display_decryption_key)
  key_button.grid(row=6, column=1, padx=10, pady=10)

 
def store_password(): 
  def generate_key():
    return Fernet.generate_key()
    
  def encrypt_password(password, key):
    fernet = Fernet(key)
    encrypted_password = fernet.encrypt(password.encode())
    return encrypted_password

    # Open connection to SQLite database
    conn = sqlite3.connect('db1.db')
    c = conn.cursor()

    # Generate encryption key
    key = generate_key()

    # Get website, username, and password from entry fields
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    # Encrypt password
    encrypted_password = encrypt_password(password, key)

    # Store encrypted password in database
    c.execute("INSERT INTO passwords (website, username, password) VALUES (?, ?, ?)", (website, username, encrypted_password))

    # Commit changes and close connection
    conn.commit()
    conn.close()

    messagebox.showinfo("Success", "Password stored securely using AES encryption.")

  def decrypt_password(encrypted_password, key):
    fernet = Fernet(key)
    decrypted_password = fernet.decrypt(encrypted_password).decode()
    return decrypted_password

  def display_decryption_key():
    key = generate_key()
    messagebox.showinfo("Decryption Key", f"Your decryption key: {key.decode()}")


# Creating widgets
title_label = tk.Label(root, text="Simple Password Manager by xobash", font=("Arial", 12), padx=10, pady=10)
title_label.grid(row=0, column=0, columnspan=1, sticky="nsew")

left_frame = tk.Frame(root, width=100, padx=10, pady=10)
left_frame.grid(row=1, column=0, sticky="nsew")

middle_frame = tk.Frame(root, padx=10, pady=10)
middle_frame.grid(row=1, column=1, sticky="nsew")

right_frame = tk.Frame(root, padx=10, pady=10)
right_frame.grid(row=1, column=2, sticky="nsew")

all_settings_button = tk.Button(left_frame, text="All Settings", padx=10, pady=5)
all_settings_button.pack(fill="x", padx=10, pady=(20, 5))

favorites_button = tk.Button(left_frame, text="Favorites (beta)", padx=10, pady=5)
favorites_button.pack(fill="x", padx=10, pady=5)

notes_button = tk.Button(left_frame, text="Notes (beta)", padx=10, pady=5)
notes_button.pack(fill="x", padx=10, pady=5)

passwords_button = tk.Button(left_frame, text="Passwords (beta)", padx=10, pady=5)
passwords_button.pack(fill="x", padx=10, pady=5)

tags_button = tk.Button(left_frame, text="Tags", padx=10, pady=5)
tags_button.pack(fill="x", padx=10, pady=5)

tags_button = tk.Button(left_frame, text="Password Generator", padx=1, pady=5)
tags_button.pack(fill="x", padx=10, pady=5)

search_label = tk.Label(middle_frame, text="Search:", font=("Arial", 10))
search_label.grid(row=0, column=0, padx=(10, 5), pady=10)

search_entry = tk.Entry(middle_frame, width=30, font=("Arial", 10))
search_entry.grid(row=0, column=1, padx=(0, 10), pady=10)

# add_password_entry function called when clicked
add_button = Button(root, text="+", font=("Arial", 10), bd=0, command=add_password_entry)
add_button.grid(row=0, column=1, padx=10, pady=10, sticky="ne")

settings_button = tk.Button(root, text="\u2630", font=("Arial", 10), bd=0)
settings_button.grid(row=0, column=2, padx=10, pady=10, sticky="ne")
settings_button.bind("<Button-1>", lambda event: create_settings_menu(event))


def create_settings_menu(event):
    settings_menu = tk.Menu(root, tearoff=0)
    settings_menu.add_command(label="Import using a .csv file (beta)") # Working on this
    settings_menu.add_command(label="Export to .csv file (beta)") # Working on this
    settings_menu.add_command(label="Toggle Dark Mode", command=toggle_dark_mode)
    settings_menu.add_command(label="Exit", command=root.quit)
    settings_menu.post(event.x_root, event.y_root)

# Create widgets initially
update_widgets()

# Close connection to sqlite3 db
conn.close()
root.mainloop()
