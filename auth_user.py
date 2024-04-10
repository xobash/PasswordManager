# AuthUser class with improvements and fixes
import tkinter as tk
from tkinter import messagebox, simpledialog
import secrets
import hashlib
import keyring
from password_manager import PasswordManagerApp

class AuthUser:
    app_instance = None

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
                            messagebox.showinfo("kek", "Master password set successfully!")
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
            if not master_password_hash:
                return self.set_master_password()

            while True:
                entered_password = simpledialog.askstring("You Shall Not Pass", "Enter Master Password:", show="*")
                if not entered_password:
                    return False

                salt = keyring.get_password("password_manager", "salt")
                if not salt:
                    messagebox.showerror("Error", "Salt not found. Please set the master password.")
                    return False

                # Hash the entered password with the retrieved salt
                entered_password_hash = self.hash_master_password(entered_password, bytes.fromhex(salt))

                # Convert stored hash from hex to bytes
                stored_hash = bytes.fromhex(master_password_hash)

                # Compare the entered password hash with the stored hash
                if entered_password_hash == stored_hash:
                    app = PasswordManagerApp(self.root)
                    return True
                else:
                    messagebox.showerror("Error", "Incorrect master password. Please try again.")
                    return False

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred during authentication: {e}")
            return False

    def check_authentication(self):
        if self.prompt_for_master_password():
            try:
                root = tk.Tk()
                app = PasswordManagerApp(root)
                messagebox.showinfo("kek","security is just an illusion")
                root.mainloop()
                return True
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred while launching the Password Manager app: {e}")
                return False
        else:
            return False

if __name__ == "__main__":
    root = tk.Tk()
    auth_user = AuthUser(root)
    auth_user.check_authentication()
