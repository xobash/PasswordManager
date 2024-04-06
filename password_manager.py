import tkinter as tk
from tkinter import Button, Label, messagebox, Entry
import sqlite3
import password_generator as pg
from cryptography.fernet import Fernet
from auth_user import check_authentication

key = None 

# Setting up sqlite3 database
conn = sqlite3.connect('db1.db')
conn.execute('''CREATE TABLE IF NOT EXISTS passwords
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
             website TEXT NOT NULL,
             username TEXT NOT NULL,
             password TEXT NOT NULL);''')
conn.commit()

# Function to generate a random encryption key
def generate_key():
    return Fernet.generate_key()

# Function to encrypt a password using AES encryption
def encrypt_password(password, key):
    fernet = Fernet(key)
    encrypted_password = fernet.encrypt(password.encode())
    return encrypted_password

# Function to decrypt a password using AES encryption
def decrypt_password(encrypted_password, key):
    fernet = Fernet(key)
    decrypted_password = fernet.decrypt(encrypted_password).decode()
    return decrypted_password

# Function to import and export files using .csv format.
def import_from_file():
    messagebox.showinfo("Info", "This feature is still in beta. Please report any bugs.")

def export_to_file():
    messagebox.showinfo("Info", "This feature is still in beta. Please report any bugs.")

def password_generator():
    # Clear the middle column.
    for widget in middle_frame.winfo_children():
        widget.destroy()

    password_generator_label = tk.Label(middle_frame, text="Password Generator by xobash", bg=background_color, fg=foreground_color)
    password_generator_label.grid(row=2, column=0, sticky="e")

    password_label = tk.Label(middle_frame, text="Password:", padx=10, pady=10, bg=background_color, fg=foreground_color)
    password_label.grid(row=4, column=0, sticky="e")
    password_widget = Entry(middle_frame, width=30)
    password_widget.grid(row=4, column=1, padx=10, pady=10)

    # Function to generate a secure password
    def generate_secure_password():
        # Generate a secure password
        generated_password = pg.generate_password()

        # Display the generated password
        password_widget.delete(0, tk.END)
        password_widget.insert(0, generated_password)

    # Function to store the generated password
    def store_generated_password():
        pass

    # Buttons for generating and storing passwords
    generate_button = Button(middle_frame, text="Generate Password", command=generate_secure_password, bg=accent_color, fg=foreground_color)
    generate_button.grid(row=5, column=0, columnspan=2, pady=10)

    store_button = Button(middle_frame, text="Store Password", command=store_generated_password, bg=accent_color, fg=foreground_color)
    store_button.grid(row=6, column=0, columnspan=2, pady=10)

# Check authentication before proceeding
if not check_authentication():
    exit()
else:
    # Creating application window
    root = tk.Tk()
    root.geometry("800x600")
    root.title("Simple Password Manager by xobash")

    # Function to toggle dark mode
    def toggle_dark_mode():
        global darkmode
        darkmode = not darkmode
        update_widgets()

    # Function to update widgets based on dark mode
    def update_widgets():
        global background_color, foreground_color, accent_color
        background_color = "#0d1117" if darkmode else "white"
        foreground_color = "#c9d1d9" if darkmode else "black"
        accent_color = "#21262d" if darkmode else "light gray"
        root.config(bg=background_color)
        title_label.config(bg=background_color, fg=foreground_color)
        left_frame.config(bg=background_color)
        middle_frame.config(bg=background_color)
        right_frame.config(bg=background_color)
        all_settings_button.config(bg=accent_color, fg=foreground_color)
        favorites_button.config(bg=accent_color, fg=foreground_color)
        notes_button.config(bg=accent_color, fg=foreground_color)
        passwords_button.config(bg=accent_color, fg=foreground_color)
        tags_button.config(bg=accent_color, fg=foreground_color)
        password_generator_button.config(bg=accent_color, fg=foreground_color)
        search_label.config(bg=background_color, fg=foreground_color)
        search_entry.config(bg=accent_color, fg=foreground_color)
        settings_button.config(bg=background_color, fg=foreground_color)

    # Function to handle adding a new password entry
    def add_password_entry():
        # Clear the middle column.
        for widget in middle_frame.winfo_children():
            widget.destroy()

        website_label = tk.Label(middle_frame, text="Website:", font=("Arial", 10), padx=10, pady=10, bg=background_color, fg=foreground_color)
        website_label.grid(row=2, column=0, sticky="e")
        website_entry_widget = Entry(middle_frame, width=30)
        website_entry_widget.grid(row=2, column=1, padx=10, pady=10)

        username_label = tk.Label(middle_frame, text="Username:", font=("Arial", 10), padx=10, pady=10, bg=background_color, fg=foreground_color)
        username_label.grid(row=3, column=0, sticky="e")
        username_entry_widget = Entry(middle_frame, width=30)
        username_entry_widget.grid(row=3, column=1, padx=10, pady=10)

        password_label = tk.Label(middle_frame, text="Password:", font=("Arial", 10), padx=10, pady=10, bg=background_color, fg=foreground_color)
        password_label.grid(row=4, column=0, sticky="e")
        password_entry_widget = Entry(middle_frame, width=30, show="*")
        password_entry_widget.grid(row=4, column=1, padx=10, pady=10)

        # Option to use custom encryption key
        custom_key = messagebox.askyesno("Use Custom Key", "Do you want to use your own encryption key? If you choose not to, everything will be encrypted using an autogenerated key.")
        if custom_key:
            key_label = tk.Label(middle_frame, text="Key:", font=("Arial", 10), padx=10, pady=10, bg=background_color, fg=foreground_color)
            key_label.grid(row=5, column=0, sticky="e")
            key_entry = Entry(middle_frame, width=30)
            key_entry.grid(row=5, column=1, padx=10, pady=10)
        else:
            key_entry = None

        # Generate encryption key if not provided by the user
        if custom_key and key_entry:
            key = key_entry.get()
        else:
            key = generate_key()

        # Create and grid store button
        store_button = Button(middle_frame, text="Store Securely using AES", command=lambda: store_password(
            website_entry_widget.get(), username_entry_widget.get(), password_entry_widget.get(), key), bg=accent_color, fg=foreground_color)
        store_button.grid(row=6, column=1, padx=10, pady=10)

    # Function to store a password securely using AES encryption
    def store_password(website, username, password, key):
        # Check if any of the entry boxes are empty
        if not website or not username or not password:
            messagebox.showerror("Error", "Cannot store empty values.")
            return

        # Check if the key is empty, and generate one if needed
        if not key:
            messagebox.showinfo("Encryption Key", "An autogenerated key will be used.")
            key = generate_key()

        encrypted_password = encrypt_password(password, key)

        conn = sqlite3.connect('db1.db')
        c = conn.cursor()
        c.execute("INSERT INTO passwords (website, username, password) VALUES (?, ?, ?)",
                  (website, username, encrypted_password))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Password stored securely using AES encryption.")

    # Function to create settings menu
    def create_settings_menu():
        settings_menu = tk.Menu(root, tearoff=0)
        settings_menu.add_command(label="Import using a .csv file (beta)", command=import_from_file)
        settings_menu.add_command(label="Export to .csv file (beta)", command=export_to_file)
        settings_menu.add_command(label="Toggle Dark Mode", command=toggle_dark_mode)
        settings_menu.add_command(label="Exit", command=root.quit)
        settings_menu.post(settings_button.winfo_rootx(), settings_button.winfo_rooty() + settings_button.winfo_height())  # Adjust menu position

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

    password_generator_button = tk.Button(left_frame, text="Password Generator", padx=1, pady=5, command=password_generator)
    password_generator_button.pack(fill="x", padx=10, pady=5)

    search_label = tk.Label(middle_frame, text="Search:", font=("Arial", 10))
    search_label.grid(row=0, column=0, padx=(10, 5), pady=10)

    search_entry = tk.Entry(middle_frame, width=30, font=("Arial", 10))
    search_entry.grid(row=0, column=1, padx=(0, 10), pady=10)

    add_button = Button(root, text="+", font=("Arial", 10), bd=0, command=add_password_entry)
    add_button.grid(row=0, column=1, padx=10, pady=10, sticky="ne")

    settings_button = tk.Button(root, text="\u2630", font=("Arial", 10), bd=0, command=create_settings_menu)
    settings_button.grid(row=0, column=2, padx=10, pady=10, sticky="ne")

    # Initialize dark mode
    darkmode = True
    update_widgets()

    # Close connection to sqlite3 db
    conn.close()
    root.mainloop()
