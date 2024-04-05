import tkinter as tk
from tkinter import messagebox, Entry
import keyring

# Function to get master password
def get_master_password():
    return keyring.get_password("password_manager", "master_password")

# Function to authenticate the user with the master password
authenticated = False  # Global variable to track authentication status

def authenticate_user():
    global authenticated  # Declare the variable as global
    
    def authenticate():
        global authenticated  # Declare again to ensure modification of the global variable
        master_password = master_password_entry.get()
        if master_password == get_master_password():
            messagebox.showinfo("Success", "Authentication successful.")
            authenticated = True  # Update the global variable
            root.destroy()
        else:
            messagebox.showerror("Error", "Incorrect master password. Please try again.")
    
    root = tk.Tk()
    root.title("Authenticate")
    root.geometry("300x100")
    
    master_password_label = tk.Label(root, text="Master Password:")
    master_password_label.pack()
    master_password_entry = Entry(root, show="*")
    master_password_entry.pack()
    
    authenticate_button = tk.Button(root, text="Authenticate", command=authenticate)
    authenticate_button.pack()
    
    root.mainloop()

    return authenticated  # Return the authentication status

def check_authentication():
    if get_master_password() is None:
        messagebox.showerror("Error", "Master password is not set. Please set the master password.")
        return False
    else:
        authenticated = authenticate_user()
        print(authenticated)  # Add this line for debugging
        return authenticated