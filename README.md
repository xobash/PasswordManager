### Simple Password Manager by xobash

This is a simple password manager application using Tkinter for the GUI, SQLite for the database, and AES encryption for storing passwords securely. 

#### Features:

- **Master Password:** Hashing of the master password using PBKDF2-HMAC-SHA256 algorithm.

- **Keyring integration:** Setting and retrieving the master password securely using the keyring library.

- **Secure Access:** Prompting the user to enter the master password for authentication.

- **Secure Password Storage:** Passwords are encrypted using AES encryption before being stored in the SQLite3 database.

- **Dark Mode:** Users can toggle between light and dark mode according to their preference.

- **User-friendly Interface:** The application provides a simple and intuitive interface for users to add, view, and manage their passwords easily.

- **Import and Export (Beta):** Users can import passwords from and export passwords to a .csv file.

- **Search Functionality:** Search functionality to retrieve passwords based on website names.

- **Settings Menu** Quick settings menu for importing/exporting passwords and toggling dark mode.

#### Getting Started:

You can compile the code yourself if you like; however, this is still a work in progress, and much of the functionality is still being worked on.

1. Clone the repository to your local machine:

    ```
    git clone https://github.com/xobash/PasswordManager
    ```

2. Navigate to the project directory:

    ```
    cd password_manager
    ```

3. Install the required dependencies:

    ```
    pip install -r requirements.txt
    ```

4. Run the application:

    ```
    python password_manager.py
    ```

#### Usage:

- **Signing in** Upon first compiling the code, you will be prompted to create a master password. This will be saved and stored securely in the keyring and used later to encrypt and decrypt your passwords securely within the program. 

- **Adding a Password:** Click on the "+" button to add a new password entry. Enter the website, username, and password, then click "Store Securely" to save the password to the db.

- **Displaying Decryption Key (Beta):** You can display the decryption key by clicking the "Display Decryption Key" button. Write down this key on a piece of paper.

- **Toggle Dark Mode:** Click on the settings menu (three horizontal lines in the top right) and select "Toggle Dark Mode" to switch between light and dark mode.

- **Import and Export:** Use the settings menu to import passwords from or export passwords to a .csv file.

- **Exiting the Application:** To exit the application, click on the settings menu and select "Exit".

#### Contributions:

Contributions are welcome! If you'd like to contribute to the project, feel free to fork the repository, make your changes, and submit a pull request.
