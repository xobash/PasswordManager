import tkinter as tk
from tkinter import messagebox, simpledialog
import secrets
import hashlib
import keyring

class AuthUser:
    def __init__(self, root):
        self.root = root
        self.root.withdraw()

    def hash_master_password(self, password, salt):
        hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
        return hashed_password

    def generate_salt(self):
        return secrets.token_bytes(16)

    def set_master_password(self):
        while True:
            initial_password = simpledialog.askstring("Set a Master Password", "A Super Safe Master Password:", show="*")
            if initial_password:
                salt = self.generate_salt()
                hashed_password = self.hash_master_password(initial_password, salt)
                keyring.set_password("password_manager", "master_password", hashed_password)
                keyring.set_password("password_manager", "salt", salt)
                return True
            else:
                messagebox.showerror("Error", "Master Password cannot be blank.")
                retry = messagebox.askretrycancel("stop it", "get some help?")
                if not retry:
                    return False

    def prompt_for_master_password(self):
        master_password = keyring.get_password("password_manager", "master_password")
        if master_password:
            while True:
                entered_password = simpledialog.askstring("You Shall Not Pass", "Enter Master Password:", show="*")
                if entered_password:
                    salt = keyring.get_password("password_manager", "salt")
                    if salt:
                        salt = salt.encode()  # Convert salt back to bytes
                        hashed_entered_password = self.hash_master_password(entered_password, salt)
                        if hashed_entered_password == master_password.encode():  # Convert master_password to bytes
                            return True
                        else:
                            messagebox.showerror("Error", "Incorrect master password. Please try again.")
                    else:
                        messagebox.showerror("Error", "Salt not found. Please set the master password.")
                        return False
                else:
                    return False
        else:
            return self.set_master_password()

    def check_authentication(self):
        if not self.prompt_for_master_password():
            self.root.destroy()
            return False
        else:
            return True
