### Simple Password Manager by xobash

This is a simple password manager application built using Python and Tkinter GUI toolkit. It allows users to securely store their passwords using AES encryption and manage them easily.

#### Features:

1. **Secure Password Storage:** Passwords are encrypted using AES encryption before being stored in the SQLite3 database, ensuring basic security.
   
2. **Dark Mode:** Users can toggle between light and dark mode according to their preference.

3. **User-friendly Interface:** The application provides a simple and intuitive interface for users to add, view, and manage their passwords easily.

#### Getting Started:

You can compile the code youself if you like, however this is still a work in progress, and much of the functionality is still being worked on.

1. Clone the repository to your local machine:

    ```
    git clone https://github.com/xobash/PasswordManager
    ```

2. Navigate to the project directory:

    ```
    cd PasswordManager
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

- **Adding a Password:** Click on the "+" button to add a new password entry. Enter the website, username, and password, then click "Store Securely" to save the password to the db.

- **Displaying Decryption Key:** You can display the decryption key by clicking the "Display Decryption Key" button. Write down this key on a piece of paper.

- **Toggle Dark Mode:** Click on the settings menu (three horizontal lines in the top right) and select "Toggle Dark Mode" to switch between light and dark mode.

- **Exiting the Application:** To exit the application, click on the settings menu and select "Exit".

#### Contributions:

Contributions are welcome! If you'd like to contribute to the project, feel free to fork the repository, make your changes, and submit a pull request.
