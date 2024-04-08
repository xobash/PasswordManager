# Simple Password Manager by xobash

This is a python project that is built with Tkinter, SQLite, and AES encryption for securely storing and managing passwords. This project aims to build upon my security and python knowledge.

## Features:

- **Master Password Security:** Implements hashing of the master password using PBKDF2-HMAC-SHA256 algorithm along with salt to enhance security.
  
- **Keyring Integration:** Securely sets and retrieves the master password using the keyring library.
  
- **Secure Access:** Prompts the user to enter the master password for authentication before opening the application.
  
- **Secure Password Storage:** Encrypts passwords using AES encryption before storing them in the SQLite3 database.
  
- **Dark Mode:** Allows users to switch between light and dark modes according to their preference.
  
- **User-friendly Interface:** Provides a simple and intuitive interface for adding, viewing, and managing passwords easily.
  
- **Import and Export (Beta):** Supports importing passwords from and exporting passwords to a .csv file.
  
- **Search Functionality:** Enables users to retrieve passwords based on website names.
  
- **Settings Menu:** Provides quick access to import/export passwords and toggle dark mode.

## Getting Started:

1. **Clone the Repository:**

    ```
    git clone https://github.com/xobash/PasswordManager
    ```

2. **Navigate to the Project Directory:**

    ```
    cd password_manager
    ```

3. **Install Dependencies:**

    ```
    pip install -r requirements.txt
    ```

4. **Run the Application:**

    ```
    python password_manager.py
    ```

## Usage:

- **Signing In:** Upon first run, create a master password, securely stored using keyring for future authentication.

- **Adding a Password:** Click the "+" button to add a new password entry. Enter website, username, and password, then click "Store Securely".

- **Displaying Decryption Key (Beta):** Option to display the decryption key for manual storage.

- **Toggle Dark Mode:** Switch between light and dark mode from the settings menu.

- **Import and Export:** Import/export passwords from/to a .csv file via the settings menu.

- **Exiting the Application:** Select "Exit" from the settings menu.

## Contributions:

Contributions are welcome! Fork the repository, make your changes, and submit a pull request.

## Security Considerations:

- **Master Password Handling:** Implements secure hashing and salt usage for master password storage.
  
- **Encryption and Decryption:** Uses AES encryption for password storage; ensure proper key management.
  
- **Database Security:** Store SQLite database securely and restrict access appropriately.
  
- **GUI Security:** Validate and sanitize user inputs to prevent injection attacks. 
  
- **Error Handling:** Ensure consistent and informative error messages without leaking sensitive information.
