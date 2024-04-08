import tkinter as tk
from tkinter import messagebox, simpledialog
import secrets
import hashlib
import keyring
from password_manager import PasswordManagerApp

class AuthUser:
    def __init__(self, root):
        self.root = root
        self.root.withdraw()

    def hash_master_password(self, password, salt):
        try:
            hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
            return hashed_password
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while hashing the master password: {e}")
            return None

    def generate_salt(self):
        try:
            return secrets.token_bytes(16)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while generating salt: {e}")
            return None

    def set_master_password(self):
        while True:
            initial_password = simpledialog.askstring("Set a Master Password", "A Super Safe Master Password:", show="*")
            if initial_password:
                salt = self.generate_salt()
                if salt:
                    hashed_password = self.hash_master_password(initial_password, salt)
                    if hashed_password:
                        try:
                            keyring.set_password("password_manager", "master_password", hashed_password.hex())
                            keyring.set_password("password_manager", "salt", salt.hex())
                            messagebox.showinfo("kek", "You've Got Mail.")
                            return True
                        except Exception as e:
                            messagebox.showerror("Error", f"An error occurred while setting the master password: {e}")
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                messagebox.showerror("Error", "Master Password cannot be blank.")
                retry = messagebox.askretrycancel("Really?", "Stop it. Do you want to try again?")
                if not retry:
                    return False

def prompt_for_master_password(self):
    try:
        master_password_hash = keyring.get_password("password_manager", "master_password")
        if master_password_hash:
            while True:
                entered_password = simpledialog.askstring("Enter Master Password", "Enter Master Password:", show="*")
                if entered_password:
                    salt = keyring.get_password("password_manager", "salt")
                    if salt:
                        salt = bytes.fromhex(salt)
                        entered_password_hash = self.hash_master_password(entered_password, salt)
                        if entered_password_hash:
                            stored_hash_bytes = bytes.fromhex(master_password_hash)
                            if len(stored_hash_bytes) == len(entered_password_hash) and \
                               hashlib.compare_digest(entered_password_hash, stored_hash_bytes): # hashlib.compare_digest used. This change improves the security of the authentication process by mitigating certain timing attacks.
                                app_root = tk.Toplevel()  # Create a new window for the app
                                app = PasswordManagerApp(app_root)
                                return True
                            else:
                                messagebox.showerror("Error", "Incorrect master password. Please try again.")
                                return False
                        else:
                            return False
                    else:
                        messagebox.showerror("Error", "Salt not found. Please set the master password.")
                        return False
                else:
                    return False
        else:
            return self.set_master_password()
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred during authentication: {e}")
        return False

    def check_authentication(self):
        if not self.prompt_for_master_password():
            self.root.destroy()
            return False
        else:
            try:
                app_root = tk.Toplevel()  # Create a new window for the app
                app = PasswordManagerApp(app_root)
                return True
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred while launching the Password Manager app: {e}")
                return False
