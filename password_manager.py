import tkinter 
from tkinter import Button, Label, messagebox, Entry, Menu, Frame, END, TclError
import sqlite3
import password_generator as pg
from cryptography.fernet import Fernet # Work in progress.

class PasswordManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.overrideredirect(True) 
        self.root.geometry("800x600")
        self.root.title("Simple Password Manager by xobash") # Yours truly :)
        self.dark_mode = True  # Initialize dark_mode globally in the PasswordManagerApp class.

        # Variables to store widget references
        self.title_label = None
        self.left_frame = None
        self.middle_frame = None
        self.right_frame = None
        self.all_settings_button = None
        self.add_button = None
        self.search_label_widget = None
        self.search_entry = None
        self.password_generator_button = None
        self.settings_button = None
        self.password_widget = None
        self.generate_button = None
        self.store_button = None
        self.website_label = None
        self.username_label = None
        self.password_label = None
        self.website_entry_widget = None
        self.username_entry_widget = None
        self.password_entry_widget = None
        self.key_label = None
        self.key_entry = None

        self.accent_color = "#21262d" if self.dark_mode else "light gray"
        self.background_color = "#0d1117" if self.dark_mode else "white"
        self.foreground_color = "#c9d1d9" if self.dark_mode else "black"

        # Bind MB1 to start_move method. 
        self.root.bind("<ButtonPress-1>", self.start_move)
        self.root.bind("<B1-Motion>", self.on_move)
        self.root.bind("<ButtonRelease-1>", self.stop_move)
        self.offset_x = 0
        self.offset_y = 0

        # How were they being created in the first place....?
        try:
            self.create_widgets()
            self.update_widgets()
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
            
    def __del__(self):
        if self.conn:
            self.conn.close()

    def update_widgets(self):  
        try:
            # Configure the root, this will not be changing.
            self.accent_color = "#21262d" if self.dark_mode else "light gray"
            self.background_color = "#0d1117" if self.dark_mode else "white"
            self.foreground_color = "#c9d1d9" if self.dark_mode else "black"
            self.accent_color = "#21262d" if self.dark_mode else "light gray"
            self.root.config(background=self.background_color)

            # List of tuples containing widget references and their configuration options
            widgets = [
                (self.add_button, {"background": self.background_color, "foreground": self.foreground_color}),
                (self.website_label, {"background": self.background_color, "foreground": self.foreground_color}),
                (self.username_label, {"background": self.background_color, "foreground": self.foreground_color}),
                (self.password_label, {"background": self.background_color, "foreground": self.foreground_color}),
                (self.website_entry_widget, {"background": self.background_color, "foreground": self.foreground_color}),
                (self.username_entry_widget, {"background": self.background_color, "foreground": self.foreground_color}),
                (self.password_entry_widget, {"background": self.background_color, "foreground": self.foreground_color}),
                (self.key_label, {"background": self.background_color, "foreground": self.foreground_color}),
                (self.key_entry, {"background": self.background_color, "foreground": self.foreground_color}),
                (self.store_button, {"background": self.accent_color, "foreground": self.foreground_color}),  
                (self.password_generator_button, {"background": self.accent_color, "foreground": self.foreground_color}),  
                (self.password_widget, {"background": self.background_color, "foreground": self.foreground_color}),
                (self.generate_button, {"background": self.accent_color, "foreground": self.foreground_color}),  
                (self.search_label_widget, {"background": self.background_color, "foreground": self.foreground_color}),
                (self.search_entry, {"background": self.background_color, "foreground": self.foreground_color}),
                (self.all_settings_button, {"background": self.background_color, "foreground": self.foreground_color}),
                (self.settings_button, {"background": self.background_color, "foreground": self.foreground_color}),
                (self.left_frame, {"background": self.background_color, "foreground": self.foreground_color}),
                (self.middle_frame, {"background": self.background_color, "foreground": self.foreground_color}),
                (self.right_frame, {"background": self.background_color, "foreground": self.foreground_color}),
            ]
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    # Pls no buffer overflow <3
    def create_widgets(self):

        self.accent_color = "#21262d" if self.dark_mode else "light gray"
        self.background_color = "#0d1117" if self.dark_mode else "white"
        self.foreground_color = "#c9d1d9" if self.dark_mode else "black"
        self.accent_color = "#21262d" if self.dark_mode else "light gray"

        try:
            # Define accent_color within create_widgets method
            self.title_label = Label(self.root, text="Simple Password Manager by xobash", font=("Arial", 12), padx=10, pady=10, background=self.background_color, foreground=self.foreground_color)
            self.title_label.grid(row=0, column=0, columnspan=1, sticky="nsew")
            self.left_frame = Frame(self.root, width=100, padx=10, pady=10, background=self.background_color)
            self.left_frame.grid(row=1, column=0, sticky="nsew")
            self.middle_frame = Frame(self.root, padx=10, pady=10, background=self.background_color)
            self.middle_frame.grid(row=1, column=1, sticky="nsew")
            self.right_frame = Frame(self.root, padx=10, pady=10, background=self.background_color)
            self.right_frame.grid(row=1, column=2, sticky="nsew")
            self.all_settings_button = Button(self.left_frame, text="All Settings", padx=10, pady=5, background=self.accent_color)
            self.all_settings_button.pack(fill="x", padx=10, pady=(20, 5))
            self.add_button = Button(self.root, text="+", font=("Arial", 10), bd=0, command=self.add_password_entry, background=self.background_color, foreground=self.foreground_color)
            self.add_button.grid(row=0, column=1, padx=10, pady=10, sticky="ne") 
                          
            # Create search label after middle_frame is created
            self.create_search_label()
            self.favorites_button = Button(self.left_frame, text="Favorites (beta)", padx=10, pady=5, background=self.accent_color, foreground=self.foreground_color)
            self.favorites_button.pack(fill="x", padx=10, pady=5)
            self.notes_button = Button(self.left_frame, text="Notes (beta)", padx=10, pady=5, background=self.accent_color, foreground=self.foreground_color)
            self.notes_button.pack(fill="x", padx=10, pady=5)
            self.passwords_button = Button(self.left_frame, text="Passwords (beta)", padx=10, pady=5, background=self.accent_color, foreground=self.foreground_color)
            self.passwords_button.pack(fill="x", padx=10, pady=5)
            self.tags_button = Button(self.left_frame, text="Tags", padx=10, pady=5, background=self.accent_color, foreground=self.foreground_color)
            self.tags_button.pack(fill="x", padx=10, pady=5)
            self.password_generator_button = Button(self.left_frame, text="Password Generator", padx=1, pady=5, command=self.password_generator, background=self.accent_color, foreground=self.foreground_color)
            self.password_generator_button.pack(fill="x", padx=10, pady=5)
            self.settings_button = Button(self.root, text="\u2630", font=("Arial", 10), bd=0, command=self.create_settings_menu, background=self.background_color, foreground=self.foreground_color)
            self.settings_button.grid(row=0, column=2, padx=10, pady=10, sticky="ne")
            self.update_widgets()

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def start_move(self, event):
        # Record the initial click position
        self.offset_x = event.x_root
        self.offset_y = event.y_root

    def on_move(self, event):
        # Calculate the new position of the window relative to the initial click position and offset
        new_x = self.root.winfo_pointerx() - self.offset_x
        new_y = self.root.winfo_pointery() - self.offset_y

        # Get the screen width and height
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Limit the movement to keep the window within the screen boundaries
        if 0 <= new_x <= screen_width and 0 <= new_y <= screen_height:
            self.root.geometry(f"+{new_x}+{new_y}")

    def stop_move(self, event):
        self.offset_x = 0
        self.offset_y = 0
    # Most of the following is still a work in progress. This is supposed to securely store the passwords in the db using AES encryption.
    # I'm not sure if I will be able to fetch the passwords as cleartext within the program. We'll see.
    def generate_key(self):
        try:
            # This will autogenerate a key for the user to encrypt their data.
            return Fernet.generate_key()
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def encrypt_password(self, password, key):
        try:
            # This will use that key to encrypt it.
            fernet = Fernet(key)
            encrypted_password = fernet.encrypt(password.encode())
            return encrypted_password
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def decrypt_password(self, encrypted_password, key):
        try:
            # Placeholder logic, I am not sure if this will work yet.
            fernet = Fernet(key)
            decrypted_password = fernet.decrypt(encrypted_password).decode()
            return decrypted_password
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def import_from_file(self):
        try:
            with open('filename.csv', 'r') as file:
                # Read data from the file and process it
                pass  # Placeholder for file reading logic
            messagebox.showinfo("Info", "Import successful.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def export_to_file(self):
        try:
            with open('filename.csv', 'w') as file:
                # Write data to the file
                pass  # Placeholder for file writing logic
            messagebox.showinfo("Info", "Export successful.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
    
    def search(self, event=None):
        conn = None
        # Check if the entry exists first. Pass for now.....
        if search_exists():
            pass
        try:
            search_query = self.search_entry.get()

            conn = sqlite3.connect('db1.db')
            c = conn.cursor()
            c.execute("SELECT * FROM passwords WHERE website LIKE ?", ('%' + search_query + '%',))
            search_results = c.fetchall()
            conn.close()
            
            # Destroy the widgets in the middle frame. 
            if widget not in [self.search_label_widget, self.search_entry]:
                widget.destroy()

            for idx, result in enumerate(search_results):
                result_label = Label(self.middle_frame, text=result, font=("Arial", 10))
                result_label.grid(row=idx + 1, column=0, padx=10, pady=5)
        except Exception as e:
            # Error handling.
            messagebox.showerror("Error", f"An error occurred: {e}")
        finally:
            # Close database connection
            if conn:
                conn.close()

    # Meridia will be blown up - John Helldiver
    # edit... it was. 
    def create_search_label(self): # No need for error handling here.
            self.background_color = "#0d1117" if self.dark_mode else "white"
            self.foreground_color = "#c9d1d9" if self.dark_mode else "black"
            self.search_label_widget = Label(self.middle_frame, text="Search:", font=("Arial", 10), background=self.background_color, foreground=self.foreground_color)
            self.search_label_widget.grid(row=0, column=0, padx=(10, 5), pady=10)

            # Entry widget for search
            self.search_entry = Entry(self.middle_frame, width=30, font=("Arial", 10))
            self.search_entry.grid(row=0, column=1, padx=(0, 10), pady=10)
            self.search_entry.bind("<Return>", self.search)  # Bind Enter key to self.search 
            self.update_widgets()
            
    # Moving up in the world :)
    def password_generator(self):
        try:
            # Clear the middle column.
            for widget in self.middle_frame.winfo_children(): 
                if widget not in [self.search_label_widget, self.search_entry]:
                    widget.destroy()

            self.password_generator_label = Label(self.middle_frame, text="Password Generator by xobash", background=self.background_color, foreground=self.foreground_color)
            self.password_generator_label.grid(row=2, column=0, sticky="e")

            self.password_label = Label(self.middle_frame, text="Password:", padx=10, pady=10, background=self.background_color, foreground=self.foreground_color)
            self.password_label.grid(row=4, column=0, sticky="e")
            self.password_widget = Entry(self.middle_frame, width=30)
            self.password_widget.grid(row=4, column=1, padx=10, pady=10)
            self.update_widgets()

            # Function to generate a secure password
            def generate_secure_password():
                try:
                    generated_password = pg.generate_password() # Generate a secure password, will eventually add customization.

                    # Display the generated password
                    self.password_widget.delete(0, tkinter.END)
                    self.password_widget.insert(0, generated_password)
                    self.update_widgets()
                except Exception as e:
                    # Error handling.
                    messagebox.showerror("Error", f"An error occurred: {e}") 

            # Function to store the generated password
            def store_generated_password():
                try:
                    conn = sqlite3.connect('db1.db') # Placeholder logic, WIP.
                except Exception as e:
                    messagebox.showerror("Error", f"An error occurred: {e}") 

                finally:
                    # Close database connection
                    if conn:
                        pass
                        # conn.close()
    
            # Buttons for generating and storing passwords
            self.generate_button = Button(self.middle_frame, text="Generate Password", command=generate_secure_password, background=self.accent_color, foreground=self.foreground_color)
            self.generate_button.grid(row=5, column=0, columnspan=2, pady=10)

            self.store_button = Button(self.middle_frame, text="Store Password", command=store_generated_password, background=self.accent_color, foreground=self.foreground_color)
            self.store_button.grid(row=6, column=0, columnspan=2, pady=10)
            self.update_widgets()
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def toggle_dark_mode(self):
        try:
            self.dark_mode = not self.dark_mode # LEVEL UP
            self.background_color = "#0d1117" if self.dark_mode else "white"
            self.foreground_color = "#c9d1d9" if self.dark_mode else "black"
            self.update_widgets()
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}") 

    def add_password_entry(self):
        try:
            for widget in self.middle_frame.winfo_children():  # BURN THE CHILDREN
                if widget not in [self.search_label_widget, self.search_entry]:
                    widget.destroy()

            # Check if website entry widget exists before accessing it.
            if not hasattr(self, 'website_entry_widget'):
                self.website_label = Label(self.middle_frame, text="Website:", font=("Arial", 10), padx=10, pady=10,background=self.background_color, foreground=self.foreground_color)
                self.website_label.grid(row=2, column=0, sticky="e")
                self.website_entry_widget = Entry(self.middle_frame, width=30)
                self.website_entry_widget.grid(row=2, column=1, padx=10, pady=10)

            # Check if username entry widget exists before accessing it.
            if not hasattr(self, 'username_entry_widget'):
                self.username_label = Label(self.middle_frame, text="Username:", font=("Arial", 10), padx=10, pady=10,background=self.background_color, foreground=self.foreground_color)
                self.username_label.grid(row=3, column=0, sticky="e")
                self.username_entry_widget = Entry(self.middle_frame, width=30)
                self.username_entry_widget.grid(row=3, column=1, padx=10, pady=10)

            # Check if password entry widget exists before accessing it.
            if not hasattr(self, 'password_entry_widget'):
                self.password_label = Label(self.middle_frame, text="Password:", font=("Arial", 10), padx=10, pady=10,background=self.background_color, foreground=self.foreground_color)
                self.password_label.grid(row=4, column=0, sticky="e")
                self.password_entry_widget = Entry(self.middle_frame, width=30, show="*")
                self.password_entry_widget.grid(row=4, column=1, padx=10, pady=10)

            # Option to use custom encryption key
            custom_key = messagebox.askyesno("Use Custom Key","Do you want to use your own encryption key? If you choose not to, everything will be encrypted using an autogenerated key. This is not recommended and can lead to data loss.")
            if custom_key:
                if not hasattr(self, 'key_entry'):
                    self.key_label = Label(self.middle_frame, text="Key:", font=("Arial", 10), padx=10, pady=10,background=self.background_color, foreground=self.foreground_color)
                    self.key_label.grid(row=5, column=0, sticky="e")
                    self.key_entry = Entry(self.middle_frame, width=30)
                    self.key_entry.grid(row=5, column=1, padx=10, pady=10)
            else:
                self.key_entry = None  # custom encryption key was not used.

            # Generate encryption key if not provided by the user - not sure if this will work when decrypting.
            if not custom_key:
                key = self.generate_key()  # Generate key only if not using a custom key
                if key is None:
                    messagebox.showerror("Error", "Failed to generate encryption key.")
                    return
            else:
                key = self.key_entry.get() if self.key_entry else None  # Retrieve the custom key from the entry widget if exists

            # Create and grid store button
            if not hasattr(self, 'store_button'):
                self.store_button = Button(self.middle_frame, text="Store Securely using AES",command=lambda: self.store_password(self.website_entry_widget.get(), self.username_entry_widget.get(),self.password_entry_widget.get(), key), background=self.accent_color,foreground=self.foreground_color)
                self.store_button.grid(row=6, column=1, padx=10, pady=10)
                self.update_widgets()

        except Exception as e:
            # Error handling.
            messagebox.showerror("Error", f"An error occurred: {e}")


    # Store password securely in the database
    def store_password(self, website, username, password, key=None):
        try:
            self.background_color = "#0d1117" if self.dark_mode else "white"
            self.foreground_color = "#c9d1d9" if self.dark_mode else "black"

            if not website or not username or not password:
                messagebox.showerror("Error", "Cannot store empty values.")
                return

            if not key:
                messagebox.showinfo("Encryption Key", "An autogenerated key will be used.")
                key = self.generate_key()

            encrypted_password = self.encrypt_password(password, key)

            try:
                # Trying connection to db.
                conn = sqlite3.connect('db1.db')
                c = conn.cursor()
                c.execute("INSERT INTO passwords (website, username, password) VALUES (?, ?, ?)",
                      (website, username, encrypted_password))
                conn.commit() # Commiting changes.
                messagebox.showinfo("Success", "Password stored securely using AES encryption.")
            except sqlite3.Error as e:
                conn.rollback()
                messagebox.showerror("Database Error", f"Failed to store password: {e}")
            finally:
                # Close connection to db.
                conn.close()
        except Exception as e:
            # Error handling.
            messagebox.showerror("Error", f"An error occurred: {e}")

    def create_settings_menu(self):
        try:
            settings_menu = Menu(self.root, tearoff=0)
            settings_menu.add_command(label="Import using a .csv file (beta)", 
                                                            command=self.import_from_file)
            settings_menu.add_command(label="Export to .csv file (beta)", command=self.export_to_file)
            settings_menu.add_command(label="Toggle Dark Mode", command=self.toggle_dark_mode)
            settings_menu.add_command(label="Exit", command=self.root.quit)
            settings_menu.post(self.settings_button.winfo_rootx(), self.settings_button.winfo_rooty() + self.settings_button.winfo_height())  # Adjust menu position
            self.update_widgets()

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
            
# This method will call the PasswordManagerApp class upon authentication.             
def main():
    try:
        import sqlite3
        from auth_user import AuthUser  # Import logic here to avoid circular import.
        
        # Create database connection
        conn = sqlite3.connect('db1.db')
        conn.execute('''CREATE TABLE IF NOT EXISTS passwords
                     (id INTEGER PRIMARY KEY AUTOINCREMENT,
                     website TEXT NOT NULL,
                     username TEXT NOT NULL,
                     password TEXT NOT NULL);''')

        root = tkinter.Tk()
        auth_user = AuthUser(root)  # Initialize AuthUser instance
        if auth_user.check_authentication():
            app = PasswordManagerApp(root)
            app.root.mainloop()
        else:
            root.destroy()  # if not check_authentication, root.destroy.

    except sqlite3.Error as sqlite_error:
        messagebox.showerror("Database Error", f"SQLite error: {sqlite_error}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    main()
