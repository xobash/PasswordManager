import tkinter as tk
from tkinter import Button, Label, messagebox, Entry, Menu
import sqlite3
import password_generator as pg
from cryptography.fernet import Fernet # Work in progress.
import auth_user
from auth_user import check_authentication

class PasswordManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("800x600")
        self.root.title("Simple Password Manager by xobash")
        self.dark_mode = True  # Initialize dark_mode globally in the PasswordManagerApp class.
        self.create_widgets()

        # Check authentication before creating widgets. God help me.
        authenticate = auth_user.check_authentication(self.create_widgets)
        authenticate()

    # Most of the following is still a work in progress. This is supposed to securely store the passwords in the db using AES encryption.
    def generate_key(self):
        return Fernet.generate_key()

    def encrypt_password(self, password, key):
        fernet = Fernet(key)
        encrypted_password = fernet.encrypt(password.encode())
        return encrypted_password

    def decrypt_password(self, encrypted_password, key):
        fernet = Fernet(key)
        decrypted_password = fernet.decrypt(encrypted_password).decode()
        return decrypted_password

    def import_from_file(self):
        messagebox.showinfo("Info", "This feature is still in beta. Please report any bugs.")

    def export_to_file(self):
        messagebox.showinfo("Info", "This feature is still in beta. Please report any bugs.")

    # Meridia will be blown up - John Helldiver
    def search(self, event=None):
        # Get the search query from the search bar
        search_query = self.search_entry.get()

        # Perform the search query on the database
        conn = sqlite3.connect('db1.db')
        c = conn.cursor()
        c.execute("SELECT * FROM passwords WHERE website LIKE ?", ('%' + search_query + '%',))
        search_results = c.fetchall()
        conn.close()

        # Clear the previous search results
        for widget in self.middle_frame.winfo_children():
            widget.destroy()

        # Display the search results
        for idx, result in enumerate(search_results):
            # Display each search result in the middle frame.
            result_label = tk.Label(self.middle_frame, text=result, font=("Arial", 10))
            result_label.grid(row=idx + 1, column=0, padx=10, pady=5)

    def create_widgets(self):
        self.title_label = Label(self.root, text="Simple Password Manager by xobash", font=("Arial", 12), padx=10, pady=10)
        self.title_label.grid(row=0, column=0, columnspan=1, sticky="nsew")
        self.left_frame = tk.Frame(self.root, width=100, padx=10, pady=10)
        self.left_frame.grid(row=1, column=0, sticky="nsew")
        self.middle_frame = tk.Frame(self.root, padx=10, pady=10)
        self.middle_frame.grid(row=1, column=1, sticky="nsew")
        self.right_frame = tk.Frame(self.root, padx=10, pady=10)
        self.right_frame.grid(row=1, column=2, sticky="nsew")
        self.all_settings_button = tk.Button(self.left_frame, text="All Settings", padx=10, pady=5)
        self.all_settings_button.pack(fill="x", padx=10, pady=(20, 5))
        self.favorites_button = tk.Button(self.left_frame, text="Favorites (beta)", padx=10, pady=5)
        self.favorites_button.pack(fill="x", padx=10, pady=5)
        self.notes_button = tk.Button(self.left_frame, text="Notes (beta)", padx=10, pady=5)
        self.notes_button.pack(fill="x", padx=10, pady=5)
        self.passwords_button = tk.Button(self.left_frame, text="Passwords (beta)", padx=10, pady=5)
        self.passwords_button.pack(fill="x", padx=10, pady=5)
        self.tags_button = tk.Button(self.left_frame, text="Tags", padx=10, pady=5)
        self.tags_button.pack(fill="x", padx=10, pady=5)
        self.password_generator_button = tk.Button(self.left_frame, text="Password Generator", padx=1, pady=5, command=self.password_generator)
        self.password_generator_button.pack(fill="x", padx=10, pady=5)
        self.create_search_label()
        self.add_button = Button(self.root, text="+", font=("Arial", 10), bd=0, command=self.add_password_entry)
        self.add_button.grid(row=0, column=1, padx=10, pady=10, sticky="ne")
        self.settings_button = tk.Button(self.root, text="\u2630", font=("Arial", 10), bd=0, command=self.create_settings_menu)
        self.settings_button.grid(row=0, column=2, padx=10, pady=10, sticky="ne")
        self.update_widgets()  # Call update_widgets initially

    def create_search_label(self):
        background_color = "#0d1117" if self.dark_mode else "white"
        foreground_color = "#c9d1d9" if self.dark_mode else "black"
        self.search_label_widget = tk.Label(self.middle_frame, text="Search:", font=("Arial", 10), bg=background_color, fg=foreground_color)
        self.search_label_widget.grid(row=0, column=0, padx=(10, 5), pady=10)

        # Entry widget for search
        self.search_entry = tk.Entry(self.middle_frame, width=30, font=("Arial", 10))
        self.search_entry.grid(row=0, column=1, padx=(0, 10), pady=10)
        self.search_entry.bind("<Return>", self.search)  # Bind Enter key to self.search 

    # Moving up in the world :)
    def password_generator(self):
        middle_frame = self.middle_frame
        background_color = "#0d1117" if self.dark_mode else "white"
        foreground_color = "#c9d1d9" if self.dark_mode else "black"
        accent_color = "#21262d" if self.dark_mode else "light gray"

        # Clear the middle column.
        for widget in middle_frame.winfo_children():
            widget.destroy()

        password_generator_label = Label(middle_frame, text="Password Generator by xobash", bg=background_color, fg=foreground_color)
        password_generator_label.grid(row=2, column=0, sticky="e")

        password_label = Label(middle_frame, text="Password:", padx=10, pady=10, bg=background_color, fg=foreground_color)
        password_label.grid(row=4, column=0, sticky="e")
        password_widget = Entry(middle_frame, width=30)
        password_widget.grid(row=4, column=1, padx=10, pady=10)

        # Function to generate a secure password
        def generate_secure_password():
            generated_password = pg.generate_password() # Generate a secure password

            # Display the generated password
            password_widget.delete(0, tk.END)
            password_widget.insert(0, generated_password)

        # Function to store the generated password
        def store_generated_password():
            pass # WIP

        # Buttons for generating and storing passwords
        generate_button = Button(middle_frame, text="Generate Password", command=generate_secure_password, bg=accent_color, fg=foreground_color)
        generate_button.grid(row=5, column=0, columnspan=2, pady=10)

        store_button = Button(middle_frame, text="Store Password", command=store_generated_password, bg=accent_color, fg=foreground_color)
        store_button.grid(row=6, column=0, columnspan=2, pady=10)

    def toggle_dark_mode(self):
        self.dark_mode = not self.dark_mode # LEVEL UP
        self.update_widgets()

    def update_widgets(self):
        # 'Github Dark'
        background_color = "#0d1117" if self.dark_mode else "white" # Calling self.dark_mode to check dark_mode
        foreground_color = "#c9d1d9" if self.dark_mode else "black"
        accent_color = "#21262d" if self.dark_mode else "light gray"

        self.root.config(bg=background_color)
        self.title_label.config(bg=background_color, fg=foreground_color)
        self.left_frame.config(bg=background_color)
        self.middle_frame.config(bg=background_color)
        self.right_frame.config(bg=background_color)
        self.all_settings_button.config(bg=accent_color, fg=foreground_color)
        self.favorites_button.config(bg=accent_color, fg=foreground_color)
        self.notes_button.config(bg=accent_color, fg=foreground_color)
        self.passwords_button.config(bg=accent_color, fg=foreground_color)
        self.tags_button.config(bg=accent_color, fg=foreground_color)
        self.password_generator_button.config(bg=accent_color, fg=foreground_color)
        self.search_label_widget.config(bg=background_color, fg=foreground_color)
        self.search_entry.config(bg=accent_color, fg=foreground_color)
        self.settings_button.config(bg=background_color, fg=foreground_color)

    def add_password_entry(self):
        middle_frame = self.middle_frame
        background_color = "#0d1117" if self.dark_mode else "white"
        foreground_color = "#c9d1d9" if self.dark_mode else "black"
        accent_color = "#21262d" if self.dark_mode else "light gray"

        # Clear the middle column.
        for widget in middle_frame.winfo_children(): # BURN THE CHILDREN
            widget.destroy()

        website_label = Label(middle_frame, text="Website:", font=("Arial", 10), padx=10, pady=10, bg=background_color, fg=foreground_color)
        website_label.grid(row=2, column=0, sticky="e")
        website_entry_widget = Entry(middle_frame, width=30)
        website_entry_widget.grid(row=2, column=1, padx=10, pady=10)

        username_label = Label(middle_frame, text="Username:", font=("Arial", 10), padx=10, pady=10, bg=background_color, fg=foreground_color)
        username_label.grid(row=3, column=0, sticky="e")
        username_entry_widget = Entry(middle_frame, width=30)
        username_entry_widget.grid(row=3, column=1, padx=10, pady=10)

        password_label = Label(middle_frame, text="Password:", font=("Arial", 10), padx=10, pady=10, bg=background_color, fg=foreground_color)
        password_label.grid(row=4, column=0, sticky="e")
        password_entry_widget = Entry(middle_frame, width=30, show="*")
        password_entry_widget.grid(row=4, column=1, padx=10, pady=10)

        # Option to use custom encryption key
        custom_key = messagebox.askyesno("Use Custom Key", "Do you want to use your own encryption key? If you choose not to, everything will be encrypted using an autogenerated key.")
        if custom_key:
            key_label = Label(middle_frame, text="Key:", font=("Arial", 10), padx=10, pady=10, bg=background_color, fg=foreground_color)
            key_label.grid(row=5, column=0, sticky="e")
            key_entry = Entry(middle_frame, width=30)
            key_entry.grid(row=5, column=1, padx=10, pady=10)
        else:
            key_entry = None

        # Generate encryption key if not provided by the user - not sure if this will work when decrypting. 
        if custom_key and key_entry:
            key = key_entry.get()
        else:
            key = self.generate_key()

        # Create and grid store button
        store_button = Button(middle_frame, text="Store Securely using AES", command=lambda: self.store_password(
            website_entry_widget.get(), username_entry_widget.get(), password_entry_widget.get(), key), bg=accent_color, fg=foreground_color)
        store_button.grid(row=6, column=1, padx=10, pady=10)

    def store_password(self, website, username, password, key):
        background_color = "#0d1117" if self.dark_mode else "white"
        foreground_color = "#c9d1d9" if self.dark_mode else "black"

        # Check if any of the entry boxes are empty
        if not website or not username or not password:
            messagebox.showerror("kek", "Cannot store empty values.")
            return

        # Check if the key is empty, and generate one if needed
        if not key:
            messagebox.showinfo("Encryption Key", "An autogenerated key will be used.") # Again, not sure if this will even work.
            key = self.generate_key()

        encrypted_password = self.encrypt_password(password, key) # tee hee

        conn = sqlite3.connect('db1.db')
        c = conn.cursor()
        c.execute("INSERT INTO passwords (website, username, password) VALUES (?, ?, ?)",
                (website, username, encrypted_password))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Password stored securely using AES encryption.")

    def create_settings_menu(self):
        settings_menu = Menu(self.root, tearoff=0)
        settings_menu.add_command(label="Import using a .csv file (beta)", command=self.import_from_file)
        settings_menu.add_command(label="Export to .csv file (beta)", command=self.export_to_file)
        settings_menu.add_command(label="Toggle Dark Mode", command=self.toggle_dark_mode)
        settings_menu.add_command(label="Exit", command=self.root.quit)
        settings_menu.post(self.settings_button.winfo_rootx(), self.settings_button.winfo_rooty() + self.settings_button.winfo_height())  # Adjust menu position

def main():
    # Setting up sqlite3 database
    conn = sqlite3.connect('db1.db')
    conn.execute('''CREATE TABLE IF NOT EXISTS passwords
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 website TEXT NOT NULL,
                 username TEXT NOT NULL,
                 password TEXT NOT NULL);''')
    conn.commit()

    root = tk.Tk()  # Create the root window
    # Pass the root window to the check_authentication function
    if auth_user.check_authentication(root):
        app = PasswordManagerApp(root)
        root.mainloop()
    else:
        messagebox.showerror("kek", "Authentication failed. Exiting...")
    
    # Close connection to sqlite3 db
    conn.close()

if __name__ == "__main__":
    main()
